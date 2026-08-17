from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from interface.components.header import Header
from interface.components.core import Core
from interface.components.status import Status
from interface.components.logs import Logs

from core.kernel import Kernel


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

        center.addWidget(core,3)
        center.addWidget(status,1)

        layout.addWidget(header)
        layout.addLayout(center)
        layout.addWidget(logs)

        self.setLayout(layout)


def start_interface():

    app = QApplication([])

    window = GideonWindow()

    window.show()

    app.exec()