from PySide6.QtWidgets import QGraphicsView
from PySide6.QtGui import QPainter


class GraphicsView(QGraphicsView):

    def __init__(self, scene):
        super().__init__(scene)

        self.setRenderHint(QPainter.RenderHint.Antialiasing)

        self.setFrameShape(QGraphicsView.Shape.NoFrame)

        self.setHorizontalScrollBarPolicy(False)

        self.setVerticalScrollBarPolicy(False)