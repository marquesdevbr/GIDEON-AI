import webbrowser


def open_website(url):

    try:

        webbrowser.open(
            url
        )

        return (
            f"O site {url} "
            f"foi aberto com sucesso."
        )

    except Exception as error:

        return (
            f"Não consegui abrir "
            f"o site: {error}"
        )


def register(manager):

    manager.register(
        name="open_website",

        function=open_website,

        description=(
            "Abre um site no "
            "navegador padrão."
        ),

        parameters={

            "type": "object",

            "properties": {

                "url": {
                    "type": "string",
                    "description": (
                        "Endereço do site "
                        "que deve ser aberto."
                    )
                }

            },

            "required": [
                "url"
            ]
        }
    )