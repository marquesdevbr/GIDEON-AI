from voice.speaker import Speaker


def main():

    speaker = Speaker()

    speaker.speak(
        "Primeira mensagem, Dr. Marques."
    )

    speaker.speak(
        "Segunda mensagem, Dr. Marques."
    )

    speaker.speak(
        "Terceira mensagem, Dr. Marques."
    )


if __name__ == "__main__":
    main()