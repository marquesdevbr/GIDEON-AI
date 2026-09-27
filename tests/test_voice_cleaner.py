from voice.speaker import Speaker


def main():

    speaker = Speaker()

    speaker.speak(
        "**Preço do petróleo:** "
        "US$ 70 por barril."
    )

    speaker.speak(
        "*Esta é uma mensagem de teste.* "
        "O valor é $100."
    )


if __name__ == "__main__":

    main()