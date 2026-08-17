import time

from voice.speaker import speaker


class GideonSystem:

    VERSION = "0.1.0 - Genesis"

    def __init__(self):
        self.modules = [
            "Core",
            "Brain",
            "Memory",
            "Voice",
            "Vision",
            "Security",
            "Database",
            "Interface"
        ]

    def load_modules(self):

        for module in self.modules:
            print(f"[ OK ] Carregando {module}...")
            time.sleep(0.4)

    def start(self):

        print("=" * 55)
        print("              GIDEON AI SYSTEM")
        print("           Sonekinha Systems")
        print("=" * 55)
        print()

        print(f"Versão: {self.VERSION}")
        print()

        self.load_modules()

        print()
        print("=" * 55)
        print("STATUS: ONLINE")
        print("Todos os módulos foram inicializados.")
        print("=" * 55)
        print()

        speaker.speak(
            "Inicialização concluída. "
            "Todos os sistemas estão operacionais. "
            "Boa noite, Gabriel. Como posso ajudá-lo?"
        )

    def shutdown(self):
        speaker.shutdown()