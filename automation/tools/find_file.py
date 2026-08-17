import os


def find_file(filename):

    filename = filename.lower().strip()

    # Começa a busca na pasta do projeto
    search_path = os.getcwd()

    results = []

    for root, dirs, files in os.walk(search_path):

        for file in files:

            if filename in file.lower():

                full_path = os.path.join(
                    root,
                    file
                )

                results.append(
                    full_path
                )

                # Limita a 10 resultados
                if len(results) >= 10:
                    break

        if len(results) >= 10:
            break

    if not results:

        return (
            f"Não encontrei nenhum arquivo "
            f"chamado '{filename}'."
        )

    response = (
        f"Encontrei {len(results)} "
        f"arquivo(s):\n"
    )

    for result in results:

        response += (
            f"- {result}\n"
        )

    return response


def register(manager):

    manager.register(
        name="find_file",

        function=find_file,

        description=(
            "Procura um arquivo pelo nome "
            "dentro do diretório atual."
        ),

        parameters={

            "type": "object",

            "properties": {

                "filename": {
                    "type": "string",
                    "description": (
                        "Nome ou parte do nome "
                        "do arquivo que deve "
                        "ser encontrado."
                    )
                }

            },

            "required": [
                "filename"
            ]
        }
    )