from PyQt5.QtCore import pyqtBoundSignal
from PyQt5.QtWidgets import QMenu, QAction, QSlider, QWidget, QPushButton, QToolButton

from lib.data import convert_JSON
from lib.path import globalsdynamic, Globals
from lib.utils import isSignalConnected


class utilsWindow:

    def get_menu(self,actions,menu_list):
        '''设置下拉菜单'''
        # 创建菜单
        menu = QMenu()
        # 创建子菜单
        # sub_menu = QMenu(menu)
        # sub_menu.setTitle("子菜单")
        # sub_menu.setIcon(QIcon("menu.ico"))

        # 在菜单中添加子菜单
        # menu.addMenu(sub_menu)

        # 创建action并添加到菜单中
        for i in menu_list:
            action = QAction(i, menu)
            menu.addAction(action)
            actions.append(action)
        return menu

    def setSpinbox(self,spinbox,value=0,minimum=0,maximum=100,step=1):
        '''Qspinbox,Qslider样式设置'''
        spinbox.setMinimum(int(minimum))
        spinbox.setMaximum(int(maximum))
        spinbox.setSingleStep(step)
        if value=='auto':
            # 设置特殊值文本为'auto'
            spinbox.setSpecialValueText('auto')
            # 设置默认值为特殊值
            spinbox.setValue(spinbox.minimum())
        else:
            spinbox.setValue(value)
    def setTick(self,slider,direction=QSlider.TicksBelow,step=1):
        '''设置滑块的刻度'''
        slider.setTickPosition(direction)
        slider.setTickInterval(step)
        # slider.valueChanged.connect(self.update)

    def get_input(self,socket_index=0):
        """获取输入参数"""
        # 获取连接线和自定义输出参数
        edge_results = globalsdynamic.db_child.query_data_table("Edge")
        if not edge_results:
            return None
        outputs = globalsdynamic.db_child.query_data_table(Globals.toname['自定义输出'])
        if not outputs :
            return None
        output_index = convert_JSON([output[0]-1 for output in outputs])

        # 设置参数字典 输入图元:输出图元，输入节点，输出节点
        parameters = {}
        for edge_result in edge_results:
            start_node_index, end_node_index, start_socket_index, end_socket_index = edge_result[1:]  # 连接点
            start_node_index, end_node_index, start_socket_index, end_socket_index = int(start_node_index), int(end_node_index), int(start_socket_index), int(end_socket_index)
            # 找到连接网络通讯的自定义输出模块
            if start_node_index in output_index and end_node_index == Globals.node_index-1 and end_socket_index == socket_index:
                parameters[end_node_index, end_socket_index] = start_node_index, start_socket_index

        if not (Globals.node_index-1,socket_index) in parameters:
            return None
        start_node_index, start_socket_index = parameters[(Globals.node_index-1,socket_index)]

        output = globalsdynamic.db_child.query_colum(Globals.toname['自定义输出'], int(start_node_index)+1,'id')
        if not output or not output[0][2]:
            return None
        text = convert_JSON(output[0][2])
        return text[start_socket_index]

    def close_signal(self):
        """断开打开的信号"""
        for signal in self.signal:
            if isinstance(signal,pyqtBoundSignal):
                try:
                    signal.disconnect()
                except:
                    pass
            elif isinstance(signal,QPushButton) or isinstance(signal,QToolButton):
                if isSignalConnected(signal):
                    signal.clicked.disconnect()  # 断开新建模块的clicked信号
            # else:
            #     signal.disconnect()

    def signalSlotConnection(self):
        self.close_signal()

    def window_close(self):
        '''关闭窗口'''
        # 重复打开窗口有删除之前的信号
        # for signal in self.signal:
        #     if isinstance(signal,QPushButton) or isinstance(signal,QToolButton):
        #         # if isSignalConnected(signal.clicked()):
        #         signal.clicked.disconnect()  # 断开新建模块的clicked信号，不断开重新打开会重复触发
        #     else:
        #         signal.disconnect()
        self.ChildVision.stackedWidget.close()
        # self.ChildVision.stackedWidget.hide()
        self.ChildVision.widget_11.show()