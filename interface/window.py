from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import QThread, Signal

import keyboard

from interface.components.command_input import CommandInput
from core.container import container
from interface.components.header import Header
from interface.components.core import Core
from interface.components.status import Status
from interface.components.logs import Logs

from core.kernel import Kernel


HOTKEY = "f9"


class BrainWorker(QThread):

    finished_processing = Signal(str)

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):

        brain = container.get("brain")

        response = brain.process(self.text)

        self.finished_processing.emit(response)


class ListenerWorker(QThread):

    finished_listening = Signal(str)

    def run(self):

        listener = container.get("listener")

        text = listener.listen()

        self.finished_listening.emit(text or "")


class HotkeyWorker(QThread):

    hotkey_pressed = Signal()

    def run(self):

        keyboard.add_hotkey(
            HOTKEY,
            lambda: self.hotkey_pressed.emit()
        )

        keyboard.wait()


class GideonWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.kernel = Kernel()
        self.kernel.start()

        self.setWindowTitle("GIDEON")

        self.resize(1200,700)

        self.setStyleSheet("""
            background:#05070A;
        """)

        layout = QVBoxLayout()

        header = Header()

        center = QHBoxLayout()

        core = Core()

        status = Status()

        logs = Logs()

        command_input = CommandInput()

        command_input.command_submitted.connect(
            self.handle_command
        )

        command_input.mic_clicked.connect(
            self.start_listening
        )

        self.command_input = command_input
        self.logs = logs
        self.brain_worker = None
        self.listener_worker = None

        center.addWidget(core,3)
        center.addWidget(status,1)

        layout.addWidget(header)
        layout.addLayout(center)
        layout.addWidget(command_input)
        layout.addWidget(logs)

        self.setLayout(layout)

        self.hotkey_worker = HotkeyWorker()

        self.hotkey_worker.hotkey_pressed.connect(
            self.start_listening
        )

        self.hotkey_worker.start()

        self.logs.log(
            f"⌨ Atalho global ativo: {HOTKEY.upper()}"
        )

    def start_listening(self):

        if not self.command_input.mic_button.isEnabled():
            return

        self.logs.log("🎤 Ouvindo...")

        self.command_input.set_busy(True)

        self.listener_worker = ListenerWorker()

        self.listener_worker.finished_listening.connect(
            self.handle_listened_text
        )

        self.listener_worker.start()

    def handle_listened_text(self, text):

        if not text:

            self.logs.log("🎤 Não entendi, tente novamente.")

            self.command_input.set_busy(False)

            return

        self.handle_command(text)

    def handle_command(self, text):

        self.logs.log(f"🗣 Você: {text}")

        self.command_input.set_busy(True)

        self.brain_worker = BrainWorker(text)

        self.brain_worker.finished_processing.connect(
            self.handle_response
        )

        self.brain_worker.start()

    def handle_response(self, response):

        self.logs.log(f"🤖 GIDEON: {response}")

        speaker = container.get("speaker")

        if speaker:
            speaker.speak(response)

        self.command_input.set_busy(False)


def start_interface():

    app = QApplication([])

    window = GideonWindow()

    window.show()

    app.exec()