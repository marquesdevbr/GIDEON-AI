from brain.providers.openrouter_provider import OpenRouterProvider


class AIEngine:

    def __init__(self, tool_manager=None):

        self.tool_manager = tool_manager

        self.provider = OpenRouterProvider(
            tool_manager=tool_manager
        )

    def initialize(self):

        print(
            "[AI Engine] Online."
        )

        if self.tool_manager:

            tools = (
                self.tool_manager
                .list_tools()
            )

            print(
                f"[AI Engine] "
                f"{len(tools)} "
                f"ferramentas disponíveis."
            )

            for tool in tools:

                print(
                    f"[AI Engine] "
                    f"Tool: {tool}"
                )

    def generate(
        self,
        conversation
    ):

        return (
            self.provider
            .generate(
                conversation
            )
        )

    def has_pending_confirmation(self):

        return (
            self.provider
            .confirmation
            .has_pending_action()
        )

    def confirm_action(self):

        action = (
            self.provider
            .confirmation
            .confirm()
        )

        if not action:

            return (
                "Não existe nenhuma "
                "ação pendente."
            )

        if action["action"] == "delete_file":

            data = action.get(
                "data",
                {}
            )

            path = data.get(
                "path"
            )

            if not path:

                return (
                    "O caminho do arquivo "
                    "não foi informado."
                )

            result = (
                self.tool_manager
                .execute(
                    "delete_file",
                    path=path,
                    confirmed=True
                )
            )

            return result

        return (
            "Ação confirmada, mas "
            "ainda não possui "
            "um executor."
        )

    def cancel_action(self):

        return (
            self.provider
            .confirmation
            .cancel()
        )