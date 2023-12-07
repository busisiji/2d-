from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from core.MyClass import TextLabel
from lib.path import  path_join_path_project


class QMGraphicsNode(QGraphicsItem):
    def __init__(self, node, title='Node Graphics Item', parent=None):
        super().__init__(parent)
        """绘制图元"""

        self._title_color = Qt.white
        self._title_font = QFont("Ubuntu", 10)
        self.node = node
        self.content = self.node.content
        self.proxy = None # 缩放按钮

        # self.edge_size = 10
        self.edge_size = 0
        self.title_height = 24
        self._padding = 6.0
        self._margin = 9.0
        self.width = 180
        self.text_width = 22
        # self.height = 240

        self.initTitle()
        self.title = title

        self._pen_default = QPen(QColor("#7f000000"))
        self._pen_selected = QPen(QColor("#ffffa637"))

        self._brush_title = QBrush(QColor("#ff313131"))
        self._brush_background = QBrush(QColor("#e3212121"))

        # init content
        self.initContent()
        self.initResult()

        self.initUI()

        self.height = self.content.height() + self.title_height

        self.button = QPushButton()
        self.button.setIcon(QIcon(path_join_path_project('icon/返回3.png')))
        self.button_flag = True
        self.button.clicked.connect(self.onButtonClicked)

        # self.setResult('NG')

    def update(self,title):
        self.title = title

    def boundingRect(self):
        return QRectF(
            0,
            0,
            2 * self.edge_size + self.width,
            2 * self.edge_size + self.height
            # 2 * self.edge_size + self.content.height()
        ).normalized()

    def initContent(self):
        """表格大小位置设置"""
        self.grContent = QGraphicsProxyWidget(self)
        # self.content.setGeometry(self.edge_size,self.title_height+self.edge_size,
        #                          self.width - 2*self.edge_size,self.height - 2*self.edge_size - self.title_height)
        self.content.move(self.edge_size,self.title_height+self.edge_size)
        self.content.setFixedWidth(self.width - 2*self.edge_size)
        self.content.adjustSize()

        self.grContent.setWidget(self.content)


    def initUI(self):
        # pass
        self.setFlag(QGraphicsItem.ItemIsSelectable) # 可选
        # self.setFlag(QGraphicsItem.ItemIsMovable) # 可移动

    def initTitle(self):
        self.title_item = QGraphicsTextItem(self)
        self.title_item.setDefaultTextColor(self._title_color)
        self.title_item.setFont(self._title_font)
        self.title_item.setPos(self._padding, 0)
        self.title_item.setTextWidth(
            self.width - 2 * self._padding - 50
        )

    def initResult(self):
        self.result_item = QGraphicsTextItem(self)
        self.result_item.setDefaultTextColor(Qt.red)
        self.result_item.setFont(self._title_font)
        self.result_item.setPos(self._padding+self.title_item.textWidth()-50, 0)
        self.result_item.setTextWidth(80)

    def setResult(self,type,time=0):
        if type == 'OK':
            self.result_item.setDefaultTextColor(Qt.green)
        elif type == 'NG':
            self.result_item.setDefaultTextColor(Qt.red)
        self.result_item.setPlainText(type+f'({time})ms')

    def onButtonClicked(self):
        """缩放按钮"""
        if self.node.scene.main.main.isRun:
            # 流程运行中不能缩放
            return
        if self.button_flag: # 缩
            self.button.setIcon(QIcon(path_join_path_project('icon/返回4.png')))
            self.content.hide()
            self.height = 0
            self.button_flag = False
            # 更新图元和按钮位置
            height = self.node.content.height()
            index_update = self.node.scene.nodes.index(self.node) + 1  # 获取node的索引
            if index_update:
                for node in self.node.scene.nodes:
                    index = self.node.scene.nodes.index(node)  # 获取node的索引
                    if index >= index_update:
                        y = node.grNode.pos().y()
                        node.setPos(0, y - height)
                        node.grNode.proxy.setPos(node.content.width() - 22, y - height)
            # 更新节点位置，节点放在图元标题
            for socket in self.node.sockets:
                if socket:
                    socket.setSocketPosition(-1)
            # 更新线
            for edge in self.node.scene.edges:
                edge.updatePosition()

        else: # 放
            self.button.setIcon(QIcon(path_join_path_project('icon/返回3.png')))
            self.content.show()
            self.button_flag = True
            self.height = self.title_height + self.content.height()
            # 更新图元和按钮位置
            height = self.node.content.height()
            index_update = self.node.scene.nodes.index(self.node) + 1  # 获取node的索引
            if index_update:
                for node in self.node.scene.nodes:
                    index = self.node.scene.nodes.index(node)  # 获取node的索引
                    if index >= index_update:
                        y = node.grNode.pos().y()
                        node.setPos(0, y + height)
                        node.grNode.proxy.setPos(node.content.width() - 22, y + height)
            # 更新节点位置
            for i in range(len(self.node.sockets)):
                socket = self.node.sockets[i]
                if socket:
                    socket.setSocketPosition(i)
            # 更新线
            for edge in self.node.scene.edges:
                edge.updatePosition()

    def contextMenuEvent(self, event):
        '''鼠标右键事件'''
        if self.node.title == '图像设备': # 图像设备不能删除
            return
        for node in self.node.scene.nodes:
                node.grNode.setSelected(False)
        self.setSelected(True)  # 设置选中
        menu = QMenu()
        delete_action = menu.addAction("删除")
        action = menu.exec_(event.screenPos())
        if self.node and action == delete_action:
            self.node.remove()

    def mouseMoveEvent(self, event):
        """鼠标拖动"""
        super().mouseMoveEvent(event)
        self.node.updateConnectedEdges()
    # def mouseMoveEvent(self, event):
    # # """禁止鼠标拖动"""
    #     event.ignore()

    def mouseDoubleClickEvent(self,e):
        super().mouseDoubleClickEvent(e)
        """双击"""
        # self.node.scene.main.ChildVisionCode.showParameterWindow(self.node.title)
        self.node.scene.main._signal_.emit(self.node.title, self.node.get_index())

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.title_item.setPlainText(self._title)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        #outline
        path_outline = QPainterPath()
        path_outline.addRoundedRect(0,0,self.width,self.height,self.edge_size,self.edge_size)
        painter.setPen(self._pen_default if not self.isSelected() else self._pen_selected)
        painter.setBrush(Qt.NoBrush)
        painter.drawPath(path_outline.simplified())
        #title
        path_title = QPainterPath()
        path_title.setFillRule(Qt.WindingFill)
        path_title.addRoundedRect(0,0,self.width,self.title_height,self.edge_size,self.edge_size)
        path_title.addRect(0,self.title_height - self.edge_size,self.edge_size,self.edge_size)
        path_title.addRect(self.width - self.edge_size, self.title_height - self.edge_size, self.edge_size, self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_title)
        painter.drawPath(path_title.simplified())
        #content
        path_content = QPainterPath()
        path_content.setFillRule(Qt.WindingFill)
        path_content.addRoundedRect(0,self.title_height,self.width,self.height - self.title_height,self.edge_size,self.edge_size)
        path_content.addRect(0,self.title_height,self.edge_size,self.edge_size)
        path_content.addRect(self.width - self.edge_size,self.title_height,self.edge_size,self.edge_size)
        painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush_background)
        painter.drawPath(path_content.simplified())

