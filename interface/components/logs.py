from PySide6.QtWidgets import QTextEdit


class Logs(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setStyleSheet("""
        QTextEdit{
            background:#10151C;
            color:#00E5FF;
            border:1px solid #00E5FF;
            font-size:14px;
        }
        """)

        self.log("✔ Kernel iniciado")
        self.log("✔ Brain Online")
        self.log("✔ Memory Online")
        self.log("✔ Voice Online")
        self.log("✔ Interface pronta")

    def log(self, text):

        self.append(text)