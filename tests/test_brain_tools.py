from automation.tool_registry import create_tool_manager
from brain.brain import Brain


def main():

    print()
    print("=== GIDEON TOOL SYSTEM ===")
    print()

    tool_manager = create_tool_manager()

    brain = Brain(
        tool_manager=tool_manager
    )

    brain.initialize()

    print()

    while True:

        text = input("Dr. Marques: ")

        if text.lower() in [
            "sair",
            "exit",
            "quit"
        ]:

            print()
            print(
                "GIDEON: Até logo, Dr. Marques."
            )

            break

        response = brain.process(
            text
        )

        print()
        print(
            f"GIDEON: {response}"
        )
        print()


if __name__ == "__main__":
    main()