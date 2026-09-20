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

        if not text:
            return

        speech_text = clean_for_speech(
            text
        )

        print(
            f"[GIDEON Voice] {text}"
        )

        print(
            f"[DEBUG VOICE] Limpo: "
            f"{speech_text}"
        )

        try:

            print(
                "[DEBUG VOICE] "
                "Iniciando streaming..."
            )

            audio_stream = (
                self.client.text_to_speech.stream(
                    voice_id=self.voice_id,
                    text=speech_text,
                    model_id="eleven_flash_v2_5"
                )
            )

            print(
                "[DEBUG VOICE] "
                "Reproduzindo áudio..."
            )

            stream(
                audio_stream
            )

            print(
                "[DEBUG VOICE] "
                "Fala concluída."
            )

        except Exception as error:

            print(
                f"[Voice] Erro ao falar: "
                f"{error}"
            )

    def stop(self):
        pass