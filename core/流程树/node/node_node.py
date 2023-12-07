
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from core.流程树.node.node_socket import Socket
from core.流程树.node_graphics.node_graphics_node import QDMNodeContentWidget, QMGraphicsNode
from lib.path import path_join, Globals, path_join_path_project
from lib.utils import list_de_weight

LEFT_TOP = 1
LEFT_BOTTON = 2
RIGHT_TOP = 3
RIGHT_BOTTON = 4

class Node():
    def __init__(self, scene, title="Undefined Node",types=[],texts=[],icons=[],isNew=True):
        """
        图元

        :param scene: 场景
        :param title: 图元标题
        :param types: 数据类型
        :param texts: 文本内容
        :param icons: 按钮样式
        """
        self.input_num = 0
        self.title = title
        self.socket_spacing = 22
        self.types = types
        self.texts = list_de_weight(texts)
        self.icons = icons
        self.scene = scene

        self.content = QDMNodeContentWidget(self.types,self.texts,self.icons)

        self.grNode = QMGraphicsNode(self, self.title)

        if isNew:
            self.scene.addNode(self)

        self.set_socket()

        # 样式
        self.stylesheet_filename = path_join_path_project('core/流程树/qss/nodestyle.qss')
        self.loadStylesheet(self.stylesheet_filename)

    def set_socket(self):
        # crate socket for inputs and outputs
        self.inputs = []
        self.outputs = []
        self.sockets = [None] * len(self.icons)
        inputs = [i for i, x in enumerate(self.icons) if x == 1]
        outputs = [i for i, x in enumerate(self.icons) if x == 0]

        for item in inputs:
            socket = Socket(node=self, index=item, position=RIGHT_TOP, socket_type=1)
            # socket = Socket(node=self, index=item, position=LEFT_TOP, socket_type=1)
            self.inputs.append(socket)
            self.sockets[item] = socket
            self.input_num = self.input_num + 1

        for item in outputs:
            socket = Socket(node=self, index=item, position=RIGHT_TOP, socket_type=0)
            # socket = Socket(node=self, index=item, position=RIGHT_BOTTON)
            self.outputs.append(socket)
            self.sockets[item] = socket

        # 不分输入输出节点
        self.inputs = self.sockets
        self.outputs = self.sockets
    def updata(self,title="Undefined Node",types=[],texts=[],icons=[]):
        """更新node"""
        self.title = title
        self.socket_spacing = 22
        self.types = types
        self.texts = texts
        self.icons = icons
        self.sockets.clear()
        self.set_socket()
        self.content.update(self.types,self.texts,self.icons)
        self.grNode.update(self.title)

    def get_index(self):
        try:
            nodes = self.scene.nodes
            index = nodes.index(self)  # 获取node的索引
            # self.name = 'node' + str(index)
            return index
        except:
            return None

    def loadStylesheet(self, filename):
        # print('STYLE loading', filename)
        file = QFile(filename)
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll()
        self.content.setStyleSheet(str(stylesheet, encoding='utf-8'))

    def getSocketPosition(self, index, position):
        """edge头和尾的坐标位置"""
        if position in (LEFT_TOP, LEFT_BOTTON):
            x = 0
        else:
            x = self.grNode.width
        if position in (LEFT_BOTTON, RIGHT_BOTTON):
            y = -index * (self.socket_spacing + self.content.gridLayout.verticalSpacing()) + self.grNode.title_height - self.grNode.edge_size - self.socket_spacing
        else:
            y = index * (self.socket_spacing + self.content.gridLayout.verticalSpacing()) + self.grNode.title_height + self.grNode.edge_size + self.socket_spacing
        # return x, y
        return [x, y]

    def updateConnectedEdges(self):
        # 将输入输出的socket全部扫描一遍,并通过hasEdge()方法判断是否更新
        for socket in self.inputs + self.outputs:
            if socket.hasEdge():
                socket.edge.updatePosition()

    @property
    def pos(self):
        """获取位置"""
        return self.grNode.pos()

    def setPos(self, x, y):
        """放置位置"""
        self.grNode.setPos(x, y)

    def hasEdge(self):
        """通过判断这个socket是否有edge来决定是否更新"""
        return self.edge is not None

    def updata_tip(self,tip_texts=None):
        """更新图元提示"""
        texts = []
        if not tip_texts:
            texts = [''] * len(self.content.tips)
        else:
            for output in tip_texts:
                if isinstance(output,float):
                    output = round(output,2)
                texts.append(str(output))
        self.content.tips = texts
        return texts

    def remove(self,isDelDb=True):
        """删除图元"""
        if self.title == '图像设备': # 图像设备不能删除
            return
        self.scene.grScene.removeItem(self.grNode)
        self.scene.removeNode(self,isDelDb)
        self.grNode = None

        if isDelDb:
            self.scene.grScene.updateNodePos()
            self.scene.grScene.initSockettoDb()



