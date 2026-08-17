import os
import shutil


def delete_file(path, confirmed=False):

    if not os.path.exists(path):

        return (
            f"Não encontrei o arquivo "
            f"ou pasta '{path}'."
        )

    # Primeira tentativa: pedir confirmação
    if not confirmed:

        return (
            f"CONFIRMAÇÃO NECESSÁRIA: "
            f"O arquivo ou pasta '{path}' "
            f"será excluído. "
            f"Peça confirmação ao usuário "
            f"antes de continuar."
        )

    try:

        # Se for uma pasta
        if os.path.isdir(path):

            shutil.rmtree(path)

        # Se for um arquivo
        else:

            os.remove(path)

        return (
            f"'{path}' foi excluído "
            f"com sucesso."
        )

    except Exception as error:

        return (
            f"Não consegui excluir "
            f"'{path}': {error}"
        )


def register(manager):

    manager.register(
        name="delete_file",

        function=delete_file,

        description=(
            "Exclui um arquivo ou pasta. "
            "Antes de excluir, deve solicitar "
            "confirmação do usuário."
        ),

        parameters={

            "type": "object",

            "properties": {

                "path": {
                    "type": "string",
                    "description": (
                        "Caminho do arquivo "
                        "ou pasta."
                    )
                },

                "confirmed": {
                    "type": "boolean",
                    "description": (
                        "Indica se o usuário "
                        "confirmou a exclusão."
                    )
                }

            },

            "required": [
                "path"
            ]
        }
    )