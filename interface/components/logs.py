from PySide6.QtWidgets import QTextEdit


class Logs(QTextEdit):

    def __init__(self):
        super().__init__()

        self.setReadOnly(True)

        self.setStyleSheet("""
        QTextEdit{
            background:#0A0E14;
            border:1px solid #1E2430;
            border-radius:12px;
            padding:12px;
            font-family:'Inter','Segoe UI',sans-serif;
            font-size:14px;
        }
        """)

        self.log_system("Kernel iniciado")
        self.log_system("Brain Online")
        self.log_system("Memory Online")
        self.log_system("Voice Online")
        self.log_system("Interface pronta")

    def log(self, text):

        self.append(
            f'<span style="color:#E8ECF1;">{text}</span>'
        )

    def log_user(self, text):

        self.append(
            f'<div style="margin:8px 0;">'
            f'<span style="color:#6B7684;font-size:12px;">VOCÊ</span><br>'
            f'<span style="color:#E8ECF1;">{text}</span>'
            f'</div>'
        )

    def log_gideon(self, text):

        self.append(
            f'<div style="margin:8px 0;">'
            f'<span style="color:#00E5FF;font-size:12px;">GIDEON</span><br>'
            f'<span style="color:#E8ECF1;">{text}</span>'
            f'</div>'
        )

    def log_system(self, text):

        self.append(
            f'<span style="color:#6B7684;font-size:12px;">✓ {text}</span>'
        )