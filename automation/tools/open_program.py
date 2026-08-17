import os
import subprocess
from pathlib import Path


def find_program_in_start_menu(program_name):

    program_name = program_name.lower().strip()

    start_menu_paths = [
        os.path.expandvars(
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs"
        ),
        os.path.expandvars(
            r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs"
        )
    ]

    for base_path in start_menu_paths:

        if not os.path.exists(base_path):
            continue

        for root, dirs, files in os.walk(base_path):

            for file in files:

                file_name = Path(file).stem.lower()

                if (
                    program_name == file_name
                    or program_name in file_name
                ):

                    full_path = os.path.join(
                        root,
                        file
                    )

                    if file.lower().endswith(".lnk"):

                        return full_path

                    if file.lower().endswith(".exe"):

                        return full_path

    return None


def find_program_executable(program_name):

    program_name = program_name.lower().strip()

    search_paths = [
        os.path.expandvars(
            r"%LOCALAPPDATA%\Programs"
        ),
        os.path.expandvars(
            r"%LOCALAPPDATA%"
        ),
        os.path.expandvars(
            r"%PROGRAMFILES%"
        ),
        os.path.expandvars(
            r"%PROGRAMFILES(x86)%"
        )
    ]

    for base_path in search_paths:

        if not os.path.exists(base_path):
            continue

        for root, dirs, files in os.walk(base_path):

            for file in files:

                if not file.lower().endswith(".exe"):
                    continue

                file_name = Path(file).stem.lower()

                if (
                    program_name == file_name
                    or program_name in file_name
                ):

                    return os.path.join(
                        root,
                        file
                    )

    return None


def open_program(program):

    program = program.strip()

    # 1. Procurar no Menu Iniciar
    start_menu_path = find_program_in_start_menu(
        program
    )

    if start_menu_path:

        try:

            os.startfile(
                start_menu_path
            )

            return (
                f"O programa {program} "
                f"foi aberto com sucesso."
            )

        except Exception as error:

            return (
                f"Encontrei o atalho de {program}, "
                f"mas não consegui abri-lo: {error}"
            )

    # 2. Procurar executável
    executable_path = find_program_executable(
        program
    )

    if executable_path:

        try:

            subprocess.Popen(
                [executable_path]
            )

            return (
                f"O programa {program} "
                f"foi aberto com sucesso."
            )

        except Exception as error:

            return (
                f"Encontrei o executável de {program}, "
                f"mas não consegui abri-lo: {error}"
            )

    return (
        f"Não encontrei o programa "
        f"'{program}' no computador."
    )


def register(manager):

    manager.register(
        name="open_program",

        function=open_program,

        description=(
            "Abre um programa instalado "
            "no computador pelo nome."
        ),

        parameters={

            "type": "object",

            "properties": {

                "program": {
                    "type": "string",
                    "description": (
                        "Nome do programa "
                        "que deve ser aberto."
                    )
                }

            },

            "required": [
                "program"
            ]
        }
    )