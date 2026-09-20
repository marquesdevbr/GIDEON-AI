import json
from openai import APIStatusError
from openai import OpenAI

from core.config import Config
from brain.providers.base_provider import BaseProvider
from brain.prompt_manager import SYSTEM_PROMPT

from automation.confirmation_manager import ConfirmationManager


class OpenRouterProvider(BaseProvider):

    def __init__(self, tool_manager=None):

        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=Config.OPENROUTER_API_KEY,
        )

        self.tool_manager = tool_manager

        self.confirmation = ConfirmationManager()

    def generate(self, messages):

        chat = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        chat.extend(messages)

        tools = None

        if self.tool_manager:

            tools = self.tool_manager.get_definitions()

        # ==========================================
        # PRIMEIRA CHAMADA
        # ==========================================

        try:

            response = self.client.chat.completions.create(

                model=Config.OPENROUTER_MODEL,
                messages=chat,
                tools=tools,
                tool_choice=(
                    "auto"
                    if tools
                    else None
                ),
                max_tokens=500
            )

        except APIStatusError as error:

            print(f"\n[ERRO API] {error}")

            return (
                "Dr. Marques, não consegui me conectar "
                "ao modelo de IA no momento. Pode ser "
                "um problema de créditos ou conexão "
                "com o OpenRouter."
            )

        # ==========================================
        # VERIFICAÇÃO DE SEGURANÇA
        # ==========================================

        if not response.choices:

            print(
                "\n[ERRO] O modelo não retornou "
                "nenhuma escolha."
            )

            print(
                "[ERRO] Resposta recebida:"
            )

            print(response)

            return (
                "Desculpe, Dr. Marques. "
                "Não consegui processar "
                "essa solicitação."
            )

        message = response.choices[0].message

        # ==========================================
        # SEM TOOL CALL
        # ==========================================

        if not message.tool_calls:

            return message.content

        # ==========================================
        # ADICIONAR MENSAGEM DO MODELO
        # ==========================================

        chat.append(
            message.model_dump(
                exclude_none=True
            )
        )

        # ==========================================
        # PROCESSAR FERRAMENTAS
        # ==========================================

        for tool_call in message.tool_calls:

            function_name = (
                tool_call.function.name
            )

            try:

                arguments = json.loads(
                    tool_call.function.arguments
                )

            except json.JSONDecodeError:

                result = (
                    "Não foi possível interpretar "
                    "os argumentos da ferramenta."
                )

                chat.append(
                    {
                        "role": "tool",
                        "tool_call_id": (
                            tool_call.id
                        ),
                        "content": result
                    }
                )

                continue

            print(
                f"\n[Tool Call] "
                f"{function_name}"
            )

            print(
                f"[Arguments] "
                f"{arguments}"
            )

            # ==================================
            # VERIFICAR AÇÕES PERIGOSAS
            # ==================================

            if function_name == "delete_file":

                path = arguments.get(
                    "path"
                )

                if not self.confirmation.has_pending_action():

                    confirmation_message = (
                        f"Dr. Marques, deseja "
                        f"realmente excluir "
                        f"'{path}'?"
                    )

                    self.confirmation.request_confirmation(

                        action=function_name,

                        description=(
                            confirmation_message
                        ),

                        data=arguments
                    )

                    print(
                        "\n[CONFIRMAÇÃO NECESSÁRIA]"
                    )

                    print(
                        confirmation_message
                    )

                    return confirmation_message

            # ==================================
            # EXECUTAR FERRAMENTA
            # ==================================

            result = self.tool_manager.execute(

                function_name,

                **arguments

            )

            print(
                f"[Tool Result] "
                f"{result}"
            )

            chat.append(
                {
                    "role": "tool",

                    "tool_call_id": (
                        tool_call.id
                    ),

                    "content": str(result)
                }
            )

        # ==========================================
        # SEGUNDA CHAMADA
        # ==========================================

        try:

            final_response = self.client.chat.completions.create(

                model=Config.OPENROUTER_MODEL,
                messages=chat,
                max_tokens=300
            )

        except APIStatusError as error:

            print(f"\n[ERRO API] {error}")

            return (
                "A ação foi executada, Dr. Marques, mas "
                "não consegui gerar a resposta final "
                "devido a um erro na API."
            )

        if not final_response.choices:

            return (
                "A ação foi executada, "
                "mas não consegui gerar "
                "a resposta final."
            )

        final_message = final_response.choices[0].message

        print(f"\n[DEBUG FINAL MESSAGE] {final_message}")

        return (
            final_message.content
            or "Pronto, Dr. Marques."
        )

    