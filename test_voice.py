from voice.speaker import Speaker


def main():

    print(
        "=== GIDEON VOICE TEST ==="
    )

    speaker = Speaker()

    speaker.speak(
        "Olá, Dr. Marques. "
        "É um prazer falar com você."
    )


if __name__ == "__main__":

    main()