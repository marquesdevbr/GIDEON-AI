from voice.listener import Listener


def main():

    print(
        "=== GIDEON LISTENER TEST ==="
    )

    listener = Listener()

    while True:

        text = listener.listen(
            duration=5
        )

        if text:

            print(
                f"GIDEON recebeu: {text}"
            )

        print()


if __name__ == "__main__":

    main()