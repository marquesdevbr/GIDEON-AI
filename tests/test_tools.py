from automation.tool_registry import create_tool_manager


def main():

    tools = create_tool_manager()

    print("\n=== GIDEON TOOL SYSTEM ===\n")

    print(
        tools.execute(
            "open_website",
            url="https://www.google.com"
        )
    )

    print(
        tools.execute(
            "create_folder",
            path="GIDEON_TEST"
        )
    )

    print(
        tools.execute(
            "open_program",
            program="notepad"
        )
    )


if __name__ == "__main__":
    main()