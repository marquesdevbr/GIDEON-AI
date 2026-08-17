import os
import shutil


def move_file(source, destination):

    try:

        if not os.path.exists(source):

            return (
                f"Não encontrei o arquivo "
                f"ou pasta '{source}'."
            )

        # Cria a pasta de destino caso não exista
        if not os.path.exists(destination):

            os.makedirs(
                destination,
                exist_ok=True
            )

        # Monta o caminho final
        final_destination = os.path.join(
            destination,
            os.path.basename(source)
        )

        shutil.move(
            source,
            final_destination
        )

        return (
            f"'{source}' foi movido com sucesso "
            f"para '{final_destination}'."
        )

    except Exception as error:

        return (
            f"Não consegui mover "
            f"'{source}': {error}"
        )


def register(manager):

    manager.register(
        name="move_file",

        function=move_file,

        description=(
            "Move um arquivo ou pasta "
            "para outro local."
        ),

        parameters={

            "type": "object",

            "properties": {

                "source": {
                    "type": "string",
                    "description": (
                        "Caminho do arquivo "
                        "ou pasta que será movido."
                    )
                },

                "destination": {
                    "type": "string",
                    "description": (
                        "Pasta para onde o arquivo "
                        "ou pasta será movido."
                    )
                }

            },

            "required": [
                "source",
                "destination"
            ]
        }
    )