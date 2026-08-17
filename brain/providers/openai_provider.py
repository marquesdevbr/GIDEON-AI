from .base_provider import BaseProvider


class OpenAIProvider(BaseProvider):

    def __init__(self, client=None):
        self.client = client

    def generate(self, messages):

        raise NotImplementedError(
            "A integração real será implementada após configurarmos o provedor escolhido."
        )