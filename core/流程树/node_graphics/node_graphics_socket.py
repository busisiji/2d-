from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class QDMGraphicsSocket(QGraphicsItem):
    def __init__(self, socket,parent=None,socket_type=1):
        """绘制节点"""
        super().__init__(parent)
        self.radius = 6
        self.parent = parent
        self.socket = socket
        self.outline_width = 1.0
        self.socket_type = socket_type
        # self._color_background = QColor("#FFFF7700")
        self.setupUi()

    def setupUi(self):
        # 根据socket_type来决定socket的背景颜色
        self._color = [
            QColor("#FFFF7700"),
            QColor("#FF52e220"),
            QColor("#FF0056a6"),
            QColor("#FFa86db1"),
            QColor("#FFb54747"),
            QColor("#FFdbe220"),
        ]
        self._color_background = self._color[self.socket_type]
        self._color_outline = QColor("#FF000000")

        self._pen = QPen(self._color_outline)
        self._pen.setWidthF(self.outline_width)
        self._brush = QBrush(self._color_background)

        # self.setZValue(100)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        #painting circle
        painter.setBrush(self._brush)
        painter.setPen(self._pen)
        painter.drawEllipse(-self.radius,-self.radius,2*self.radius,2*self.radius)

    def boundingRect(self):
        return QRectF(
            - self.radius - self.outline_width,
            - self.radius - self.outline_width,
            2 * (self.radius - self.outline_width),
            2 * (self.radius - self.outline_width),
        )