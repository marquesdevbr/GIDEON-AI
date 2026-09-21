from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)
from PySide6.QtCore import QThread, Signal

from interface.components.command_input import CommandInput
from core.container import container
from interface.components.header import Header
from interface.components.core import Core
from interface.components.status import Status
from interface.components.logs import Logs

from core.kernel import Kernel


class BrainWorker(QThread):

    finished_processing = Signal(str)

    def __init__(self, text):
        super().__init__()
        self.text = text

    def run(self):

        brain = container.get("brain")

        response = brain.process(self.text)

        self.finished_processing.emit(response)


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

        self.command_input = command_input
        self.logs = logs
        self.worker = None

        center.addWidget(core,3)
        center.addWidget(status,1)

        layout.addWidget(header)
        layout.addLayout(center)
        layout.addWidget(command_input)
        layout.addWidget(logs)

        self.setLayout(layout)

    def handle_command(self, text):

        self.logs.log(f"🗣 Você: {text}")

        self.command_input.setEnabled(False)

        self.worker = BrainWorker(text)

        self.worker.finished_processing.connect(
            self.handle_response
        )

        self.worker.start()

    def handle_response(self, response):

        self.logs.log(f"🤖 GIDEON: {response}")

        speaker = container.get("speaker")

        if speaker:
            speaker.speak(response)

        self.command_input.setEnabled(True)


def start_interface():

    app = QApplication([])

    window = GideonWindow()

    window.show()

    app.exec()