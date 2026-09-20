import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.stderr.reconfigure(encoding="utf-8")

from automation.tool_registry import create_tool_manager
from brain.brain import Brain
from voice.listener import Listener
from voice.speaker import Speaker


def main():

    print("=== GIDEON SYSTEM ===")

    listener = Listener()
    speaker = Speaker()

    tool_manager = create_tool_manager()
    brain = Brain(tool_manager=tool_manager)

    brain.initialize()

    print()
    print(
        "GIDEON está pronta."
    )

    # ==============================
    # SAUDAÇÃO INICIAL
    # ==============================

    greeting = (
        "Olá, Dr. Marques. "
        "Como você está hoje?"
    )

    print(
        f"GIDEON: {greeting}"
    )

    speaker.speak(
        greeting
    )

    # ==============================
    # LOOP PRINCIPAL
    # ==============================

    while True:

        text = listener.listen()

        if not text:
            continue

        # ==============================
        # COMANDO PARA ENCERRAR
        # ==============================

        if text.lower().strip() in [
            "encerrar",
            "sair",
            "desligar gideon"
        ]:

            goodbye = (
                "Até logo, "
                "Dr. Marques."
            )

            print(
                f"GIDEON: {goodbye}"
            )

            speaker.speak(
                goodbye
            )

            break

        # ==============================
        # PROCESSAR COMANDO
        # ==============================

        response = brain.process(
            text
        )

        print(
            f"GIDEON: {response}"
        )

        speaker.speak(
            response
        )

        print(
            "[DEBUG] Resposta enviada para voz."
        )


if __name__ == "__main__":

    main()