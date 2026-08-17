from core.module import Module


class Memory(Module):

    def __init__(self):
        super().__init__("Memory")
        self.history = []

    def initialize(self):
        print("[Memory] Online.")

    def add(self, text):
        self.history.append(text)