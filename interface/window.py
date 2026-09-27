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
            background:#0A0E14;
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(16)

        header = Header()

        center = QHBoxLayout()
        center.setContentsMargins(20, 0, 20, 0)
        center.setSpacing(16)

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

        self.core = core
        self.command_input = command_input
        self.logs = logs
        self.brain_worker = None
        self.listener_worker = None

        center.addWidget(core,3)
        center.addWidget(status,1)

        content_margin_layout = QVBoxLayout()
        content_margin_layout.setContentsMargins(20, 0, 20, 20)
        content_margin_layout.setSpacing(16)

        content_margin_layout.addWidget(command_input)
        content_margin_layout.addWidget(logs)

        layout.addWidget(header)
        layout.addLayout(center)
        layout.addLayout(content_margin_layout)

        self.setLayout(layout)

        self.hotkey_worker = HotkeyWorker()

        self.hotkey_worker.hotkey_pressed.connect(
            self.start_listening
        )

        self.hotkey_worker.start()

        self.logs.log_system(
            f"Atalho global ativo: {HOTKEY.upper()}"
        )

        greeting = "Olá, Dr. Marques. Como você está hoje?"

        self.logs.log_gideon(greeting)

        speaker = container.get("speaker")

        if speaker:
            speaker.speak(greeting)

    def start_listening(self):

        if not self.command_input.mic_button.isEnabled():
            return

        self.core.set_state("listening")

        self.logs.log_system("Ouvindo...")

        self.command_input.set_busy(True)

        self.listener_worker = ListenerWorker()

        self.listener_worker.finished_listening.connect(
            self.handle_listened_text
        )

        self.listener_worker.start()

    def handle_listened_text(self, text):

        if not text:

            self.logs.log_system("Não entendi, tente novamente.")

            self.command_input.set_busy(False)

            self.core.set_state("idle")

            return

        self.handle_command(text)

    def handle_command(self, text):

        self.logs.log_user(text)

        self.core.set_state("thinking")

        self.command_input.set_busy(True)

        self.brain_worker = BrainWorker(text)

        self.brain_worker.finished_processing.connect(
            self.handle_response
        )

        self.brain_worker.start()

    def handle_response(self, response):

        self.logs.log_gideon(response)

        self.core.set_state("speaking")

        speaker = container.get("speaker")

        if speaker:
            speaker.speak(response)

        self.core.set_state("idle")

        self.command_input.set_busy(False)


def start_interface():

    app = QApplication([])

    window = GideonWindow()

    window.show()

    app.exec()