from core.module import Module

from brain.ai_engine import AIEngine
from brain.conversation import Conversation


class Brain(Module):

    def __init__(
        self,
        tool_manager=None
    ):

        super().__init__(
            name="Brain"
        )

        self.conversation = (
            Conversation()
        )

        self.ai = AIEngine(
            tool_manager=tool_manager
        )

    def initialize(self):

        self.ai.initialize()

        print(
            "[Brain] Online."
        )

    def process(self, text):

        text_lower = (
            text
            .lower()
            .strip()
        )

        # ======================================
        # CONFIRMAÇÃO PENDENTE
        # ======================================

        if (
            self.ai
            .has_pending_confirmation()
        ):

            if text_lower in [
                "sim",
                "s",
                "confirmo",
                "confirmar",
                "pode",
                "pode sim",
                "autorizo"
            ]:

                return (
                    self.ai
                    .confirm_action()
                )

            if text_lower in [
                "não",
                "nao",
                "n",
                "cancela",
                "cancelar"
            ]:

                return (
                    self.ai
                    .cancel_action()
                )

            return (
                "Dr. Marques, preciso saber "
                "se deseja confirmar a ação. "
                "Responda sim ou não."
            )

        # ======================================
        # CONVERSA NORMAL
        # ======================================

        self.conversation.add(
            "user",
            text
        )

        response = (
            self.ai
            .generate(
                self.conversation.history()
            )
        )

        self.conversation.add(
            "assistant",
            response
        )

        return response