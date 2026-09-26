from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal


class CommandInput(QWidget):

    command_submitted = Signal(str)
    mic_clicked = Signal()

    def __init__(self):
        super().__init__()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText(
            "Digite um comando para a GIDEON..."
        )

        self.send_button = QPushButton("Enviar")

        self.mic_button = QPushButton("🎤")

        self.input_field.setStyleSheet("""
            QLineEdit{
                background:#10151C;
                color:white;
                border:1px solid #00E5FF;
                border-radius:6px;
                padding:8px;
                font-size:14px;
            }
        """)

        self.send_button.setStyleSheet("""
            QPushButton{
                background:#00E5FF;
                color:#05070A;
                border-radius:6px;
                padding:8px 16px;
                font-weight:bold;
            }
        """)

        self.mic_button.setStyleSheet("""
            QPushButton{
                background:#10151C;
                color:#00E5FF;
                border:1px solid #00E5FF;
                border-radius:6px;
                padding:8px 12px;
                font-size:16px;
            }
        """)

        layout = QHBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        layout.addWidget(self.mic_button)
        self.setLayout(layout)

        self.send_button.clicked.connect(self.submit)
        self.input_field.returnPressed.connect(self.submit)
        self.mic_button.clicked.connect(self.mic_clicked.emit)

    def submit(self):

        text = self.input_field.text().strip()

        if not text:
            return

        self.input_field.clear()

        self.command_submitted.emit(text)

    def set_busy(self, busy):

        self.input_field.setEnabled(not busy)
        self.send_button.setEnabled(not busy)
        self.mic_button.setEnabled(not busy)