from brain.brain import Brain
from voice.listener import Listener
from voice.speaker import Speaker


def main():

    print(
        "=== GIDEON SYSTEM ==="
    )

    # ==============================
    # INICIALIZAR SISTEMA DE VOZ
    # ==============================

    listener = Listener()

    # ==============================
    # INICIALIZAR CÉREBRO
    # ==============================
    
    speaker = Speaker()

    brain = Brain()

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