from automation.confirmation_manager import ConfirmationManager


def main():

    confirmation = ConfirmationManager()

    print(
        confirmation.request_confirmation(
            action="delete_file",
            description=(
                "Deseja excluir o arquivo "
                "'teste.txt'?"
            ),
            data={
                "path": "teste.txt"
            }
        )
    )

    print()

    print(
        "Ação pendente:"
    )

    print(
        confirmation.get_pending_action()
    )

    print()

    print(
        "Confirmando..."
    )

    action = confirmation.confirm()

    print(
        "Ação confirmada:"
    )

    print(
        action
    )

    print()

    print(
        "Existe ação pendente?"
    )

    print(
        confirmation.has_pending_action()
    )


if __name__ == "__main__":

    main()