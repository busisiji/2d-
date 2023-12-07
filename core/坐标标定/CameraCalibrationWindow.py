# !/usr/bin/env python
# -*- encoding: utf-8 -*-
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QMessageBox
from func_timeout import func_set_timeout

from core.utils_window import utilsWindow
from core.坐标标定.CameraCalibration import getTransformationMatrix, findRound, ImagetoWorld
from core.坐标标定.CameraCalibrationDb import CCOperateDb, CCNameDb
from lib.file import write_json
from lib.path import globalsdynamic, Globals
from lib.utils import parameter_str_to_list, parameter_list_to_str


class CameraCalibrationWindow(utilsWindow):
    '''相机标定界面'''
    def __init__(self,MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision
        self.calibration_point_names = ['第一点','第二点','第三点','第四点','第五点','第六点','第七点','第八点','第九点'] # 标定点列表
        self.index = int(self.ChildVision.comboBox_16.currentIndex())  # 标定方式索引
        self.ponit_number = int(self.ChildVision.comboBox_15.currentIndex())
        self.keys = ['name','comboBoxIndex','text','matrix']
        self.data={
        'name': '第一点',
        'text': '["","","","","","","","","","","","","","","",""]',
        'comboBoxIndex': 0,  # 标定方式索引
        'matrix': "[0.0,0.0,0.0,0.0,0.0,0.0]"  # 转换矩阵
    }
        self.matrix = self.data['matrix'] # 转换矩阵
        # 显示图像x坐标的label
        self.Coordinate_imagex_list = [[self.ChildVision.lineEdit_4_1_1,self.ChildVision.lineEdit_4_2_1,
                                        self.ChildVision.lineEdit_4_3_1,self.ChildVision.lineEdit_4_4_1],
                                       [self.ChildVision.lineEdit_9_1_1,self.ChildVision.lineEdit_9_2_1,self.ChildVision.lineEdit_9_3_1,
                                        self.ChildVision.lineEdit_9_4_1,self.ChildVision.lineEdit_9_5_1,self.ChildVision.lineEdit_9_6_1,
                                        self.ChildVision.lineEdit_9_7_1,self.ChildVision.lineEdit_9_8_1,self.ChildVision.lineEdit_9_9_1]]
        # 显示图像y坐标
        self.Coordinate_imagey_list = [[self.ChildVision.lineEdit_4_1_2, self.ChildVision.lineEdit_4_2_2,
                                        self.ChildVision.lineEdit_4_3_2, self.ChildVision.lineEdit_4_4_2],
                                       [self.ChildVision.lineEdit_9_1_2, self.ChildVision.lineEdit_9_2_2,self.ChildVision.lineEdit_9_3_2,
                                        self.ChildVision.lineEdit_9_4_2, self.ChildVision.lineEdit_9_5_2,self.ChildVision.lineEdit_9_6_2,
                                        self.ChildVision.lineEdit_9_7_2, self.ChildVision.lineEdit_9_8_2,self.ChildVision.lineEdit_9_9_2]]
        # 显示世界x坐标
        self.Coordinate_worldx_list = [[self.ChildVision.lineEdit_4_1_3, self.ChildVision.lineEdit_4_2_3,
                                        self.ChildVision.lineEdit_4_3_3, self.ChildVision.lineEdit_4_4_3],
                                       [self.ChildVision.lineEdit_9_1_3, self.ChildVision.lineEdit_9_2_3,
                                        self.ChildVision.lineEdit_9_3_3,
                                        self.ChildVision.lineEdit_9_4_3, self.ChildVision.lineEdit_9_5_3,
                                        self.ChildVision.lineEdit_9_6_3,
                                        self.ChildVision.lineEdit_9_7_3, self.ChildVision.lineEdit_9_8_3,
                                        self.ChildVision.lineEdit_9_9_3]]
        # 显示世界y坐标
        self.Coordinate_worldy_list = [[self.ChildVision.lineEdit_4_1_4, self.ChildVision.lineEdit_4_2_4,
                                        self.ChildVision.lineEdit_4_3_4, self.ChildVision.lineEdit_4_4_4],
                                       [self.ChildVision.lineEdit_9_1_4, self.ChildVision.lineEdit_9_2_4,
                                        self.ChildVision.lineEdit_9_3_4,
                                        self.ChildVision.lineEdit_9_4_4, self.ChildVision.lineEdit_9_5_4,
                                        self.ChildVision.lineEdit_9_6_4,
                                        self.ChildVision.lineEdit_9_7_4, self.ChildVision.lineEdit_9_8_4,
                                        self.ChildVision.lineEdit_9_9_4]]

        self.setcss()

        # 显示转换矩阵的label
        self.matrix_list = [self.ChildVision.label_25,self.ChildVision.label_26,self.ChildVision.label_27,self.ChildVision.label_28,self.ChildVision.label_23,self.ChildVision.label_24]

        self.signalSlotConnection()

    def setcss(self):
        self.ChildVision.actions, self.ChildVision.actions_4 = [], []
        # self.ChildVision.pushButton_9.setMenu(self.get_menu(self.ChildVision.actions,
        #                                         ["标定一", "标定二", "标定三", "标定四", "标定五", "标定六", "标定七",
        #                                          "标定八", "标定九"]))
        # self.ChildVision.pushButton_4.setMenu(self.get_menu(self.ChildVision.actions_4,
        #                                         ["标定一", "标定二", "标定三", "标定四", "标定五", "标定六", "标定七",
        #                                          "标定八", "标定九"]))

    def signalSlotConnection(self):
        self.signal = [self.ChildVision.pushButton_13,self.ChildVision.pushButton_9,self.ChildVision.comboBox_45.currentIndexChanged,
                       self.ChildVision.comboBox_16.currentIndexChanged,self.ChildVision.pushButton,
                       self.ChildVision.pushButton_33,self.ChildVision.pushButton_37,
                       self.ChildVision.View._signal_Point,self.ChildVision.pushButton_2.clicked]
        super().signalSlotConnection()

        self.ChildVision.pushButton_13.clicked.connect(self.delete_data)
        self.ChildVision.pushButton_9.clicked.connect(self.save_data)
        self.ChildVision.comboBox_45.currentIndexChanged.connect(self.updataTODb)

        self.ChildVision.comboBox_16.currentIndexChanged.connect(self.changedComboBox)
        self.ChildVision.pushButton.clicked.connect(self.CoordinateCalibration)
        self.ChildVision.pushButton_33.clicked.connect(self.getCoordinate)
        self.ChildVision.pushButton_37.clicked.connect(self.findPoint)
        self.ChildVision.View._signal_Point.connect(self.getCoordinatePoint)
        self.ChildVision.pushButton_2.clicked.connect(self.window_close)

        # # 不能用循环，否则lambda函数会固定传最后一个参数
        # actions = self.ChildVision.actions
        # actions[0].triggered.connect(lambda : self.save_data(actions[0].text()))
        # actions[1].triggered.connect(lambda: self.save_data(actions[1].text()))
        # actions[2].triggered.connect(lambda: self.save_data(actions[2].text()))
        # actions[3].triggered.connect(lambda: self.save_data(actions[3].text()))
        # actions[4].triggered.connect(lambda: self.save_data(actions[4].text()))
        # actions[5].triggered.connect(lambda: self.save_data(actions[5].text()))
        # actions[6].triggered.connect(lambda: self.save_data(actions[6].text()))
        # actions[7].triggered.connect(lambda: self.save_data(actions[7].text()))
        # actions[8].triggered.connect(lambda: self.save_data(actions[8].text()))
        # self.signal = self.signal + [action.triggered for action in actions ]
        #
        # actions = self.ChildVision.actions_4
        # actions[0].triggered.connect(lambda: self.derive_data(actions[0].text()))
        # actions[1].triggered.connect(lambda: self.derive_data(actions[1].text()))
        # actions[2].triggered.connect(lambda: self.derive_data(actions[2].text()))
        # actions[3].triggered.connect(lambda: self.derive_data(actions[3].text()))
        # actions[4].triggered.connect(lambda: self.derive_data(actions[4].text()))
        # actions[5].triggered.connect(lambda: self.derive_data(actions[5].text()))
        # actions[6].triggered.connect(lambda: self.derive_data(actions[6].text()))
        # actions[7].triggered.connect(lambda: self.derive_data(actions[7].text()))
        # actions[8].triggered.connect(lambda: self.derive_data(actions[8].text()))
        # self.signal = self.signal + [action.triggered for action in actions]

    @func_set_timeout(Globals.timeout)  # 设定函数超执行时间_
    def run(self,module_input):
        if not isinstance(module_input,list) or not self.ChildVision.comboBox_45.currentText():
            return [[]],[]

        worldPoints = []
        module_input = module_input[-1]
        inputs = parameter_str_to_list(module_input,True)
        result = CCOperateDb.get_row(self.ChildVision.comboBox_45.currentText())
        if not result or not result[3]:
            return [[]],[]
        matrix = eval(result[3])
        if all(x == 0.0 for x in matrix):
            return [[]], []

        inputs = [inputs[i:i + 2] for i in range(0, len(inputs), 2)]
        for input in inputs:
            if not isinstance(input,list):
                return [[]],[]
            [x] , [y] = ImagetoWorld(input[0],input[1],matrix)
            # worldPoints.append([round(x,2),round(y,2)])
            worldPoints.append(round(x,2))
            worldPoints.append(round(y, 2))
        worldPoints = parameter_list_to_str(worldPoints)
        # worldPoints = [tuple(sublist) for sublist in worldPoints]
        return [module_input,worldPoints],[]


    def findPoint(self):
        '''搜索圆点'''
        imgpath = globalsdynamic.temp_path
        score = self.ChildVision.spinBox_11.value()
        size = self.ChildVision.spinBox_12.value()
        Rows, Columns = findRound(imgpath,score=score/100.0,size=size)
        num = len(Rows)
        if 9 > num >= 4:
            num = 4
            Rows = Rows[:4]
            Columns = Columns[:4]
            self.ChildVision.comboBox_16.setCurrentIndex(0)
        elif num >= 9:
            num = 9
            Rows = Rows[:9]
            Columns = Columns[:9]
            self.ChildVision.comboBox_16.setCurrentIndex(1)
        else:
            QMessageBox.warning(self.MainWindow, "错误", "没有找到四个以上圆点，请保证图片上至少有四个圆点，或者使用手动获取标定点！")
            # 不知道为什么有时会连续跳3次弹窗，所以加上断开连接。确保每次点击按钮时只会连接一次self.findPoint函数
            self.ChildVision.pushButton_37.clicked.disconnect()
            self.ChildVision.pushButton_37.clicked.connect(self.findPoint)
            return

        self.ChildVision.View.clear()
        for i in range(num-1,-1,-1):
            self.ponit_number = i
            self.getCoordinatePoint(Columns[i],Rows[i])
            self.ChildVision.View.addNewPoint(id=self.calibration_point_names[i], type='标定',pos=(Columns[i],Rows[i]))


    def changedComboBox(self):
        '''设置标定方式'''
        list1 = [4,9]
        list2 = ['第一点','第二点','第三点','第四点','第五点','第六点','第七点','第八点','第九点']
        self.index = int(self.ChildVision.comboBox_16.currentIndex()) # 标定方式索引
        self.ChildVision.stackedWidget_4.setCurrentIndex(self.index)
        self.calibration_mode = list1[self.index] # 标定方式
        self.calibration_point_names = list2[:self.calibration_mode] # 标定点名称列表
        self.ChildVision.comboBox_15.clear()
        for i in self.calibration_point_names:
            self.ChildVision.comboBox_15.addItem(i)

    def getCoordinatePoint(self,x,y):
        '''标定点坐标 输入参数为图像坐标'''
        lineEditx = self.Coordinate_imagex_list[self.index][self.ponit_number]
        lineEditx.setText(str(x))
        lineEdity = self.Coordinate_imagey_list[self.index][self.ponit_number]
        lineEdity.setText(str(y))

    def getCoordinate(self):
        '''点击图像获取标定点坐标'''
        self.ponit_number = int(self.ChildVision.comboBox_15.currentIndex())
        self.ChildVision.View.addNewPoint(id=self.calibration_point_names[self.ponit_number],type='标定')

    def CoordinateCalibration(self):
        '''坐标标定'''
        X,Y,Columns,Rows = [],[],[],[]
        for i in self.Coordinate_imagex_list[self.index]:
            if not i.text():
                QMessageBox.warning(self.MainWindow, "错误", "请填写所有坐标！")
                self.ChildVision.pushButton.clicked.disconnect()
                self.ChildVision.pushButton.clicked.connect(self.CoordinateCalibration)
                return None
            Columns.append(float(i.text()))
        for i in self.Coordinate_imagey_list[self.index]:
            if not i.text():
                QMessageBox.warning(self.MainWindow, "错误", "请填写所有坐标！")
                self.ChildVision.pushButton.clicked.disconnect()
                self.ChildVision.pushButton.clicked.connect(self.CoordinateCalibration)
                return None
            Rows.append(float(i.text()))
        for i in self.Coordinate_worldx_list[self.index]:
            if not i.text():
                QMessageBox.warning(self.MainWindow, "错误", "请填写所有坐标！")
                self.ChildVision.pushButton.clicked.disconnect()
                self.ChildVision.pushButton.clicked.connect(self.CoordinateCalibration)
                return None
            X.append(float(i.text()))
        for i in self.Coordinate_worldy_list[self.index]:
            if not i.text():
                QMessageBox.warning(self.MainWindow, "错误", "请填写所有坐标！")
                self.ChildVision.pushButton.clicked.disconnect()
                self.ChildVision.pushButton.clicked.connect(self.CoordinateCalibration)
                return None
            Y.append(float(i.text()))
        try:
            self.matrix,average_error = getTransformationMatrix(Columns,Rows,X,Y) # 转换矩阵
        except Exception as e:
            self.matrix = [0.0,0.0,0.0,0.0,0.0,0.0]
            average_error = 0.0
            QMessageBox.warning(self.MainWindow, "错误", f"请确保输入的标定点不共线或距离过近！")
        if not self.matrix:
            return None
        for i in range(len(self.matrix_list)):
            self.matrix_list[i].setText(str(self.matrix[i]))
        self.ChildVision.label_32.setText(str(average_error))


    def save_data(self):
        '''保存标定数据'''
        if not self.ChildVision.comboBox_45.currentText():
            QMessageBox.information(self.MainWindow, "错误", f"标定名称不能为空！")
            return
        try:
            name = self.ChildVision.comboBox_45.currentText()
            text = []
            for i in self.Coordinate_imagex_list[self.index]:
                text.append(i.text())
            for i in self.Coordinate_imagey_list[self.index]:
                text.append(i.text())
            for i in self.Coordinate_worldx_list[self.index]:
                text.append(i.text())
            for i in self.Coordinate_worldy_list[self.index]:
                text.append(i.text())
            data = {
                'name': name,
                'comboBoxIndex' : self.index, # 标定方式索引
                'text' : text, # 图像坐标
                'matrix' : self.matrix # 转换矩阵
            }

            # 数据库写入
            CCOperateDb.add_data(data)
            self.updata_name_changeds(isReturnOld=True)
        except Exception as e:
            QMessageBox.warning(self.MainWindow, "错误", f"保存标定数据失败：{e}！")
        else:
            QMessageBox.warning(self.MainWindow, "提示", f"保存标定数据成功！")

    def updataTODb(self):
        """读取数据库写入窗口"""
        result = CCOperateDb.get_row(self.ChildVision.comboBox_45.currentText())
        if not result:
            return
        if result[1]:
            self.ChildVision.comboBox_16.setCurrentIndex(int(result[1]))
        if result[2]:
            text = eval(result[2])
        num = 4 if self.index == 0 else 9
        for i in range(len(self.Coordinate_imagex_list[self.index])):
            self.Coordinate_imagex_list[self.index][i].setText(text[i])
        for i in range(len(self.Coordinate_imagey_list[self.index])):
            self.Coordinate_imagey_list[self.index][i].setText(text[num+i])
        for i in range(len(self.Coordinate_worldx_list[self.index])):
            self.Coordinate_worldx_list[self.index][i].setText(text[num*2+i])
        for i in range(len(self.Coordinate_worldy_list[self.index])):
            self.Coordinate_worldy_list[self.index][i].setText(text[num*3+i])
        if result[3]:
            matrix = eval(result[3])
            for i in range(len(self.matrix_list)):
                self.matrix_list[i].setText(str(matrix[i]))

    def updata_name_changeds(self,isReturnOld = False,isUdata = True):
        """更新名称列表"""
        name = self.ChildVision.comboBox_45.currentText()
        names = CCOperateDb.get_names()
        self.ChildVision.comboBox_45.clear()
        self.ChildVision.comboBox_45.addItems(names)
        if name and isReturnOld:
            self.ChildVision.comboBox_45.setCurrentText(name)
        if isUdata:
            self.updataTODb()

    def delete_data(self):
        """删除数据"""
        CCOperateDb.delete_row(self.ChildVision.comboBox_45.currentText())
        self.updata_name_changeds()

    def save_name(self):
        """保存当前表名"""
        if self.ChildVision.comboBox_45.currentText():
            CCNameDb.add_data({'name': self.ChildVision.comboBox_45.currentText()})
    def window_close(self):
        self.save_name()
        super().window_close()