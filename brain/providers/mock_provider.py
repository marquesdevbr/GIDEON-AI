from .base_provider import BaseProvider


class MockProvider(BaseProvider):

    def generate(self, messages):

        last = messages[-1]["content"]

        return f"[Mock] Recebi sua mensagem: {last}"