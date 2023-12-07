import math

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QDMGraphicsEdge(QGraphicsPathItem):
    def __init__(self, edge, parent=None):
        """父类方便接下来建立直线和曲线两个类"""
        super().__init__(parent)

        self.edge = edge
        self.arrow = 1
        self.painterPath = QPainterPath()
        self.arrowHead = QPolygonF()

        self._color = QColor("#001000")
        self._color_selected = QColor("#00ff00")
        self._pen = QPen(self._color)
        self._pen_selected = QPen(self._color_selected)
        self._pen.setWidth(2.0)
        self._pen_selected.setWidth(3.0)

        self.setFlag(self.ItemIsSelectable, True)  # 允许内部线条接收点击事件

        # self.setZValue(-1)

        self.posSource = [0, 0]
        self.posDestination = [200, 100]


        self.setupUi()

    def setupUi(self):
        pass
        # self.setFlag(QGraphicsItem.ItemHasNoContents)

    def boundingRect(self):
        """边界"""
        # # return self.shape().boundingRect()
        self.updatePath()
        path = self.path()  # 获取路径
        path.translate(5, 0)  # 将路径向右缩减5个单位
        rect = path.boundingRect()  # 获取更新后的边界矩形
        # print('rect',rect)
        return rect
    # def shape(self):
    #     self.painterPath.addPolygon(self.arrowHead)
    #     return self.painterPath

    def paint(self, painter, QStyleOptionGraphicsItem, widge=None):
        # self.updatePath()

        painter.setPen(self._pen if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(self.path())

        # 绘制多边形箭头
        polygon = QPolygon()
        polygon.append(QPoint(self.posDestination[0], self.posDestination[1]))  # 顶点1
        polygon.append(QPoint(self.posDestination[0] + 12*self.arrow, self.posDestination[1] + 5))  # 顶点2
        polygon.append(QPoint(self.posDestination[0] + 12*self.arrow, self.posDestination[1] - 5))  # 顶点3
        # 设置画圆点的画笔
        self._mark_pen = QPen(Qt.green)
        self._mark_pen.setWidthF(2.0)
        self._mark_brush = QBrush()
        self._mark_brush.setColor(Qt.green)
        self._mark_brush.setStyle(Qt.SolidPattern)
        painter.setPen(self._mark_pen)
        painter.setBrush(self._mark_brush)
        painter.drawPolygon(polygon)
        # # 计算箭头的多边形
        # self.arrowHead = QPolygonF()
        # line = QLineF(self.posSource[0], self.posSource[1], self.posDestination[0], self.posDestination[1])
        # angle = math.acos(line.dx() / line.length())
        # if line.dy() >= 0:
        #     angle = math.pi * 2 - angle
        # arrowP1 = QPointF(self.posDestination[0] + 12 * self.arrow * math.cos(angle - math.pi / 3),
        #                   self.posDestination[1] + 12 * self.arrow * math.sin(angle - math.pi / 3))
        # arrowP2 = QPointF(self.posDestination[0] + 12 * self.arrow * math.cos(angle + math.pi / 3),
        #                   self.posDestination[1] + 12 * self.arrow * math.sin(angle + math.pi / 3))
        # self.arrowHead.clear()
        # self.arrowHead << QPointF(self.posDestination[0], self.posDestination[1]) << arrowP1 << arrowP2

    def updatePath(self):
        # 画一条A指向B的线
        raise NotImplemented("This method has to be overriden in a child class")

    def setSource(self, x, y):
        """更新头"""
        self.posSource = [x, y]

    def setDestination(self,x ,y):
        """更新尾"""
        self.posDestination = [x,y]

    def contextMenuEvent(self, event):
        '''鼠标右键事件'''
        for edge in self.edge.scene.edges :
            if edge.grEdge:
                edge.grEdge.setSelected(False)
        self.setSelected(True) # 设置选中
        menu = QMenu()
        delete_action = menu.addAction("删除")
        action = menu.exec_(event.screenPos())
        if self.edge and action == delete_action:
            self.edge.remove()

class QDMGraphicsEdgeDirect(QDMGraphicsEdge):
    """直线类"""
    def updatePath(self):
        self.painterPath = QPainterPath(QPointF(self.posSource[0], self.posSource[1]))
        patch = (self.posDestination[1] - self.posSource[1]) / 2
        patchx = self.posDestination[0] - self.posSource[0]
        self.setZValue(-patch - patchx)
        if patch > 150:
            patch = 150
        if patch < 20:
            patch = 20
        if patchx < patch:
            self.arrow = 1
        else:
            self.arrow = -1
        # print(self.posSource[0] + patch,self.posSource[1],self.posDestination[0],self.posDestination[1])
        self.painterPath.lineTo(self.posSource[0] + patch, self.posSource[1])
        self.painterPath.lineTo(self.posSource[0] + patch, self.posDestination[1])
        self.painterPath.lineTo(self.posDestination[0], self.posDestination[1])
        self.setPath(self.painterPath)

class QDMGraphicsEdgeBezier(QDMGraphicsEdge):
    """曲线类"""
    def updatePath(self):
        s = self.posSource
        d = self.posDestination
        dist = (d[0] - s[0]) * 0.5
        if s[0] > d[0]: dist *= -1

        self.painterPath = QPainterPath(QPointF(self.posSource[0], self.posSource[1]))
        self.painterPath.cubicTo(s[0] + dist, s[1], d[0] - dist, d[1],
                     self.posDestination[0], self.posDestination[1])
        self.setPath(self.painterPath)
