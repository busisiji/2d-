import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from func_timeout import func_set_timeout

from core.utils_window import utilsWindow
from core.数据合并.PooleOperateDb import PooleOperateDb
from core.流程树.node.node_node import Node
from lib.path import globalsdynamic, Globals


class PooleWindow(utilsWindow):
    '''数据合并界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision

        self.signalSlotConnection()

    def signalSlotConnection(self):
        self.signal = [self.ChildVision.pushButton_40,
                       ]
        super().signalSlotConnection()

        self.ChildVision.pushButton_40.clicked.connect(self.window_close)

    @func_set_timeout(Globals.timeout)  # 设定函数超执行时间_
    def run(self, module_input):
        output = ''
        first = True
        for i in range(len(module_input)):
            input = module_input[i]
            if input:
                if not first and i < len(module_input)-1:
                    output = output + '|'
                output = output + input
                first = False
        return module_input+[output],[]

    def updata_node_data(self):
        """参数表格更新数据"""
        self.node_data = {
            'id' : Globals.node_index,
            'title' : '数据合并',
            'types':[],
            'texts':[],
            'icons':[]
        }
        type = self.ChildVision.comboBox_31.currentText()
        for i in range(self.ChildVision.spinBox_16.value()):
            self.node_data['types'].append(type)
            self.node_data['texts'].append('输入'+type)
            self.node_data['icons'].append(1)
        self.node_data['types'].append(type)
        self.node_data['texts'].append('输出' + type)
        self.node_data['icons'].append(0)

        # 获取新图元
        tree = self.ChildVision.nodeEditWind
        new_node = Node(tree.scene,self.node_data['title'], self.node_data['types'], self.node_data['texts'], self.node_data['icons'], isNew=False)

        # 更新流程树
        tree.scene.updataNode(Globals.node_index-1,new_node)
        # 流程树数据库保存
        globalsdynamic.db_child.insert_data('Node', self.node_data,'id')

    def save_data(self):
        """保存数据库"""
        data = {
            'type': self.ChildVision.comboBox_31.currentText(),
            'num':  self.ChildVision.spinBox_16.value()
        }
        PooleOperateDb.add_data(data)

    def window_close(self):
        self.updata_node_data()
        self.save_data()
        super().window_close()