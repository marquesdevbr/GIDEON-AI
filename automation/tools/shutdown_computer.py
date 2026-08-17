import subprocess


def shutdown_computer(confirmed=False):

    # Primeira tentativa: pedir confirmação
    if not confirmed:

        return (
            "CONFIRMAÇÃO NECESSÁRIA: "
            "O computador será desligado. "
            "Peça confirmação ao usuário "
            "antes de continuar."
        )

    try:

        # Desligamento real do Windows
        subprocess.run(
            [
                "shutdown",
                "/s",
                "/t",
                "0"
            ],
            check=True
        )

        return (
            "O computador está sendo desligado."
        )

    except Exception as error:

        return (
            f"Não consegui desligar "
            f"o computador: {error}"
        )


def register(manager):

    manager.register(
        name="shutdown_computer",

        function=shutdown_computer,

        description=(
            "Desliga o computador Windows. "
            "SEMPRE deve solicitar confirmação "
            "explícita do usuário antes de executar."
        ),

        parameters={

            "type": "object",

            "properties": {

                "confirmed": {
                    "type": "boolean",
                    "description": (
                        "Indica se o usuário "
                        "confirmou explicitamente "
                        "o desligamento."
                    )
                }

            },

            "required": []
        }
    )