from PySide6.QtWidgets import QGraphicsScene


class GraphicsEngine(QGraphicsScene):

    def __init__(self):
        super().__init__()

        self.setSceneRect(0, 0, 800, 800)

        print("[Graphics Engine] Online.")