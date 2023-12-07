from core.流程树.node_graphics.node_graphics_edge import QDMGraphicsEdgeDirect, QDMGraphicsEdgeBezier

EDGE_TYPE_DIRECT = 1
EDGE_TYPE_BEZIER = 2

class Edge():
    def __init__(self, scene, start_node_index=None,end_node_index=None,start_socket_index=None,end_socket_index=None,type=1):
        """获取socket的相对node的位置"""
        self.start_node_index  = start_node_index
        self.end_node_index    = end_node_index
        self.start_socket_index = start_socket_index
        self.end_socket_index  = end_socket_index
        self.scene = scene

        if type == EDGE_TYPE_DIRECT:
            self.grEdge = QDMGraphicsEdgeDirect(self)
        else:
            self.grEdge = QDMGraphicsEdgeBezier(self)

        self.store()
        self.scene.grScene.addItem(self.grEdge)

        self.updateSkcket()
        self.updatePosition()

    def store(self):
        """增加线"""
        self.scene.addEdge(self)

    def updateSkcket(self):
        """更新线头和线尾"""
        nodes = self.scene.nodes
        if self.start_node_index != None and self.start_node_index < len(nodes):
            self.start_node = nodes[self.start_node_index]
            self.start_socket = self.start_node.outputs[self.start_socket_index]
        else:
            self.start_node = None
            self.start_socket = None
        if self.end_node_index != None and self.end_node_index < len(nodes):
            self.end_node = nodes[self.end_node_index]
            self.end_socket = self.end_node.inputs[self.end_socket_index]
        else:
            self.end_node = None
            self.end_socket = None

    def updatePosition(self):
        """更新线头和线尾位置"""

        if self.start_socket is not None:
            source_pos = self.start_socket.getSocketPosition()
            source_pos[0] += self.start_socket.node.grNode.pos().x()
            source_pos[1] += self.start_socket.node.grNode.pos().y()
            self.grEdge.setSource(*source_pos)
            if self.end_socket is not None:
                end_pos = self.end_socket.getSocketPosition()
                end_pos[0] += self.end_socket.node.grNode.pos().x()
                end_pos[1] += self.end_socket.node.grNode.pos().y()
                self.grEdge.setDestination(*end_pos)
            else:
                self.grEdge.setDestination(*source_pos)
            self.grEdge.update()

            self.start_socket.edge = self
        if self.end_socket is not None:
            self.end_socket.edge = self

    def remove_from_socket(self):
        """管理删除"""
        if self.start_socket is not None:
            self.start_socket.edge = None
        if self.end_socket is not None:
            self.end_socket.edge = None
        self.end_socket = None
        self.start_socket = None
    def remove(self):
        """删除连接线"""
        self.remove_from_socket()
        # self.scene.grScene.removeItem(self.grEdge)
        self.scene.removeEdge(self)
        self.grEdge = None