class QDMNodeContentWidget(QWidget):
    def __init__(self,types=[], texts=[],icon=[],parent=None):
        super().__init__(parent)
        """图表"""
        self.texts = texts
        self.tips = texts
        self.types = types
        self.icons = icon
        self.label_names = []
        self.setupUi()
        # self.installEventFilter(self)
        self.setMouseTracking(True)


    def add_row(self,index,type,name,icon):
        """
        图表增加一行

        :param index: 行数
        :param type: 第一列：类型
        :param name: 第二列：名称
        :param icon: 第三列：输入/输出图标
        """
        # index = self.gridLayout.rowCount()
        # 数据类型
        self.label_type = QLabel(self)
        self.label_type.setText(type)
        self.label_type.setFixedHeight(22)  # 设置高度为50像素
        self.label_type.setFixedWidth(38)  # 设置高度为50像素
        self.gridLayout.addWidget(self.label_type, index, 0, 1, 1)
        # 数据名称
        self.label_name = QLabel(self)
        self.label_name.setText(name)
        self.label_name.setFixedHeight(22)  # 设置高度为50像素
        self.gridLayout.addWidget(self.label_name, index, 1, 1, 1)
        self.label_names.append(self.label_name)
        # 图标
        self.label_icon = QLabel(self)
        self.label_icon.setFixedHeight(22)  # 设置高度为50像素
        self.label_icon.setFixedWidth(22)  # 设置高度为50像素
        # 加载图片
        if icon == 1:
            pixmap = QPixmap(path_join_path_project('icon/左箭头1.png'))
        else:
            pixmap = QPixmap(path_join_path_project('icon/右箭头1.png'))
        # 等比例缩放图片
        pixmap = pixmap.scaled(self.label_icon.size(), Qt.AspectRatioMode.KeepAspectRatio)
        # 在QLabel控件中显示图片
        self.label_icon.setPixmap(pixmap)
        self.gridLayout.addWidget(self.label_icon, index, 2, 1, 1)

    def update(self,types=[], texts=[],icon=[]):
        self.texts = texts
        self.types = types
        self.icons = icon
        # 移除所有的子组件
        while self.gridLayout.count():
            item = self.gridLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                if item.layout() is not None:
                    item.layout().deleteLater()
        for index in range(len(self.texts)):
            self.add_row(index,self.types[index],str(self.texts[index]),self.icons[index])

    def setupUi(self):
        self.setObjectName(u"widget")
        # self.setGeometry(QRect(130, 80, 115, 84))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 9, -1)

        for index in range(len(self.texts)):
            self.add_row(index,self.types[index],str(self.texts[index]),self.icons[index])
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.toolButton.setText(QCoreApplication.translate("Frame", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.toolButton_2.setText(QCoreApplication.translate("Frame", u"...", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.toolButton_3.setText(QCoreApplication.translate("Frame", u"...", None))
    # retranslateUi

    def eventFilter(self, obj, event):
        """过滤器"""
        print(event.type(),QEvent.HoverMove,self.label_name.underMouse())
        if obj == self and event.type() == QEvent.HoverMove:
            if self.label_name.underMouse():
                QToolTip.showText(event.globalPos(), "This is a QLabel")
            else:
                QToolTip.hideText()
        return super().eventFilter(obj, event)