import struct
import sys

import serial
import serial.tools.list_ports
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from func_timeout import func_set_timeout

from core.PopUpWindow import QsciParameterDialog, ModbusParameterDialog
from core.utils_window import utilsWindow
from core.流程树.node.node_node import Node
from core.网络通讯.ModbusOperateDb import ModbusOperateDb, ModbusNameDb
from core.网络通讯.ModbusCommunication import connect_tcp, Plc, connect_rtu
from lib.data import convert_JSON
from lib.path import Globals, globalsdynamic
from core.MyClass import MyTableWidget

class ModbusWindow(utilsWindow):
    '''网络通讯界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision

        self.Com_Dict = {}
        self.isolated = True  # 是否单独运行

        self.signalSlotConnection()
    def setcss(self):
        self.comboboxs = [self.ChildVision.comboBox_43,
                     self.ChildVision.comboBox_20, self.ChildVision.comboBox_21, self.ChildVision.spinBox_14,self.ChildVision.comboBox_33,self.ChildVision.spinBox_17,self.ChildVision.spinBox_18,
                     self.ChildVision.lineEdit_4, self.ChildVision.lineEdit_5,self.ChildVision.comboBox_22,self.ChildVision.comboBox_23,self.ChildVision.comboBox_24,self.ChildVision.comboBox_25,self.ChildVision.comboBox_26,
                     self.ChildVision.comboBox_39,self.ChildVision.spinBox_20,self.ChildVision.comboBox_41, self.ChildVision.comboBox_40,
                     self.ChildVision.comboBox_27, self.ChildVision.comboBox_29]
        # for box in self.comboboxs:
        #     if isinstance(box,QComboBox) :
        #         box.setCurrentIndex(0)
        self.ChildVision.lineEdit_4.setText('192.168.1.1')
        self.ChildVision.lineEdit_5.setText('502')
        self.ChildVision.comboBox_23.setCurrentText('9600')
        self.ChildVision.comboBox_24.setCurrentText('8')
        self.ChildVision.comboBox_22.setEditable(True)
        self.ChildVision.comboBox_40.setToolTip('多数值的分隔符为|\n范围为-32768,32767')
        # self.ChildVision.comboBox_40.setEditable(True)

        self.setSpinbox(self.ChildVision.spinBox_14, 100, 1, 3000, 10)  # 置信度
        self.setSpinbox(self.ChildVision.spinBox_17, 1, 1, 1000, 1)  # 置信度
        self.setSpinbox(self.ChildVision.spinBox_18, 0, 0, 10000000, 1)  # 置信度


        self.ChildVision.stackedWidget_8.hide()
        self.ChildVision.groupBox_29.hide() # 不转换数据类型
        self.port_check()
        # self.changedComboBox33()

    def signalSlotConnection(self):
        self.signal = [self.ChildVision.comboBox_27.currentIndexChanged,self.ChildVision.comboBox_20.currentIndexChanged,self.ChildVision.comboBox_22.currentIndexChanged,
                       self.ChildVision.comboBox_33.currentIndexChanged,self.ChildVision.comboBox_43.currentIndexChanged,
                       self.ChildVision.pushButton_20,self.ChildVision.pushButton_21,self.ChildVision.pushButton_49,self.ChildVision.pushButton_50]
        super().signalSlotConnection()

        self.ChildVision.comboBox_27.currentIndexChanged.connect(self.changedComboBox27)
        self.ChildVision.comboBox_20.currentIndexChanged.connect(self.changedComboBox20)
        self.ChildVision.comboBox_22.currentIndexChanged.connect(self.changedComboBox22)
        self.ChildVision.comboBox_33.currentIndexChanged.connect(self.changedComboBox33)
        self.ChildVision.comboBox_43.currentIndexChanged.connect(self.updataTODb)
        self.ChildVision.comboBox_40.currentIndexChanged.connect(self.changedComboBox40)

        self.ChildVision.pushButton_20.clicked.connect(self.communication)
        self.ChildVision.pushButton_21.clicked.connect(self.delete_data)
        self.ChildVision.pushButton_49.clicked.connect(self.save_data)
        self.ChildVision.pushButton_50.clicked.connect(self.window_close)

    @func_set_timeout(Globals.timeout)  # 设定函数超执行时间_
    def run(self,module_input):
        result = self.communication(module_input[-1])
        return [result],[]

    def init_changedComboBox(self):
        self.changedComboBox27()
        self.changedComboBox20()
        # self.changedComboBox33()
        self.changedComboBox40()

    def changedComboBox27(self):
        text = self.ChildVision.comboBox_27.currentIndex()
        if text < 4:
            self.ChildVision.stackedWidget_7.setCurrentIndex(0)
        else:
            self.ChildVision.stackedWidget_7.setCurrentIndex(1)
    def changedComboBox20(self):
        """接口"""
        text = self.ChildVision.comboBox_20.currentIndex()
        if text == 0:
            self.ChildVision.stackedWidget_6.setCurrentIndex(0)
        elif text == 1:
            self.ChildVision.stackedWidget_6.setCurrentIndex(1)
    def changedComboBox22(self):
        """串口端口提示"""
        text = self.ChildVision.comboBox_22.currentText()
        self.ChildVision.comboBox_22.setToolTip(self.Com_Dict[text]) if self.Com_Dict and text else ''
    def changedComboBox33(self):
        """读写操作"""
        text = self.ChildVision.comboBox_33.currentIndex()
        if text == 0:
            self.ChildVision.stackedWidget_9.setCurrentIndex(0)
            # # 流程树更改
            # self.save_data = {
            #     "title": "网络通讯",
            #     'types' : [Globals.types[0]],
            #     'texts' : ['输入数值'],
            #     'icons' : [1]
            # }
            # self.ChildVision.nodeEditWind.scene.updata_Treedb(self.save_data)
        elif text == 1:
            self.ChildVision.stackedWidget_9.setCurrentIndex(1)
            # # 流程树更改
            # self.save_data = {
            #     "title": "网络通讯",
            #     'types': [Globals.types[0]],
            #     'texts': ['输出数值'],
            #     'icons': [0]
            # }
            # self.ChildVision.nodeEditWind.scene.updata_Treedb(self.save_data)


    def changedComboBox40(self):
        """传递目标"""
        text = self.ChildVision.comboBox_40.currentIndex()
        if text == 0:
            self.ChildVision.comboBox_40.setEditable(False)
        else:
            self.ChildVision.comboBox_40.setEditable(True)
            # 自定义值增加限制器
            intValidator = QIntValidator()
            regex = QRegExp("[0-9\-|]*")
            regexValidator = QRegExpValidator(regex)
            self.ChildVision.comboBox_40.setValidator(regexValidator)

    def port_check(self):
        """串口检测"""
        # 检测所有存在的串口，将信息存储在字典中
        self.Com_Dict = {}
        self.port_list = list(serial.tools.list_ports.comports())

        self.ChildVision.comboBox_22.clear()
        for port in self.port_list:
            self.Com_Dict["%s" % port[0]] = "%s" % port[1]

        for com in self.Com_Dict:
            self.ChildVision.comboBox_22.addItem(com)

        # 无串口判断
        if len(self.Com_Dict) == 0:
            self.ChildVision.comboBox_22.addItem("无串口")
        #     self.ChildVision.comboBox_22.setEditable(True)
        # else:
        #     self.ChildVision.comboBox_22.setEditable(False)

    def updata_output_changeds(self,columns):
        """输出参数选项为输入参数"""
        self.ChildVision.comboBox_30.clear()
        for column in columns:
            self.ChildVision.comboBox_30.addItem(column)

    def updata_name_changeds(self,isReturnOld = False,isUdata = True):
        """更新名称列表"""
        name = self.ChildVision.comboBox_43.currentText()
        names = ModbusOperateDb.get_names()
        self.ChildVision.comboBox_43.clear()
        self.ChildVision.comboBox_43.addItems(names)
        if name and isReturnOld:
            self.ChildVision.comboBox_43.setCurrentText(name)
        if isUdata:
            self.updataTODb()

    def updataTODb(self):
        """导入数据库数据"""
        result = ModbusOperateDb.get_row(self.ChildVision.comboBox_43.currentText())
        # 初始化参数
        for i in range(len(self.comboboxs)):
            box = self.comboboxs[i]
            if not result or not result[i]:
                continue
            if isinstance(box, QComboBox):
                # comboBox_40不能直接setCurrentText，否则一定为输入参数
                if i == 17 and str(result[i]) != '输入参数':
                    self.ChildVision.comboBox_40.setCurrentIndex(1)
                    self.ChildVision.comboBox_40.setCurrentText(str(result[i]))
                else:
                    box.setCurrentText(str(result[i]))
            elif isinstance(box, QLineEdit):
                box.setText(result[i])
            elif isinstance(box, QSpinBox):
                box.setValue(int(result[i]))
        self.init_changedComboBox()

    def updata_node(self):
        """更新图元参数"""
        # 获取新图元
        tree = self.ChildVision.nodeEditWind
        if self.ChildVision.comboBox_33.currentIndex() == 0:
            new_node = Node(tree.scene, '网络通讯', ['数值'], ["输出数值"],
                            [0], isNew=False)
        else:
            new_node = Node(tree.scene, '网络通讯', ['数值'], ["输入数值"],
                            [1], isNew=False)

        # 更新流程树
        tree.scene.updataNode(Globals.node_index - 1, new_node)
        # 流程树数据库保存
        globalsdynamic.db_child.insert_data('Node', self.save_data, 'id')

    def save_data(self):
        """保存数据"""
        if not self.ChildVision.comboBox_43.currentText():
            QMessageBox.information(self.MainWindow, "错误", f"Modbus名称不能为空！")
            return
        try:
            texts = []
            for combobox in self.comboboxs:
                if isinstance(combobox, QComboBox):
                    texts.append(combobox.currentText())
                elif isinstance(combobox, QLineEdit) or isinstance(combobox, QSpinBox):
                    texts.append(combobox.text())
            data = dict(zip(ModbusOperateDb.keys[:len(texts)], texts))
            # data['name'] = self.ChildVision.comboBox_43.currentText()
            ModbusOperateDb.add_data(data)
            self.updata_name_changeds(isReturnOld=True)
        except Exception as e:
            QMessageBox.warning(self.MainWindow, "错误", f"保存通讯参数失败：{e}！")
        # else:
        #     QMessageBox.warning(self.MainWindow, "提示", f"保存通讯参数成功！")

    def delete_data(self):
        """删除数据"""
        ModbusOperateDb.delete_row(self.ChildVision.comboBox_43.currentText())
        self.updata_name_changeds()

    def communication(self,text=None):
        """通讯测试"""
        # 网口通讯
        if self.ChildVision.comboBox_20.currentText() == '网口':
            try:
                self.master = connect_tcp(self.ChildVision.lineEdit_4.text(), int(self.ChildVision.lineEdit_5.text()), float(self.ChildVision.spinBox_14.text()) / 100)
            except Exception as e:
                if self.isolated:
                    QMessageBox.information(self.MainWindow, "错误", f"网口打开失败：{e}")
                else:
                    raise  # 重新引发异常
                return
        elif self.ChildVision.comboBox_20.currentText() == '串口':
            try:
                self.master = connect_rtu(self.ChildVision.comboBox_22.currentText(),int(self.ChildVision.comboBox_23.currentText()),int(self.ChildVision.comboBox_24.currentText()),
                                           self.ChildVision.comboBox_26.currentText(),int(self.ChildVision.comboBox_25.currentText()),timeout=float(self.ChildVision.spinBox_14.text()) / 100)
            except Exception as e:
                if self.isolated:
                    QMessageBox.information(self.MainWindow, "错误", f"串口打开失败：{e}")
                else:
                    raise  # 重新引发异常
                return
        self.modbus_plc = Plc(self.master)  # 建立一个plc对象
        return self.communication_plc(text)

    def turn_type(self,data):
        data = int(data)
        if -32768 < data or data > 32767:
            data = 0
        return data
    #     """数据类型转换"""
    #     if self.ChildVision.comboBox_27.currentText() == 'Siged(正整数）':
    #         return int(data)
    #     elif self.ChildVision.comboBox_27.currentText() == 'Unsiged(负整数)':
    #         return int.from_bytes((int(data)).to_bytes(1, 'little', signed=True), 'little', signed=False)
    #     elif self.ChildVision.comboBox_27.currentText() == 'Float(单精度数)':
    #     elif self.ChildVision.comboBox_27.currentText() == 'Float Inverse(负单精度数)':
    #     elif self.ChildVision.comboBox_27.currentText() == 'Double(双精度数)':
    #     elif self.ChildVision.comboBox_27.currentText() == 'Double Inverse(负双精度数)':
    #     return int(data)

    def communication_plc_read(self):
        """通讯测试 读"""
        funName = self.ChildVision.comboBox_39.currentText()
        result = self.modbus_plc.fun[funName](
            int(self.ChildVision.spinBox_17.text()), int(self.ChildVision.spinBox_18.text()),
            int(self.ChildVision.spinBox_20.text()))
        result = [x - 65536 if x > 32767 else x for x in result]
        if self.isolated:
            QMessageBox.information(self.MainWindow, "提示", f"通讯成功,获取值：{result}")

    def communication_plc_write(self,texts):
        """写"""
        funName = self.ChildVision.comboBox_41.currentText()
        # 获取自定义值
        if self.ChildVision.comboBox_40.currentIndex() == 1:
            texts = self.ChildVision.comboBox_40.currentText()
            try:
                texts = str(texts).split('|')
                # 写入值格式修正
                if funName == 'Wirte(05) 单线圈' or funName == 'Wirte(06) 单寄存器':
                    text = self.turn_type(texts[0])
                elif funName == 'Wirte(15) 多线圈' or funName == 'Wirte(16) 多寄存器':
                    text = [self.turn_type(text) for text in texts]

            except:
                QMessageBox.information(self.MainWindow, "错误", f"通讯失败,请输入正确的自定义值")
                return
        # 获取输入参数
        else:
            try:
                if self.isolated:
                    texts = self.get_input()
                texts = str(texts).split('|')
                if funName == 'Wirte(05) 单线圈' or funName == 'Wirte(06) 单寄存器':
                    text = int(texts[0])
                elif funName == 'Wirte(15) 多线圈' or funName == 'Wirte(16) 多寄存器':
                    text = [int(text) for text in texts]
            except Exception as e:
                QMessageBox.information(self.MainWindow, "错误", f"通讯失败,连接正确的参数值")
                return
        self.modbus_plc.fun[funName](int(self.ChildVision.spinBox_17.text()),
                                              int(self.ChildVision.spinBox_18.text()), text)
        if self.isolated:
            QMessageBox.information(self.MainWindow, "提示", f"通讯成功,写入值：{text}")
        return text

    def communication_plc(self,texts=None):
        """通讯测试"""
        try:
            # 如果点击了确定按钮，则将参数设置为编辑框中的内容
            if self.ChildVision.comboBox_33.currentText() == '读':
                return self.communication_plc_read()
            else:
                return self.communication_plc_write(texts)
        except Exception as e:
            QMessageBox.information(self.MainWindow, "错误", f"通讯失败：{e}")
        finally:
            if self.master:
                self.master.close()

    def save_name(self):
        """保存当前表名"""
        ModbusNameDb.add_data({'name':self.ChildVision.comboBox_43.currentText()})

    def window_close(self):
        self.save_data()
        self.updata_node()
        self.save_name()
        super().window_close()
