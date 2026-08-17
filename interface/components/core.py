from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QColor, QPen
from PySide6.QtCore import Qt, QTimer
import math


class Core(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 400)

        self.angle1 = 0
        self.angle2 = 0
        self.frame = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)  # 60 FPS

    def animate(self):
        self.angle1 += 2
        self.angle2 -= 3
        self.frame += 0.08

        self.update()

    def paintEvent(self, event):

        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)

        cx = self.width() / 2
        cy = self.height() / 2

        pulse = math.sin(self.frame) * 5
        radius = 60 + pulse

        # Brilho
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor(0, 229, 255, 40))
        p.drawEllipse(
            int(cx-95),
            int(cy-95),
            190,
            190
        )

        # Núcleo
        p.setBrush(QColor("#00E5FF"))
        p.drawEllipse(
            int(cx-radius),
            int(cy-radius),
            int(radius*2),
            int(radius*2)
        )

        pen = QPen(QColor("#00E5FF"))
        pen.setWidth(4)

        p.setBrush(Qt.BrushStyle.NoBrush)
        p.setPen(pen)

        # Anel 1
        p.drawArc(
            int(cx-90),
            int(cy-90),
            180,
            180,
            self.angle1*16,
            120*16
        )

        # Anel 2
        p.drawArc(
            int(cx-115),
            int(cy-115),
            230,
            230,
            self.angle2*16,
            100*16
        )

        # Pontos orbitando
        p.setPen(Qt.PenStyle.NoPen)
        p.setBrush(QColor("#00E5FF"))

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