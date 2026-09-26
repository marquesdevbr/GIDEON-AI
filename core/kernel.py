from automation.tool_registry import create_tool_manager
from core.container import container
brain = container.get("brain")
memory = container.get("memory")
speaker = container.get("speaker")

from core.module_manager import ModuleManager
from core.state_manager import state_manager, State
from core.event_bus import event_bus

from brain.brain import Brain
from memory.memory import Memory
from voice.speaker import Speaker
from voice.listener import Listener


class Kernel:

    def __init__(self):
        self.manager = ModuleManager()

    def start(self):

        print("[Kernel] Inicializando...")

        tool_manager = create_tool_manager()

        brain = Brain(tool_manager=tool_manager)
        memory = Memory()
        speaker = Speaker()
        listener = Listener()

        self.manager.register(brain)
        self.manager.register(memory)
        self.manager.register(speaker)

        container.register("brain", brain)
        container.register("memory", memory)
        container.register("speaker", speaker)
        container.register("listener", listener)

        state_manager.set_state(State.ONLINE)

        event_bus.emit("kernel_started")

        print("[Kernel] Online.")


brain = container.get("brain")
memory = container.get("memory")
speaker = container.get("speaker")