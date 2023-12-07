# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import time

from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem, QHeaderView, QAbstractItemView, QTableWidget, \
    QGraphicsTextItem
from func_timeout import func_set_timeout

from core.utils_window import utilsWindow
from core.颜色识别.CROperateDb import CROperateDb
from core.颜色识别.ColorRecognition import ColorRecognition, get_scale, add_text
from lib.file import delete_file
from lib.path import Globals, globalsdynamic
from lib.image import *
from core.MyClass import WorkerThread, MyTableWidget, ColorThread


class CRTableWidget(MyTableWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def delete_row(self):
        super().delete_row(db_name=None)
        CROperateDb.delete_table_row(self.currentRow())
        if not self.rowCount():
            self.insertRow(0)  # 插入一行

    def clear_row(self,use=True,db_name = Globals.toname['颜色识别']):
        super().clear_row(db_name = db_name)
        self.add_item()

    def get_column_list(self,index=0):
        """获取某列的值"""
        text_list = []  # 存储文本的列表

        for row in range(self.rowCount()):
            item = self.item(row, index)
            if item is not None:
                text = item.text()
                text_list.append(text)

        return text_list

    def set_item(self,text,column=1):
        row = self.currentRow()  # 选中的行
        if row >= 0:
            newItem = QTableWidgetItem(str(text))
            self.setItem(row, column, newItem)
            return True
        return False

    def add_item(self):
        """新增一行"""
        # 若最后一行空行被写入则在最后添加一行
        row = self.currentRow()  # 选中的行
        row_count = self.rowCount()  # 总行数
        if (row == row_count - 1 and self.item(row, 0)) or not self.rowCount():
            self.insertRow(row_count)  # 插入一行

    def setcss(self,table):
        super().setcss(table)
        if len(table) == 3:
            header = self.horizontalHeader()  # 获取表头部件
            header.setSectionResizeMode(1, QHeaderView.Stretch)  # 自动调整宽度
            header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 根据内容调整宽度
            header.setSectionResizeMode(2, QHeaderView.ResizeToContents)  # 根据内容调整宽度
        self.verticalHeader().setVisible(True)  # 设置垂直表头为可见
        self.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选择行为为选择整行
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 将表格变为禁止编辑
        # self.insertRow(0)  # 插入一行

class ColorRecognitionWindow(utilsWindow):
    '''颜色识别界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision
        self.colorrecognition = None
        self.data = {'name': globalsdynamic.value, 'temppath': '','num':""}
        self.keys = ['name', 'temppath','num']
        self.isolated = True # 是否单独运行

        self.signalSlotConnection()

    def setcss(self):
        self.ChildVision.stackedWidget_2.setCurrentIndex(0)
        result = CROperateDb.get_row()
        if result and result[5]:
            value = int(result[5])
        else:
            value = 200
        self.setSpinbox(self.ChildVision.spinBox_19, value, 1, 10000, 10)  # 迭代次数

    def signalSlotConnection(self):
        self.signal = [self.ChildVision.pushButton_42,self.ChildVision.pushButton_17,self.ChildVision.pushButton_23,
                       self.ChildVision.pushButton_15,self.ChildVision.pushButton_39,self.ChildVision.pushButton_24,
                       self.ChildVision.pushButton_16]
        super().signalSlotConnection()

        # if Globals.isSignalSlotConnection['颜色识别']: # 演示关闭后重开不触发
        #     return
        # 模板
        self.ChildVision.pushButton_42.clicked.connect(self.template_select)
        self.ChildVision.pushButton_17.clicked.connect(self.test_select)
        self.ChildVision.pushButton_23.clicked.connect(self.train_colorrecognition)
        self.ChildVision.pushButton_15.clicked.connect(self.detect_colorrecognition)
        self.ChildVision.pushButton_39.clicked.connect(self.close_gather)
        self.ChildVision.pushButton_24.clicked.connect(self.save_gather)

        # self.ChildVision.tableWidget.itemDoubleClicked.connect(self.handle_double_click) # 双击，不包括空白行
        self.ChildVision.tableWidget.cellDoubleClicked.connect(self.handle_double_click)

        self.ChildVision.pushButton_16.clicked.connect(self.window_close)

        Globals.isSignalSlotConnection['颜色识别'] = True

    @func_set_timeout(Globals.timeout*2)  # 设定函数超执行时间_
    def run(self, module_input,boxs,last_name):
        """颜色识别运行"""
        # 连接模板匹配
        if last_name == '模板匹配':
            img_path = module_input[-1]
            globalsdynamic.temp_path = img_path

            poss = [QPoint(box[0], box[1]) for box in boxs]
            sizes = [QSizeF(box[2] - box[0], box[3] - box[1]) for box in boxs]
            results = ''
            result_list = []
            for i in range(len(boxs)):
                result = self.detect_colorrecognition(poss[i],sizes[i])
                # 参数格式调整
                results = results + result
                if i < len(boxs)-1:
                    results = results + '|'
                result_list.append(result)
            self.color_result_show(result_list,boxs)
            return [globalsdynamic.temp_path,len(boxs),results,globalsdynamic.temp_path] , []
        # 连接图像设备
        elif last_name == '图像设备':
            self.isolated = True
            self.detect_colorrecognition()
            return [globalsdynamic.temp_path,0,'',globalsdynamic.temp_path ], []
        else:
            raise Exception("没有输入图像！")
            # return [[], [], '', []],[]

    def handle_double_click(self, row):
        '''处理表格项双击事件'''
        item = self.ChildVision.tableWidget.item(row, 0)
        if item:
            text = self.ChildVision.tableWidget.item(row, 0).text()
            self.ChildVision.lineEdit_3.setText(text)
            text = self.ChildVision.tableWidget.item(row, 1).text()
            if text and text != 'None':
                self.ChildVision.View.addNewSelection(id="SelectionBox", type=text.split(',')[0])
        self.ChildVision.stackedWidget_2.setCurrentIndex(1)

    def template_result_noshow(self):
        """模板匹配识别结果显示结束"""
        # halcon
        # if self.ChildVision.View.temp_path and 'temp_halcon' in self.ChildVision.View.temp_path:
        #     self.ChildVision.View.displayImg(QImage(globalsdynamic.temp_path),globalsdynamic.temp_path)
        # view
        self.ChildVision.View.clear()

    def template_select(self):
        '''新建选取框'''
        self.template_result_noshow()
        type_select = self.ChildVision.comboBox_13.currentText()
        self.ChildVision.View.clear()
        self.ChildVision.View.addNewSelection(id="SelectionBox",type=type_select)
    def test_select(self):
        '''新建选取框'''
        self.template_result_noshow()
        type_select = self.ChildVision.comboBox_12.currentText()
        self.ChildVision.View.clear()
        self.ChildVision.View.addNewSelection(id="SelectionBox",type=type_select)

    def save_gather(self):
        """保存采集数据"""
        text0 = self.ChildVision.lineEdit_3.text()
        if not text0:
            QMessageBox.warning(self.MainWindow, "错误", "请输入样本名！")
            return None
        if self.ChildVision.tableWidget.find_same_name(text0,skip_row=[self.ChildVision.tableWidget.currentRow()]):
            QMessageBox.warning(self.MainWindow, "错误", "已经有相同的样本名了！")
            return None

        # self.color = self.ChildVision.tableWidget.get_column_list()
        # self.colorrecognition = ColorRecognition(self.color)
        item = self.ChildVision.View.get_active()
        if not item:
            if not self.ChildVision.tableWidget.item(self.ChildVision.tableWidget.currentRow(), 1):
                QMessageBox.warning(self.MainWindow, "错误", "请创建采集区域！")
            return None

        if item.type == '矩形':
            pos = item.getPos() - self.ChildVision.View.playbackItem.pos()
            row1, Column1 = pos.x(), pos.y()
            row2, Column2 = pos.x() + item.getWidth(), pos.y() + item.getHeight()
            # self.colorrecognition.addclass_rectangle(row1, Column1, row2, Column2)
            point = round((row2 + row1) / 2,2),round((Column2 + Column1) / 2,2)
            size = round(row2 - row1,2),round(Column2 - Column1,2)
            text1 = f'矩形,中心点:{point},宽高:{size}'
            # QMessageBox.warning(self.MainWindow, "提示", "采集成功！")
        elif item.type == '圆形':
            center = item.getCentral() - self.ChildVision.View.playbackItem.pos()
            row, Column = center.x(), center.y()
            r = item.getWidth() / 2
            # self.colorrecognition.addclass_circle(row, Column, r)
            text1 = f'圆形,中心点:{(round(row,2), round(Column,2))},半径:{round(r,2)}'
            # QMessageBox.warning(self.MainWindow, "提示", "采集成功！")
        else:
            text1 = None
        self.ChildVision.View.updateScaleRatio()
        scale = round(self.ChildVision.View.initscaleRatio,2)
        self.ChildVision.tableWidget.set_item(text0, 0)
        self.ChildVision.tableWidget.set_item(text1, 1)
        self.ChildVision.tableWidget.set_item(scale, 2)
        self.ChildVision.tableWidget.add_item()

        # 写入数据库
        CROperateDb.add_table(self.ChildVision.tableWidget.get_column_list(0),self.ChildVision.tableWidget.get_column_list(1),scale)


    def close_gather(self):
        """关闭采集窗口"""
        self.ChildVision.View.clear()
        self.ChildVision.stackedWidget_2.setCurrentIndex(0)

    def init_colorrecognition(self,isReadmodelName=True):
        self.color = self.ChildVision.tableWidget.get_column_list()
        result = CROperateDb.get_row()
        self.modelName = path_join(globalsdynamic.data_path, 'color' + str(
            time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())) + '.mlp')  # 颜色识别模型存储路径
        if result and result[6]:
            if isReadmodelName:
                self.modelName = result[6]
            else:
                delete_file(result[6])
        self.colorrecognition = ColorRecognition(self.color,self.modelName)
        return

    def addclass_rectangle(self,row1, column1, row2, column2,num=0):
        '''加入样本'''
        if not self.colorrecognition.addclass_rectangle(row1, column1, row2, column2) and num <= 10:
            num = num + 1
            self.train_colorrecognition(num)
            return False
        return True

    def train_colorrecognition(self,num=0):
        '''训练模型'''
        self.init_colorrecognition(False)
        if len(self.color) <= 1:
            QMessageBox.warning(self.MainWindow, "错误", "请保证颜色样本至少有两个以上！")
            return None
        # 获取采集的样本并存储在Classes字典中
        Classes = {'矩形':[],'圆形':[]}
        texts = self.ChildVision.tableWidget.get_column_list(1)
        scales = self.ChildVision.tableWidget.get_column_list(2)
        for i in range(len(texts)):
            text = texts[i]
            point_str = text.split('(')[1].split(')')[0]
            point = float(point_str.split(',')[0]),float(point_str.split(',')[1])
            scale = float(scales[i])
            if '矩形' in text:
                size_str = text.split('(')[-1].split(')')[0]
                size = float(size_str.split(',')[0]), float(size_str.split(',')[1])
                Classes['矩形'].append([point,size,scale])
            elif '圆形' in text:
                r = float(text.split(':')[-1])
                Classes['圆形'].append([point,r,scale])
        for point, size ,scale in Classes['矩形']:
            # 将采集到的矩形在item坐标系上的左上角和右下角的坐标转换为图像上的坐标
            row1 = scale * (point[0] - size[0]/ 2)
            column1 = scale * (point[1] - size[1] / 2)
            row2 = scale * (point[0] + size[0] / 2)
            column2 = scale * (point[1] + size[1] / 2)
            try:
                if not self.colorrecognition.addclass_rectangle(row1, column1, row2, column2):
                    QMessageBox.warning(self.MainWindow, "错误", f"找不到坐标轴，请重新采集样本！")
                    return None
            except:
                QMessageBox.warning(self.MainWindow, "错误", f"找不到坐标轴，请重新采集样本！")
                return None
        for point,r ,scale in Classes['圆形']:
            # 将采集到的圆形在item坐标系上的中心的坐标和半径的大小转换为图像上的坐标和大小
            row = scale * (point[0])
            column = scale * (point[1])
            r = scale * (r)
            if not self.colorrecognition.addclass_circle(row, column, r):
                QMessageBox.warning(self.MainWindow, "错误", f"找不到坐标轴，请重新采集样本！")
                return None

        # e = self.colorrecognition.train(globalsdynamic.temp_path,max_iterations=self.ChildVision.spinBox_19.text())
        # if e:
        #     QMessageBox.warning(self.MainWindow, "错误", f"训练样本出错：{e}！")
        #     return None

        # 训练 等待窗口
        self.MainWindow.awaitWindow.show_progress()
        self.worker_thread = ColorThread(self,text=self.ChildVision.spinBox_19.text())
        self.worker_thread.progressTrain.connect(lambda : self.MainWindow.awaitWindow.complete_progress('成功'))
        self.worker_thread.start()


        # # 模型写入数据库
        data = {}
        data['temppath'] = globalsdynamic.temp_path
        data['num'] = str(self.ChildVision.spinBox_19.text())
        data['modelName'] = self.modelName
        CROperateDb.add_data(data)

    def detect_colorrecognition(self,pos=QPoint(0,0),size=QSizeF(0,0)):
        '''识别测试'''
        try:
            if self.isolated:
                # 手动框选
                # 获取图像上要识别的区域
                item = self.ChildVision.View.get_active()
                if not item and self.isolated:
                    QMessageBox.warning(self.MainWindow, "错误", "请创建识别区域！")
                    return None
                pos = item.getPos() - self.ChildVision.View.playbackItem.pos()
                size = QSizeF(item.getWidth(),item.getHeight())
                row = self.ChildVision.View.item_to_img(pos.x())
                column = self.ChildVision.View.item_to_img(pos.y())
                weight = self.ChildVision.View.item_to_img(size.width())
                height = self.ChildVision.View.item_to_img(size.height())
            else:
                # 使用模板匹配的识别框
                row,column,weight,height = pos.x(),pos.y(),size.width(),size.height()

            image=QImage(globalsdynamic.temp_path)
            cropped_image = image.copy(row, column, weight, height)
            if self.isolated and item and item.type == '圆形':
                cropped_image = crop_circle(cropped_image)
            cropped_image.save(Globals.color_image_path)

            self.init_colorrecognition()
            if len(self.color) <= 1:
                QMessageBox.warning(self.MainWindow, "错误", "请保证颜色样本至少有两个以上！")
                return None

            result = self.colorrecognition.classify(Globals.color_image_path)
            if not result:
                QMessageBox.warning(self.MainWindow, "错误", f"颜色识别失败，请重新训练样本！")
                return
            result, _ = result

            if self.isolated:
                QMessageBox.warning(self.MainWindow, "提示", f"颜色识别结果为：{result}！")
            return result
        except Exception as e:
            print(e)
            raise  # 重新引发异常


    def color_result_show(self,texts,boxs):
        '''显示颜色识别结果'''
        textItem = self.ChildVision.View.text_items
        self.ChildVision.View.clearShowBoxText()
        # 显示识别结果
        for i in range(len(boxs)):
            # x1, y1, x2, y2 = boxs[i]
            text = textItem[i].toPlainText().split('\n')[-2] + '\n' + texts[i]
            item = self.ChildVision.View.show_items[i]

            self.ChildVision.View.addShowBoxText(item,text)