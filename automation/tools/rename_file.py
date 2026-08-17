import os


def rename_file(old_path, new_path):

    try:

        if not os.path.exists(old_path):

            return (
                f"Não encontrei o arquivo "
                f"'{old_path}'."
            )

        os.rename(
            old_path,
            new_path
        )

        return (
            f"O arquivo foi renomeado "
            f"com sucesso para '{new_path}'."
        )

    except Exception as error:

        return (
            f"Não consegui renomear "
            f"o arquivo: {error}"
        )


def register(manager):

    manager.register(
        name="rename_file",

        function=rename_file,

        description=(
            "Renomeia um arquivo ou pasta "
            "no computador."
        ),

        parameters={

            "type": "object",

            "properties": {

                "old_path": {
                    "type": "string",
                    "description": (
                        "Caminho atual do "
                        "arquivo ou pasta."
                    )
                },

                "new_path": {
                    "type": "string",
                    "description": (
                        "Novo caminho ou nome "
                        "do arquivo ou pasta."
                    )
                }

            },

            "required": [
                "old_path",
                "new_path"
            ]
        }
    )