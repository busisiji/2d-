from PyQt5.QtCore import pyqtSignal

from core.流程树.node.node_edge import Edge
from core.流程树.node.node_node import Node
from core.流程树.node_graphics.node_graphics_scene import QDMGraphicsScene
from lib.path import globalsdynamic, Globals


class Scene:
    def __init__(self,parent=None):
        """场景后端"""
        self.main = parent
        self.nodes = [] # 图表数
        self.edges = [] # 线数


        self.scene_width, self.scene_height = 400, 64000
        self.initUI()

    def initUI(self):
        self.grScene = QDMGraphicsScene(self)
        self.grScene.setGrScene(self.scene_width,self.scene_height)


    def addNode(self,node):
        self.nodes.append(node)
        self.grScene.addItem(node.grNode)

    def addNodeDb(self,node,id):
        """图元数据库增加"""
        self.nodedata['id'] = id
        self.nodedata['title'] = node.title
        self.nodedata['types'] = node.types
        self.nodedata['texts'] = node.content.texts
        self.nodedata['icons'] = node.content.icons
        globalsdynamic.db_child.insert_data('Node', self.nodedata,'id')

    def addEdge(self,edge):
        self.edges.append(edge)
        self.grScene.addItem(edge.grEdge)

    def addEdgeDb(self,edge,isDuplicateChecking=True):
        """连接线数据库增加"""
        # self.edgedata['name'] = str(i)
        self.edgedata['start_node_index'] =     str(edge.start_node_index     )
        self.edgedata['end_node_index'] =       str(edge.end_node_index       )
        self.edgedata['start_socket_index'] =   str(edge.start_socket_index   )
        self.edgedata['end_socket_index'] =     str(edge.end_socket_index     )
        # 重复线不增加
        if isDuplicateChecking:
            results = globalsdynamic.db_child.query_data_table('Edge')
            for result in results:
                if tuple(self.edgedata.values()) == result[1:]:
                    return
        globalsdynamic.db_child.insert_data('Edge', self.edgedata)

    def updataNode(self,index,new_node):
        """更新图元"""
        if index >= len(self.nodes):
            return
        old_node = self.nodes[index]
        if old_node == new_node:
            return
        old_edges = self.removeEdgeofNode(index)  # 删除图元相关连接线

        # 更新图元
        # self.grScene.removeItem(old_node.grNode)
        old_node.remove(isDelDb=False)
        self.nodes.insert(Globals.node_index - 1,new_node)
        self.grScene.addItem(new_node.grNode)
        self.grScene.addbtn(new_node)
        self.grScene.updateNodePos()

        # 更新连接线
        for old_edge in old_edges:
            if old_edge.start_node_index == index :
                start_node_index = index
                try:
                    start_socket_index = new_node.texts.index(old_node.texts[old_edge.start_socket_index])
                except:
                    continue
                end_node_index = old_edge.end_node_index
                end_socket_index = old_edge.end_socket_index
            elif old_edge.end_node_index == index:
                end_node_index = index
                try:
                    end_socket_index = new_node.texts.index(old_node.texts[old_edge.end_socket_index])
                except:
                    continue
                start_node_index = old_edge.start_node_index
                start_socket_index = old_edge.start_socket_index
            new_edge = Edge(self, start_node_index,
                            end_node_index, start_socket_index,
                            end_socket_index)  # 拖拽结束
            self.addEdgeDb(new_edge, isDuplicateChecking=False)
        self.grScene.initSockettoDb()


    def removeEdgeofNode(self,index):
        """删除图元相关连接线"""
        edge_remove = []
        for edge in self.edges:
            if edge.start_node_index == index or edge.end_node_index == index:
                edge_remove.append(edge)
        for edge in edge_remove:
            self.removeEdge(edge)
        return edge_remove

    def removeNode(self,node,isDelDb=True):
        """删除图元"""
        index = self.nodes.index(node) # 获取node的索引
        self.nodes.remove(node)
        # # # 删除图元时，遍历与其连接的线，并移除
        self.removeEdgeofNode(index)
        # 删除按钮
        self.grScene.removeItem(node.grNode)
        self.grScene.removeItem(node.grNode.proxy)

        # 更新数据库
        results = globalsdynamic.db_child.query_data_table("Node")
        if not results:
            return False
        node_id = results[index][0]
        title = results[index][1]

        if isDelDb:
            self.delete_correlation_db(node_id,title) # 删除子表
            globalsdynamic.db_child.delete_row('Node', 'id', node_id)  # 删除行


            for i in range(index,len(results)):
                old_node_id = i+1
                new_node_id = i
                globalsdynamic.db_child.update_data('Node', 'id', old_node_id, new_node_id)
                globalsdynamic.db_child.update_data('Edge', 'start_node_index', i, i - 1)
                globalsdynamic.db_child.update_data('Edge', 'end_node_index', i, i - 1)

        del node

    def removeEdge(self,edge,delete_db=True):
        """删除连接线"""
        self.edges.remove(edge)
        self.grScene.removeItem(edge.grEdge)

        if delete_db:
            # 更新数据库
            globalsdynamic.db_child.execute_sql(f'DELETE FROM Edge WHERE start_node_index = "{edge.start_node_index}" AND'
                                               f' end_node_index = "{edge.end_node_index}" AND '
                                               f'start_socket_index = "{edge.start_socket_index}" AND '
                                               f'end_socket_index = "{edge.end_socket_index}"')

        # del edge

    def create_db(self):
        """数据库创建"""
        self.nodekeys = Globals.nodekeys # 图元名 图元标题 是输入节点还是输出节点  连接的图元输入节点 连接的图元输出节点
        self.nodedata = {}
        self.edgekeys = ['start_node_index','end_node_index','start_socket_index','end_socket_index']  # 线名   连接的图元输入节点 连接的图元输出节点
        self.edgedata = {'start_node_index':"",'end_node_index':"",'start_socket_index':"",'end_socket_index':""}
        # globalsdynamic.db_child.create_tables('Node', self.nodekeys)
        globalsdynamic.db_child.create_table_primary('Node', self.nodekeys)
        globalsdynamic.db_child.create_table_majorkey('Edge', 'id', self.edgekeys)

    def updata_Treedb(self,data):
        """更新流程树数据库"""
        new_node = Node(self, data["title"], data['types'], data['texts'],
                        data['icons'], isNew=False)
        # 更新流程树
        self.updataNode(Globals.node_index - 1, new_node)
        # 流程树数据库保存
        globalsdynamic.db_child.insert_data('Node', data, 'id')

    def updata_delete_correlation_db(self,node_id,table_name):
        """更新主表后子表同步更新"""
        results = globalsdynamic.db_child.query_data_table(table_name)
        if not results:
            return
        names = [int(result[0]) for result in results]
        for name in names:
            if name > node_id:
                globalsdynamic.db_child.update_data(table_name, 'id', name, name - 1)

    def delete_correlation_db(self,node_id,title):
        """删除主表后子表同步更新"""
        if title in Globals.toname:
            globalsdynamic.db_child.delete_row(Globals.toname[title], 'id', node_id) # 删除行
        # for table_name in list(Globals.toname.values())[:-1]:
        for table_name in [element for element in list(Globals.toname.values()) ]:
            self.updata_delete_correlation_db(node_id,table_name)
