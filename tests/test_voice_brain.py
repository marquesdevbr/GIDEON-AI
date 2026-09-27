from brain.brain import Brain
from voice.listener import Listener
from voice.speaker import Speaker

from automation.tool_registry import create_tool_manager


def main():

    print(
        "=== GIDEON VOICE SYSTEM ==="
    )

    # Sistema de escuta
    listener = Listener()

    # Sistema de fala
    speaker = Speaker()

    # Carrega todas as ferramentas
    tool_manager = create_tool_manager()

    print(
        f"[Tools] "
        f"{len(tool_manager.list_tools())} "
        f"ferramentas carregadas."
    )

    # Cria o cérebro com acesso às ferramentas
    brain = Brain(
        tool_manager=tool_manager
    )

    brain.initialize()

    print()

    print(
        "GIDEON está pronta."
    )

    while True:

        text = listener.listen(
            duration=5
        )

        if not text:
            continue

        # ======================================
        # COMANDO PARA ENCERRAR
        # ======================================

        if text.lower().strip() in [
            "encerrar",
            "sair",
            "desligar gideon"
        ]:

            goodbye = (
                "Até logo, Dr. Marques."
            )

            print(
                f"GIDEON: {goodbye}"
            )

            speaker.speak(
                goodbye
            )

            break

        # ======================================
        # PROCESSAR COMANDO
        # ======================================

        response = brain.process(
            text
        )

        print(
            f"GIDEON: {response}"
        )

        # ======================================
        # FALAR RESPOSTA
        # ======================================

        speaker.speak(
            response
        )

        print(
            "[DEBUG] Resposta enviada para voz."
        )


if __name__ == "__main__":

    main()