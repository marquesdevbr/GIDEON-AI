from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton
from PySide6.QtCore import Signal


class CommandInput(QWidget):

    command_submitted = Signal(str)

    def __init__(self):
        super().__init__()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText(
            "Digite um comando para a GIDEON..."
        )

        self.send_button = QPushButton("Enviar")

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

        layout = QHBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        self.send_button.clicked.connect(self.submit)
        self.input_field.returnPressed.connect(self.submit)

    def submit(self):

        text = self.input_field.text().strip()

        if not text:
            return

        self.input_field.clear()

        self.command_submitted.emit(text)