from core.流程树.node_graphics.node_graphics_socket import QDMGraphicsSocket

LEFT_TOP = 1
LEFT_BOTTON = 2
RIGHT_TOP = 3
RIGHT_BOTTON = 4

class Socket():
    def __init__(self, node, index=0,position=LEFT_TOP,socket_type=1):
        """节点后端"""
        # 根据传入的节点和index在对应scene和对应position上进行通过QDMGraphicsSocket(self.node.grNode)进行绘制，通过self.grSocket.setPos(*self.node.getSocketPosition(index, position))进行放置
        # 其中position表示绘制在节点的什么位置
        self.node = node
        self.index = index
        # self.position = LEFT_TOP
        self.position = position
        self.edge = None # 确定该socket是否进行连接
        self.socket_type = socket_type

        self.grSocket = QDMGraphicsSocket(self,self.node.grNode,self.socket_type)

        self.grSocket.setPos(*self.node.getSocketPosition(index, position))

    def getSocketPosition(self):
        """获取socket的相对node的位置"""
        return self.node.getSocketPosition(self.index,self.position)

    def setConnectedEdge(self, edge=None):
        """设置连接线"""
        self.edge = edge

    def setSocketPosition(self,index):
        self.index = index
        self.grSocket.setPos(*self.node.getSocketPosition(self.index, self.position))

    def hasEdge(self):
        return self.edge is not None


