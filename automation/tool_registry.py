import importlib
import inspect
import pkgutil

from automation.tool_manager import ToolManager


def create_tool_manager():

    manager = ToolManager()

    package_name = "automation.tools"

    package = importlib.import_module(
        package_name
    )

    for module_info in pkgutil.iter_modules(
        package.__path__
    ):

        module_name = module_info.name

        if module_name.startswith("_"):
            continue

        module = importlib.import_module(
            f"{package_name}.{module_name}"
        )

        register_function = getattr(
            module,
            "register",
            None
        )

        if register_function:

            register_function(
                manager
            )

    return manager