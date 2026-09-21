import difflib

WAKE_WORD_VARIANTS = [
    "gideon",
    "guidao",
    "guidão",
    "guido",
    "gedeao",
    "gideao",
    "lirio",
    "miriam"
]

def extract_command_after_wake_word(text):

    words = text.lower().split()

    if not words:
        return None

    first_word = words[0]

    match = difflib.get_close_matches(
        first_word,
        WAKE_WORD_VARIANTS,
        n=1,
        cutoff=0.6
    )

    if not match:
        return None

    return " ".join(words[1:]).strip()


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

        command = extract_command_after_wake_word(text)

        if command is None:

            print(
                "[GIDEON] Palavra de ativação "
                "não detectada, ignorando."
            )

            continue

        if not command:

            speaker.speak("Sim, Dr. Marques?")

            continue

        text = command

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