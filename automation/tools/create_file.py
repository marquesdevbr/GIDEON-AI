import os


def create_file(path, content=""):

    try:

        # Cria as pastas necessárias
        folder = os.path.dirname(path)

        if folder:
            os.makedirs(
                folder,
                exist_ok=True
            )

        # Cria o arquivo
        with open(
            path,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(content)

        return (
            f"O arquivo '{path}' "
            f"foi criado com sucesso."
        )

    except Exception as error:

        return (
            f"Não consegui criar "
            f"o arquivo '{path}': {error}"
        )


def register(manager):

    manager.register(
        name="create_file",

        function=create_file,

        description=(
            "Cria um novo arquivo "
            "no computador."
        ),

        parameters={

            "type": "object",

            "properties": {

                "path": {
                    "type": "string",
                    "description": (
                        "Caminho e nome "
                        "do arquivo."
                    )
                },

                "content": {
                    "type": "string",
                    "description": (
                        "Conteúdo que será "
                        "colocado no arquivo."
                    )
                }

            },

            "required": [
                "path"
            ]
        }
    )