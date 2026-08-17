import io
import wave

import numpy as np
import sounddevice as sd
import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        self.sample_rate = 16000

        self.channels = 1

        # Volume mínimo considerado como voz
        self.energy_threshold = 500

        # Tempo de silêncio para encerrar a fala
        self.silence_duration = 1.2

        # Tamanho de cada bloco de áudio
        self.block_duration = 0.1

        print(
            "[Listener] Sistema de voz online."
        )

    def listen(self):

        print(
            "\n[GIDEON] Estou ouvindo..."
        )

        audio_chunks = []

        silence_time = 0

        has_started_speaking = False

        try:

            print(
                "[GIDEON] Pode falar..."
            )

            while True:

                frames = int(
                    self.sample_rate
                    * self.block_duration
                )

                audio_data = sd.rec(
                    frames,
                    samplerate=self.sample_rate,
                    channels=self.channels,
                    dtype="int16"
                )

                sd.wait()

                audio_chunks.append(
                    audio_data.copy()
                )

                # Calcula o volume médio
                # do bloco de áudio
                volume = np.abs(
                    audio_data
                ).mean()

                # Detecta se existe voz
                if volume > self.energy_threshold:

                    has_started_speaking = True

                    silence_time = 0

                else:

                    if has_started_speaking:

                        silence_time += (
                            self.block_duration
                        )

                # Se a pessoa começou a falar
                # e ficou em silêncio pelo tempo
                # configurado, encerra a gravação
                if (
                    has_started_speaking
                    and silence_time
                    >= self.silence_duration
                ):

                    break

        except Exception as error:

            print(
                f"[Listener] Erro ao capturar "
                f"o microfone: {error}"
            )

            return None

        try:

            # Junta todos os blocos
            audio_data = np.concatenate(
                audio_chunks,
                axis=0
            )

            audio_bytes = (
                audio_data
                .tobytes()
            )

            wav_buffer = io.BytesIO()

            with wave.open(
                wav_buffer,
                "wb"
            ) as wav_file:

                wav_file.setnchannels(
                    self.channels
                )

                wav_file.setsampwidth(
                    2
                )

                wav_file.setframerate(
                    self.sample_rate
                )

                wav_file.writeframes(
                    audio_bytes
                )

            wav_buffer.seek(0)

            with sr.AudioFile(
                wav_buffer
            ) as source:

                audio = (
                    self.recognizer
                    .record(source)
                )

        except Exception as error:

            print(
                f"[Listener] Erro ao processar "
                f"o áudio: {error}"
            )

            return None

        try:

            text = (
                self.recognizer
                .recognize_google(
                    audio,
                    language="pt-BR"
                )
            )

            print(
                f"[Você] {text}"
            )

            return text

        except sr.UnknownValueError:

            print(
                "[GIDEON] Não consegui entender."
            )

            return None

        except sr.RequestError as error:

            print(
                "[GIDEON] Erro no serviço "
                f"de reconhecimento: {error}"
            )

            return None