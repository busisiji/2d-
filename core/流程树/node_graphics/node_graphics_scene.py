from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import math

from core.流程树.node.node_edge import Edge
from core.流程树.node.node_node import Node
from lib.path import globalsdynamic


class QDMGraphicsScene(QGraphicsScene):
    def __init__(self,scene, parent=None):
        super().__init__(parent)
        """场景ui"""

        self.scene = scene

        # setting
        self.gridSize = 20
        self.gridSquares = 5

        self._color_background = QColor("#393939")
        self._color_light = QColor("#2f2f2f")
        self._color_drak = QColor("#292929")

        self._pen_light = QPen(self._color_light)
        self._pen_light.setWidth(1)
        self._pen_drak = QPen(self._color_drak)
        self._pen_drak.setWidth(2)


        self.setBackgroundBrush(self._color_background)

    def addbtn(self, node):
        """新增按钮"""
        proxy = QGraphicsProxyWidget()
        proxy.setWidget(node.grNode.button)
        proxy.setMaximumWidth(22)
        self.addItem(proxy)
        node.grNode.proxy = proxy
        return proxy

    def initNodetoDb(self):
        """从数据库初始化连接图元"""
        results_node = globalsdynamic.db_child.query_data_table("Node")
        if not results_node:
            self.scene.main.addNode('图像设备', [3], ["输出图像"],[0])
            self.scene.grScene.updateNodePos()
            return
        for result in results_node:
            node = Node(self.scene,result[1],eval(result[2]), texts=eval(result[3]), icons=eval(result[4]))
            self.addbtn(node)
        self.scene.grScene.updateNodePos()

    def initSockettoDb(self):
        """从数据库初始化连接线"""
        results = globalsdynamic.db_child.query_data_table("Edge")

        for edge in self.scene.edges[:]:
            self.scene.removeEdge(edge,delete_db=False)
        for result in results:
            if result[1] and result[2] and result[3] and result[3]:
                start_node_index, end_node_index, start_socket_index, end_socket_index = int(result[1]), int(
                    result[2]), int(result[3]), int(result[4])
                edge = Edge(self.scene, start_node_index=start_node_index, end_node_index=end_node_index,
                            start_socket_index=start_socket_index, end_socket_index=end_socket_index)


    def updateNodePos(self):
        """更新所有图元位置"""
        nodes = self.scene.nodes
        height = 0
        for index in range(len(nodes)):
            node = nodes[index]
            if node.grNode.proxy:
                node.grNode.proxy.setPos(node.content.width() - 22, height)
            node.setPos(0, height)
            height = height + nodes[index].content.height() + nodes[index].grNode.title_height + 20


    def setGrScene(self, width, height):
        # self.setSceneRect(-width // 2, -height // 2, width, height)
        self.setSceneRect(0, 0, width, height)

    # def drawBackground(self, painter, rect):
    #     """绘制方格线"""
    #     super().drawBackground(painter, rect)
    #
    #     left = int(math.floor(rect.left()))
    #     right = int(math.ceil(rect.right()))
    #     top = int(math.floor(rect.top()))
    #     bottom = int(math.ceil(rect.bottom()))
    #
    #     first_left = left - (left % self.gridSize)
    #     first_top = top - (top % self.gridSize)
    #     lines_light, lines_drak = [], []
    #     for x in range(first_left, right, self.gridSize):
    #         if (x % 100 != 0):
    #             lines_light.append(QLine(x, top, x, bottom))
    #         else:
    #             lines_drak.append(QLine(x, top, x, bottom))
    #
    #     for y in range(first_top, bottom, self.gridSize):
    #         if (y % 100 != 0):
    #             lines_light.append(QLine(left, y, right, y))
    #         else:
    #             lines_drak.append(QLine(left, y, right, y))
    #
    #     painter.setPen(self._pen_light)
    #     # painter.drawLine(lines_light)
    #     for i in lines_light:
    #         painter.drawLine(i)
    #     painter.setPen(self._pen_drak)
    #     for i in lines_drak:
    #         painter.drawLine(i)
