from core.state_manager import state_manager, State


class CommandCenter:

    def __init__(self, logs):
        self.logs = logs

    def set_online(self):
        state_manager.set_state(State.ONLINE)
        self.logs.log("🟢 Sistema Online")

    def listen(self):
        state_manager.set_state(State.LISTENING)
        self.logs.log("🎤 Ouvindo...")

    def think(self):
        state_manager.set_state(State.THINKING)
        self.logs.log("🧠 Processando...")

    def speak(self, text):
        state_manager.set_state(State.SPEAKING)
        self.logs.log(f"🗣️ {text}")

    def execute(self, command):
        state_manager.set_state(State.EXECUTING)
        self.logs.log(f"⚙️ Executando: {command}")

    def error(self, text):
        state_manager.set_state(State.ERROR)
        self.logs.log(f"❌ {text}")