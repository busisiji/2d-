import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from core.流程树.node.node_edge import Edge
from core.流程树.node.node_node import Node
from core.流程树.node.node_scene import Scene
from core.流程树.node_graphics.node_graphics_view import QDMGraphicsView
from lib.path import globalsdynamic, Globals


class NodeEditWind(QMainWindow):
    _signal_ = pyqtSignal(str,int)
    def __init__(self,parent=None):
        super(NodeEditWind,self).__init__()
        self.main = parent
        self.scene = Scene(self)
        self.grScene = self.scene.grScene
        self.scene.create_db()
        # create graphics scene

        # self.addDebugNode()
        self.initNode()
        # create graphics view
        self.view = QDMGraphicsView(self.grScene,self)
        # self.Layout_node.addWidget(self.view)
        self.setCentralWidget(self.view)

    def addDebugContent(self):
        """添加一些乱七八糟的东西"""
        greenBrush = QBrush(Qt.green)
        outlinePen = QPen(Qt.black)
        outlinePen.setWidth(2)

        rect = self.grScene.addRect(-100,-100, 80 ,100 ,outlinePen,greenBrush)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        text = self.grScene.addText("不错！！！！",QFont("Ubuntu"))
        text.setFlag(QGraphicsItem.ItemIsSelectable)
        text.setFlag(QGraphicsItem.ItemIsMovable)
        text.setDefaultTextColor(QColor.fromRgbF(1.0,1.0,1.0))

        widget1 = QPushButton("Hello world")
        proxy1 = self.grScene.addWidget(widget1)
        proxy1.setFlag(QGraphicsItem.ItemIsMovable)
        proxy1.setPos(0,30)

        widget2 = QTextEdit()
        proxy2 = self.grScene.addWidget(widget2)
        proxy2.setFlag(QGraphicsItem.ItemIsSelectable)
        proxy2.setPos(0,60)

        line =self.grScene.addLine(-200,-200,400,-100,outlinePen)
        line.setFlag(QGraphicsItem.ItemIsSelectable)
        line.setFlag(QGraphicsItem.ItemIsMovable)

    def addDebugNode(self):
        globalsdynamic.db_child.clear('Node')
        globalsdynamic.db_child.clear('Edge')
        node1 = Node(self.scene, "这是一个节点", texts=['这是一个节点这是一个节点这是一个节点这是一个节点这是一个节点这是一个节点',1,2,4,5,54,4,12], icons=[1,0,1,1,1,0,0,0])
        node2 = Node(self.scene, "这是第二个节点", texts=[0,2,3,1,4,254,4,2,4], icons=[1,1,0,1,0,1,0,1,0])
        node3 = Node(self.scene, "这是第三个节点", texts=[0,1], icons=[1,1])
        proxy = self.scene.grScene.addbtn(node1)
        proxy = self.scene.grScene.addbtn(node2)
        proxy = self.scene.grScene.addbtn(node3)

        self.scene.grScene.updateNodePos()
        node1.setPos(0,0)
        node2.setPos(0,  node1.grNode.title_height + node1.content.height() + 20)
        node3.setPos(0,  node1.grNode.title_height + node1.content.height() + node2.grNode.title_height + node2.content.height() + 20*2)

        edge1 = Edge(self.scene, start_node_index=0,end_node_index=1,start_socket_index=0,end_socket_index=0)
        edge2 = Edge(self.scene, start_node_index=1,end_node_index=2,start_socket_index=0,end_socket_index=0,type=1)
        edge3 = Edge(self.scene, start_node_index=0, end_node_index=2, start_socket_index=0, end_socket_index=0, type=1)
        self.scene.update_db()

    def initNode(self):
        """读取数据库初始化node"""
        self.scene.grScene.initNodetoDb()
        self.scene.grScene.initSockettoDb()


    def addNode(self,title,type_indexs=[],texts=[],icons=[]):
        """
        新增node

        :param title:  标题
        :param type_indexs: 类型
        :param texts: 名称
        :param icons: 参数类型
        :return:
        """
        height = 0
        types = [Globals.types[index] for index in type_indexs] if type_indexs else []
        node_num = len(self.scene.nodes)
        node = Node(self.scene, title,types,texts,icons)
        proxy = self.scene.grScene.addbtn(node)
        nodes = self.scene.nodes
        for index in range(node_num):
            height = height + nodes[index].content.height() + nodes[index].grNode.title_height + 20
        node.setPos(0, height)
        proxy.setPos(node.content.width() - 22, height)
        # 数据库
        self.scene.addNodeDb(node,node_num+1)



if __name__=="__main__":
    app=QApplication(sys.argv)
    mywin=NodeEditWind()
    mywin.show()
    sys.exit(app.exec_())

