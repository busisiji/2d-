# !/usr/bin/env python
# -*- encoding: utf-8 -*-

from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QSize, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QPushButton, QToolButton

from core.OperateDb import OperateDb
from core.init_window import *
from core.runFlow import RunFlow
from core.图像设备.ImageCaptureWindow import ImageCaptureWindow
from core.坐标标定.CameraCalibrationDb import CCOperateDb, CCNameDb
from core.坐标标定.CameraCalibrationWindow import CameraCalibrationWindow
from core.数据合并.PooleOperateDb import PooleOperateDb
from core.数据合并.PooleWindow import PooleWindow
from core.数据转换.QsciOperateDb import QsciOperateDb
from core.数据转换.QsciScintillaWindow import QsciScintillaWindow
from core.模板匹配.STMOperateDb import STMOperateDb
from core.模板匹配.ShapTemplateMatchingWindow import ShapTemplateMatchingWindow
from core.流程树.main import NodeEditWind
from core.网络通讯.ModbusOperateDb import ModbusOperateDb, ModbusNameDb
from core.网络通讯.ModbusWindow import ModbusWindow
from core.自定义输出.OutputOperateDb import OutputOperateDb
from core.自定义输出.OutputWindow import OutputWindow
from core.颜色识别.CROperateDb import CROperateDb
from core.颜色识别.ColorRecognitionWindow import ColorRecognitionWindow
from lib.file import clear_folder_if_exceeded_numbe, clear_folder


