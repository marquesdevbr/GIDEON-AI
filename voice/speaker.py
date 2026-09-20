from elevenlabs.client import ElevenLabs
from elevenlabs import stream

from core.config import Config
from core.module import Module
from voice.text_cleaner import clean_for_speech


class Speaker(Module):

    def __init__(self):

        super().__init__(name="Speaker")

        self.voice_id = (
            "TwvqKemQ2RhSGYoQgC6l"
        )

        self.client = ElevenLabs(
            api_key=Config.ELEVENLABS_API_KEY
        )

        print(
            "[Voice] ElevenLabs conectado."
        )

        print(
            "[Voice] Voz da GIDEON configurada."
        )

    def initialize(self):
        pass

    def speak(self, text):
        # resto do método continua igual
        ...

    def stop(self):
        pass