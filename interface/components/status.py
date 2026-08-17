from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer
import psutil


class Status(QFrame):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background:#10151C;
            border:1px solid #00E5FF;
            border-radius:10px;
        }

        QLabel{
            color:white;
            font-size:15px;
        }
        """)

        self.label = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(self.label)

        self.setLayout(layout)

        timer = QTimer(self)

        timer.timeout.connect(self.update_status)

        timer.start(1000)

        self.update_status()

    def update_status(self):

        cpu = psutil.cpu_percent()

        ram = psutil.virtual_memory().percent

        self.label.setText(f"""
CPU ........ {cpu}%

RAM ........ {ram}%

IA ......... ONLINE

VOICE ...... ONLINE

MEMORY ..... ONLINE

EVENT BUS .. ONLINE
""")