from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt, QTimer
from datetime import datetime


class Header(QWidget):

    def __init__(self):
        super().__init__()

        self.title = QLabel("GIDEON")

        self.status = QLabel("🟢 ONLINE")

        self.clock = QLabel()

        self.title.setStyleSheet("""
            color:#00E5FF;
            font-size:28px;
            font-weight:bold;
        """)

        self.status.setStyleSheet("""
            color:#00FF7F;
            font-size:18px;
        """)

        self.clock.setStyleSheet("""
            color:white;
            font-size:18px;
        """)

        layout = QHBoxLayout()

        layout.addWidget(self.title)

        layout.addStretch()

        layout.addWidget(self.status)

        layout.addSpacing(30)

        layout.addWidget(self.clock)

        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):

        self.clock.setText(
            datetime.now().strftime("%H:%M:%S")
        )