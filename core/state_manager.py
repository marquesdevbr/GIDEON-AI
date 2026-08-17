from enum import Enum


class State(Enum):

    ONLINE = "online"
    LISTENING = "listening"
    THINKING = "thinking"
    SPEAKING = "speaking"
    EXECUTING = "executing"
    ERROR = "error"


class StateManager:

    def __init__(self):

        self.state = State.ONLINE

        self.callbacks = []

    def register(self, callback):

        self.callbacks.append(callback)

    def set_state(self, state):

        self.state = state

        for callback in self.callbacks:
            callback(state)

    def get_state(self):

        return self.state


state_manager = StateManager()