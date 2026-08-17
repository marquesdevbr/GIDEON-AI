import os


def create_folder(path):

    try:

        os.makedirs(
            path,
            exist_ok=True
        )

        return (
            f"A pasta '{path}' "
            f"foi criada com sucesso."
        )

    except Exception as error:

        return (
            f"Não consegui criar "
            f"a pasta: {error}"
        )


def register(manager):

    manager.register(
        name="create_folder",

        function=create_folder,

        description=(
            "Cria uma nova pasta "
            "no computador."
        ),

        parameters={

            "type": "object",

            "properties": {

                "path": {
                    "type": "string",
                    "description": (
                        "Caminho ou nome "
                        "da pasta."
                    )
                }

            },

            "required": [
                "path"
            ]
        }
    )