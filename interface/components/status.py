from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QProgressBar
)
from PySide6.QtCore import QTimer
import psutil


class Status(QFrame):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
        QFrame{
            background:#12161F;
            border:1px solid #1E2430;
            border-radius:12px;
        }

        QLabel{
            color:#E8ECF1;
            font-family:'Inter','Segoe UI',sans-serif;
            font-size:13px;
        }

        QProgressBar{
            background:#0A0E14;
            border:1px solid #1E2430;
            border-radius:6px;
            height:10px;
            text-align:center;
            color:transparent;
        }

        QProgressBar::chunk{
            background:#00E5FF;
            border-radius:6px;
        }
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(14)

        self.cpu_label = QLabel("CPU")
        self.cpu_bar = QProgressBar()
        self.cpu_bar.setMaximum(100)
        self.cpu_bar.setTextVisible(False)

        self.ram_label = QLabel("RAM")
        self.ram_bar = QProgressBar()
        self.ram_bar.setMaximum(100)
        self.ram_bar.setTextVisible(False)

        layout.addWidget(self.cpu_label)
        layout.addWidget(self.cpu_bar)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.ram_bar)

        layout.addSpacing(10)

        self.services = {}

        for name in ["IA", "VOZ", "MEMÓRIA"]:

            row = QHBoxLayout()

            name_label = QLabel(name)
            name_label.setStyleSheet("color:#6B7684;")

            value_label = QLabel("● ONLINE")
            value_label.setStyleSheet("color:#3DDC97;")

            self.services[name] = value_label

            row.addWidget(name_label)
            row.addStretch()
            row.addWidget(value_label)

            layout.addLayout(row)

        layout.addStretch()

        self.setLayout(layout)

        timer = QTimer(self)
        timer.timeout.connect(self.update_status)
        timer.start(1000)

        self.update_status()

    def update_status(self):

        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent

        self.cpu_bar.setValue(int(cpu))
        self.ram_bar.setValue(int(ram))

        self.cpu_label.setText(f"CPU   {cpu:.0f}%")
        self.ram_label.setText(f"RAM   {ram:.0f}%")