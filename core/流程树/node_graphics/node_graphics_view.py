import inspect

from PyQt5.QtWidgets import QGraphicsView, QGraphicsItem, QGraphicsScene, QSizePolicy, QMenu, QToolTip, \
    QGraphicsProxyWidget, QApplication, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from core.流程树.node.node_edge import Edge
from core.流程树.node_graphics.node_graphics_socket import QDMGraphicsSocket
from lib.path import globalsdynamic


class QDMGraphicsView(QGraphicsView):
    def __init__(self,grScene,parent=None):
        super().__init__(parent)
        self.grScene = grScene
        self.edge_enable = False  # 用来记录目前是否可以画线条
        self.drag_edge = None  # 记录拖拽时的线

        self.setScene(self.grScene)
        self.initUI()

        self.zoomInFactor = 1.25
        self.zoom = 5
        self.zoomStep = 1
        self.zoomClamp = False
        self.zoomRange = [0,10]

    def initUI(self):
        # 设置渲染属性
        self.setRenderHints(QPainter.Antialiasing |  # 抗锯齿
                            QPainter.HighQualityAntialiasing |  # 高品质抗锯齿
                            QPainter.TextAntialiasing |  # 文字抗锯齿
                            QPainter.SmoothPixmapTransform |  # 使图元变换更加平滑
                            QPainter.LosslessImageRendering)  # 不失真的图片渲染
        # 视窗更新模式
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)
        # 设置水平和竖直方向的滚动条不显示
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # self.setTransformationAnchor(self.AnchorUnderMouse) # 鼠标滚轮缩放界面
        # 设置拖拽模式
        self.setDragMode(self.RubberBandDrag)
        # self.setDragMode(self.NoDrag) #禁止
        # 禁用图形项的索引
        self.grScene.setItemIndexMethod(QGraphicsScene.NoIndex)
        # # 视图调整为适应场景的大小
        # self.fitInView(self.grScene.sceneRect(), Qt.IgnoreAspectRatio)
        self.centerOn(0, 0)  # 将视图中心设置为场景的左上角
        self.setMouseTracking(True) # 开启鼠标跟踪

    def get_item_at_click(self, event):
        """ 获取点击位置的item，无则返回None. """
        pos = event.pos()
        item = self.itemAt(pos)
        return item

    # def contextMenuEvent(self, event):
    #     '''鼠标右键事件'''
    #     menu = QMenu()
    #     delete_action = menu.addAction("删除")
    #     action = menu.exec_(event.globalPos())
    #     item = self.get_treeitem_at_click(event)
    #     if item and action == delete_action:
    #         if self.scene() is not None:
    #             item.prepareGeometryChange()
    #             self.scene().removeItem(item)  # 从场景中删除项 没有设置scene.setItemIndexMethod(QGraphicsScene.NoIndex)会闪退

    def mousePressEvent(self, event):
        """拖拽连线"""
        if self.grScene.scene.main.main.isRun:
            # 流程运行中不能拖拽
            return
        super().mousePressEvent(event)
        item = self.get_item_at_click(event)
        if event.button() == Qt.LeftButton:
            if isinstance(item, QDMGraphicsSocket):
                # 确认起点是图元后，开始拖拽
                self.edge_drag_start(item)

    def mouseMoveEvent(self, event):
        # 实时更新线条
        pos = event.pos()
        sc_pos = self.mapToScene(pos) # view坐标转scene坐标，view坐标滑动后不增加滑动区域

        if self.edge_enable and self.drag_edge is not None and self.drag_edge.grEdge:
            self.drag_edge.grEdge.setDestination(sc_pos.x(), sc_pos.y())
            self.drag_edge.grEdge.update()
        try:
            # 设置提示
            item = self.itemAt(pos)
            if item:
                # print("Mouse is over item:", item,event.globalPos())
                # # 更新提示
                # 使用inspect模块的signature函数来获取函数的参数信息
                if not isinstance(item,QGraphicsProxyWidget) :
                    return
                if not isinstance(item.widget(),QWidget):
                    return
                for i in range(len(item.widget().label_names)):
                    # 获取QLabel位置
                    label = item.widget().label_names[i]
                    w = label.geometry().width() - 20
                    h = label.geometry().height() - 10
                    x = label.geometry().x() + item.parentItem().pos().x() + item.widget().pos().x()
                    y = label.geometry().y() + item.parentItem().pos().y() + item.widget().pos().y()
                    # 判断鼠标是否在QLabel上方
                    if x <= sc_pos.x() <= w+x and y <= sc_pos.y() <= h+y:
                        QToolTip.hideText()
                        QToolTip.showText(event.globalPos(),item.widget().tips[i])
                        break
            # else:
            #     print("Mouse is not over any item")
        except Exception as e:
            pass


    def mouseReleaseEvent(self, event):
        if self.edge_enable:
            # 拖拽结束后，关闭此功能
            self.edge_enable = False
            item = self.get_item_at_click(event)
            if self.drag_edge:
                self.remove_drag_edge(self.drag_edge)
            # 终点图元不能是起点图元，即无环图
            if isinstance(item, QDMGraphicsSocket) and item is not self.drag_start_item:
                self.edge_drag_end(item)
        else:
            super().mouseReleaseEvent(event)
    #
    def edge_drag_start(self, item):
        """连接线头"""
        self.drag_start_index = self.grScene.scene.nodes.index(item.socket.node)
        self.drag_start_item = item  # 拖拽开始时的图元，此属性可以不在__init__中声明
        if self.drag_start_item.socket.socket_type == 0:
            self.edge_enable = True
            self.drag_edge = Edge(self.grScene.scene, start_node_index=self.drag_start_index, end_node_index=None,start_socket_index=self.drag_start_item.socket.index, end_socket_index=None)
    #

    def edge_drag_end(self, item):
        """连接线尾"""
        self.drag_end_index = self.grScene.scene.nodes.index(item.socket.node)
        self.drag_end_item = item
        if self.drag_end_item.socket.socket_type == 1 and self.drag_end_index > self.drag_start_index :
            # 不同类型的线不增加
            if self.drag_end_item.socket.node.types[int(self.drag_end_item.socket.index)] != self.drag_start_item.socket.node.types[
                int(self.drag_start_item.socket.index)]:
                return

            # 重复线不增加
            self.edgedata = {}
            self.edgedata['start_node_index'] = str(self.drag_start_index)
            self.edgedata['end_node_index'] = str(self.drag_end_index)
            self.edgedata['start_socket_index'] = str(self.drag_start_item.socket.index)
            self.edgedata['end_socket_index'] = str(self.drag_end_item.socket.index)
            results = globalsdynamic.db_child.query_data_table('Edge')
            for result in results:
                if tuple(self.edgedata.values()) == result[1:]:
                    return

            # 只能上连下，出连入
            new_edge = Edge(self.grScene.scene, start_node_index=self.drag_start_index, end_node_index=self.drag_end_index,start_socket_index=self.drag_start_item.socket.index, end_socket_index=self.drag_end_item.socket.index) # 拖拽结束
            # new_edge.store() # 保存最终产生的连接线
            self.grScene.scene.addEdgeDb(new_edge)
    #
    def remove_drag_edge(self,drag_edge):
        drag_edge.remove() # 删除拖拽时画的线
        drag_edge = None
    #
    # def resizeEvent(self, event):
    #     super().resizeEvent(event)
    #     # 获取QGraphicsView的新大小
    #     new_size = event.size()
    #     if self.grScene is not None:
    #         # 设置QGraphicsScene的大小与QGraphicsView的大小一致
    #         self.grScene.setSceneRect(0, 0, new_size.width(), new_size.height())

    # def mousePressEvent(self, event):
    #     """鼠标键按下时调用"""
    #     if event.button() == Qt.MidButton:
    #         self.middleMouseButtonPress(event)
    #     elif event.button() == Qt.LeftButton:
    #         self.leftMouseButtonPress(event)
    #     elif event.button() == Qt.RightButton:
    #         self.rightMouseButtonPress(event)
    #     else:
    #         super().mousePressEvent(event)
    # def mouseReleaseEvent(self, event):
    #     """鼠标键松开时调用"""
    #     if event.button() == Qt.MiddleButton:
    #         self.middleMouseButtonRelease(event)
    #     elif event.button() == Qt.LeftButton:
    #         self.leftMouseButtonRelease(event)
    #     elif event.button() == Qt.RightButton:
    #         self.rightMouseButtonRelease(event)
    #     else:
    #         super().mouseReleaseEvent(event)

    # def middleMouseButtonPress(self, event):
    #
    #     #当鼠标中键按下时，将产生一个假的鼠标按键松开的事件
    #     releaseEvent = QMouseEvent(QEvent.MouseButtonRelease,event.localPos(),event.screenPos(),
    #                                Qt.LeftButton,Qt.NoButton,event.modifiers())
    #     super().mouseReleaseEvent(releaseEvent)
    #
    #     #变为抓取手势
    #     self.setDragMode(QGraphicsView.ScrollHandDrag)
    #
    #     #产生一个鼠标按下左键的假事件
    #     fakeEvent = QMouseEvent(event.type(),event.localPos(),event.screenPos(),
    #                             Qt.LeftButton,event.buttons() | Qt.LeftButton,event.modifiers())
    #     super().mousePressEvent(fakeEvent)

    def middleMouseButtonRelease(self, event):
        fakeEvent = QMouseEvent(event.type(),event.localPos(),event.screenPos(),
                                Qt.LeftButton,event.buttons() | Qt.LeftButton,event.modifiers())
        super().mouseReleaseEvent(fakeEvent)
        self.setDragMode(QGraphicsView.NoDrag)

    def leftMouseButtonPress(self,event):
        return super().mousePressEvent(event)

    def leftMouseButtonRelease(self,event):
        return super().mouseReleaseEvent(event)

    def rightMouseButtonPress(self,event):
        return super().mousePressEvent(event)

    def rightMouseButtonRelease(self,event):
        return super().mouseReleaseEvent(event)


    # def wheelEvent(self, event):
    #     #计算缩放系数
    #     zoomOutFactor = 1/self.zoomInFactor
    #
    #     #计算缩放
    #     if event.angleDelta().y()>0:
    #         zoomFactor = self.zoomInFactor
    #         self.zoom += self.zoomStep
    #     else:
    #         zoomFactor = zoomOutFactor
    #         self.zoom -= self.zoomStep
    #
    #     clamped = False
    #     if self.zoom < self.zoomRange[0]:
    #         self.zoom,clamped = self.zoomRange[0],True
    #     if self.zoom > self.zoomRange[1]:
    #         self.zoom, clamped = self.zoomRange[1], True
    #
    #     #设置场景比例
    #     if not clamped or self.zoomClamp:
    #         self.scale(zoomFactor,zoomFactor)





