class ToolManager:

    def __init__(self):
        self.tools = {}
        self.definitions = {}

    def register(self, name, function, description, parameters):

        self.tools[name] = function

        self.definitions[name] = {
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": parameters
            }
        }

    def execute(self, name, **kwargs):

        if name not in self.tools:
            return f"Ferramenta '{name}' não encontrada."

        try:
            return self.tools[name](**kwargs)

        except Exception as error:
            return f"Erro ao executar '{name}': {error}"

    def list_tools(self):

        return list(self.tools.keys())

    def get_definitions(self):

        return list(
            self.definitions.values()
        )