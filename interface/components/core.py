from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QTimer
import math


STATE_COLORS = {
    "idle": QColor("#00E5FF"),
    "listening": QColor("#7B61FF"),
    "thinking": QColor("#FFB020"),
    "speaking": QColor("#00E5FF"),
}

STATE_SPEEDS = {
    "idle": 1.0,
    "listening": 1.8,
    "thinking": 2.4,
    "speaking": 1.6,
}


class Core(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)

        self.angle1 = 0
        self.angle2 = 0
        self.frame = 0

        self.state = "idle"

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # 60 FPS

    def set_state(self, state):

        if state not in STATE_COLORS:
            state = "idle"

        self.state = state

    def animate(self):

        speed = STATE_SPEEDS.get(self.state, 1.0)

        self.angle1 += 2 * speed
        self.angle2 -= 3 * speed
        self.frame += 0.08 * speed

        self.update()

    def paintEvent(self, event):

        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        cx = self.width() / 2
        cy = self.height() / 2

        color = STATE_COLORS.get(
            self.state,
            STATE_COLORS["idle"]
        )

        pulse = math.sin(self.frame) * 5
        radius = 60 + pulse

        # Brilho
        glow = QColor(color)
        glow.setAlpha(40)

        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(glow)
        p.drawEllipse(
            int(cx-95),
            int(cy-95),
            190,
            190
        )

        # Núcleo
        p.setBrush(color)
        p.drawEllipse(
            int(cx-radius),
            int(cy-radius),
            int(radius*2),
            int(radius*2)
        )

        pen = QPen(color)
        pen.setWidth(4)

        p.setBrush(Qt.BrushStyle.NoBrush)
        p.setPen(pen)

        # Anel 1
        p.drawArc(
            int(cx-90),
            int(cy-90),
            180,
            180,
            int(self.angle1*16),
            120*16
        )

        # Anel 2
        p.drawArc(
            int(cx-115),
            int(cy-115),
            230,
            230,
            int(self.angle2*16),
            100*16
        )

        # Pontos orbitando
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(color)

        for i in range(6):

            ang = math.radians(self.angle1 + i*60)

            x = cx + math.cos(ang) * 115
            y = cy + math.sin(ang) * 115

            p.drawEllipse(
                int(x-4),
                int(y-4),
                8,
                8
            )