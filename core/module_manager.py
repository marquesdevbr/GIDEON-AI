class ModuleManager:

    def __init__(self):
        self.modules = {}

    def register(self, module):

        self.modules[module.name] = module

        module.initialize()

        print(f"[ModuleManager] {module.name} carregado.")

    def get(self, name):
        return self.modules.get(name)