class Visionwindow(QMainWindow):
    _signal_close = pyqtSignal()

    def __init__(self,MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision

        self.isRun = False # 是否允許中

        # 流程树嵌入
        self.ChildVision.nodeEditWind = NodeEditWind(self)
        self.ChildVision.gridLayout_25.addWidget(self.ChildVision.nodeEditWind)

        self.ChildVision.runFlow = RunFlow(self.MainWindow)

        self.init()

        self.signalSlotConnection()

    def init(self):
        """初始化"""
        init_imageCapture(self.ChildVision)
        self.ChildVision.stackedWidget.hide()
        self.ChildVision.label_42.set_ui(12)
        self.ChildVision.stackedWidget_3.setCurrentIndex(0)
        self.ChildVision.stackedWidget_4.setCurrentIndex(0)

        self.keys = ['name', 'temppath', 'parameters','mask','camera']
        globalsdynamic.db_main.create_tables('ImageCapture', self.keys) # 创建图像设备表
        self.keys = ['name','curPlaySizeW', 'curPlaySizeH']
        globalsdynamic.db_child.create_tables('View', self.keys)  # 创建视图参数

        # 初始化模块
        resluts = globalsdynamic.db_child.query_data_table('Node')
        if not resluts:
            return
        self.ChildVision.Childs = []
        for i in range(len(resluts)):
            reslut = resluts[i]
            column = reslut[1]
            Globals.node_index = reslut[0]
            self.add_Childs(column)


    def add_Childs(self,column):
        """模块增加"""
        if column == '坐标标定':
            self.ChildVision.ChildCC = CameraCalibrationWindow(self.MainWindow)
            self.ChildVision.ChildCC.title = '坐标标定'
            self.ChildVision.Childs.append(self.ChildVision.ChildCC)

        elif column == '图像设备':
            self.ChildVision.ChildIC = ImageCaptureWindow(self.MainWindow)
            self.ChildVision.ChildIC.setcss()
            self.ChildVision.ChildIC.title = '图像设备'
            self.ChildVision.Childs.append(self.ChildVision.ChildIC)

        elif column == '模板匹配':
            self.ChildVision.ChildSTM = ShapTemplateMatchingWindow(self.MainWindow)
            self.ChildVision.ChildSTM.setcss()
            self.ChildVision.ChildSTM.title = '模板匹配'
            self.ChildVision.Childs.append(self.ChildVision.ChildSTM)

        elif column == '颜色识别':
            self.ChildVision.ChildCR = ColorRecognitionWindow(self.MainWindow)
            self.ChildVision.ChildCR.setcss()
            self.ChildVision.ChildCR.title = '颜色识别'
            self.ChildVision.Childs.append(self.ChildVision.ChildCR)

        elif column == '数据转换':
            self.ChildVision.ChildQSCI = QsciScintillaWindow(self.MainWindow)
            self.ChildVision.ChildQSCI.title = '数据转换'
            self.ChildVision.Childs.append(self.ChildVision.ChildQSCI)

            # self.ChildVision.ChildQSCI.signalSlotConnection() # 信号断开

        elif column == '网络通讯':
            self.ChildVision.ChildModbus = ModbusWindow(self.MainWindow)
            self.ChildVision.ChildModbus.setcss()
            self.ChildVision.ChildModbus.title = '网络通讯'
            self.ChildVision.Childs.append(self.ChildVision.ChildModbus)
            init_Modbus(self.ChildVision.ChildModbus)

        elif column == '数据合并':
            self.ChildVision.ChildPoole = PooleWindow(self.MainWindow)
            # self.ChildVision.ChildModbus.setcss()
            self.ChildVision.ChildPoole.title = '数据合并'
            self.ChildVision.Childs.append(self.ChildVision.ChildPoole)
            init_Poole(self.ChildVision.ChildPoole)

        elif column == '自定义输出':
            self.ChildVision.ChildOutput = OutputWindow(self.MainWindow)
            # self.ChildVision.ChildModbus.setcss()
            self.ChildVision.ChildOutput.title = '自定义输出'
            self.ChildVision.Childs.append(self.ChildVision.ChildOutput)
            init_Output(self.ChildVision.ChildOutput)

    def signalSlotConnection(self):
        # self.ChildVision.treeWidget.itemClicked.connect(self.handleItemClicked) # 单击
        self.ChildVision.treeWidget.itemDoubleClicked.connect(self.handleItemClicked) # 双击
        self.ChildVision.stackedWidget.currentChanged.connect(self.changedParameterWindow)
        self.ChildVision.View._signal_Press_pos.connect(self.show_pos)

        # self.ChildVision.pushButton_12.click.connect(self.continuous)
        # self.ChildVision.pushButton_14.click.connect(self.start)
        self.ChildVision.nodeEditWind._signal_.connect(self.showParameterWindow)
        self.ChildVision.toolButton_14.clicked.connect(self.click_event)


    def click_event(self):
        # self.ChildVision.runFlow.start()
        if not self.isRun:
            self.set_run()
            self.ChildVision.runFlow.run()
        else:
            self.ChildVision.runFlow.stop()
            self.set_stop()

    def set_run(self):
        """开始运行"""
        self.ChildVision.ChildIC.set_stop() # 关闭预览

        self.isRun = True
        icon = QIcon()
        icon.addFile(u":/over/icon/over.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ChildVision.toolButton_14.setIcon(icon)
        self.ChildVision.action_2.setIcon(icon)
        self.ChildVision.toolButton_14.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.ChildVision.toolButton_14.setStyleSheet(
            "background-color: rgb(255,165,0);\n"f"border-radius: 10px; border:\n"" 3px groove gray;border-style: outset;")

    def set_stop(self):
        """停止运行"""
        icon = QIcon()
        icon.addFile(u":/run/icon/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ChildVision.toolButton_14.setIcon(icon)
        self.ChildVision.action_2.setIcon(icon)
        self.ChildVision.toolButton_14.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.ChildVision.toolButton_14.setStyleSheet(
            "background-color: rgb(58, 111, 50);\n"f"border-radius: 10px; border:\n"" 3px groove gray;border-style: outset;")
        self.isRun = False

    def addNode(self):
        """模块增加"""
        if self.isRun:
            return

        self.ChildVision.stackedWidget.hide()
        node_index = len(self.ChildVision.nodeEditWind.scene.nodes) + 1

        if self.column == '模板匹配':
            self.ChildVision.nodeEditWind.addNode('模板匹配', [3,2,0,0,0,0,0,1,1,1,0,1,3],
                                                  ["输入图像", "输出检出中心","输出检出中心X", "输出检出中心Y","输出检出角度","输出检出数量","输出检出模板数","输出检出模板名","输出识别模板名","输出学习模板名","输出得分","输出结果","输出图像"],
                                                  [1,0,0, 0, 0,0, 0,0, 0,0,0,0, 0])
            STMOperateDb.insert_data(node_index) # 创建数据库
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        elif self.column == '颜色识别':
            self.ChildVision.nodeEditWind.addNode('颜色识别',[3,0,1,3],["输入图像","输出数量","输出颜色","输出图像"], [1, 0, 0,0])
            CROperateDb.insert_data(node_index)
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        elif self.column == '坐标标定':
            self.ChildVision.nodeEditWind.addNode('坐标标定',[2,2],["输入相机坐标","输出世界坐标"], [1, 0])
            CCOperateDb.insert_data()
            CCNameDb.insert_data(node_index)
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        elif self.column == '数据转换':
            # self.ChildVision.nodeEditWind.addNode('数据转换',[0,0],["输入数值","输出数值"], [1, 0])
            self.ChildVision.nodeEditWind.addNode('数据转换')
            QsciOperateDb.insert_data(node_index)
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        elif self.column == '网络通讯':
            self.ChildVision.nodeEditWind.addNode('网络通讯',[0],["输入数值"], [1])
            ModbusOperateDb.insert_data()
            ModbusNameDb.insert_data(node_index)
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        elif self.column == '数据合并':
            self.ChildVision.nodeEditWind.addNode('数据合并',[0,0,0],["输入数值","输入数值","输出数值"], [1,1,0])
            PooleOperateDb.insert_data(node_index)
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        elif self.column == '自定义输出':
            self.ChildVision.nodeEditWind.addNode('自定义输出')
            OutputOperateDb.insert_data(node_index)
            QMessageBox.information(self.MainWindow, "提示", "创建模块成功！")

        self.ChildVision.widget_11.show()

    def changedParameterWindow(self):
        """参数窗口改变事件"""
        self.ChildVision.View.clear()

    def showParameterWindow(self,column,index):
        """显示参数窗口"""
        if index == None or self.isRun:
            return
        Globals.node_index = index + 1
        self.ChildVision.widget_11.hide()
        if column == '坐标标定':
            init_CameraCalibration(self.ChildVision.Childs[index])
            self.set_currentIndex(0)

        elif column == '图像设备':
            # init_imageCapture(self.ChildVision)
            self.set_currentIndex(2)

        elif column == '模板匹配':
            init_ShapTemplateMatching(self.ChildVision.Childs[index])
            self.set_currentIndex(4)

        elif column == '颜色识别':
            init_ColorRecognition(self.ChildVision.Childs[index])
            self.set_currentIndex(1)

        elif column == '数据转换':
            init_QsciScintilla(self.ChildVision.Childs[index])
            self.set_currentIndex(3)

        elif column == '网络通讯':
            init_Modbus(self.ChildVision.Childs[index])
            self.set_currentIndex(5)

        elif column == '数据合并':
            init_Poole(self.ChildVision.Childs[index])
            self.set_currentIndex(7)

        elif column == '自定义输出':
            init_Output(self.ChildVision.Childs[index])
            self.set_currentIndex(6)

        self.ChildVision.stackedWidget.show()

    def set_currentIndex(self,index):
        """设置显示的参数窗口"""
        self.ChildVision.stackedWidget.setCurrentIndex(index)

    def handleItemClicked(self, item, column):
        '''视觉应用树响应事件'''
        self.column = item.text(column)
        # QTimer.singleShot(100, self.addNode)
        self.addNode()
        Globals.node_index = Globals.node_index + 1
        self.add_Childs(self.column)

    def show_pos(self,x,y):
        '''显示鼠标坐标'''
        text = str(x)+','+str(y)
        self.ChildVision.label_20.setText(text)

    def start(self):
        """启动"""

    def continuous(self,time=1000):
        """连续启动"""

    def close(self):
        # 图像设备关闭
        self.ChildVision.ChildIC.window_close()
        # 相机关闭
        self.ChildVision.ChildIC.camera_close()


        # # 保存掩码
        # self.ChildVision.ChildSTM.save_mask()

