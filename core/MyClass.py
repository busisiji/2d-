# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""重写类"""

import os
import threading
import time

import numpy as np
from PIL import Image
from PyQt5 import QtCore
from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciAPIs
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from core.模板匹配.STMOperateDb import STMOperateDb
from lib.path import path_join, Globals, globalsdynamic
from lib.utils import setLabelCentral, addImageNew, get_new_model_name


class LoadingProgress(QDialog):
    update_signal = QtCore.pyqtSignal(bool)

    def __init__(self, parent=None):
        """等待窗口"""
        super(LoadingProgress, self).__init__(parent)
        self.setWindowIcon(QIcon(path_join(Globals.project_path,"icon/logo.ico")))
        self.setWindowTitle('等待中...')
        self.value = 0
        self.update_signal.connect(self.update_progress)
        vbox = QVBoxLayout(self)
        self.steps = [f"程序运行中...",
                      "连接服务器中...",
                      "发送数据中...",
                      "接收数据中...",
                      "解析数据中..."]
        self.movie_label = QLabel()
        self.movie = QMovie(path_join(Globals.project_path,"icon/loading.gif"))
        self.movie_label.setMovie(self.movie)
        self.movie.start()
        self.progress_label = QLabel()
        self.label_update()

        vbox.addWidget(self.movie_label)
        vbox.addWidget(self.progress_label)
        self.setLayout(vbox)
        # self.exec_()
        self.setWindowModality(Qt.ApplicationModal) # 阻塞其他窗体
        self.show()
    def set_text(self,text):
        self.progress_label.setText(text)

    def label_update(self):
        self.progress_label.setText(self.steps[self.value])

    def update_progress(self, boolean: bool) -> None:
        self.value += 1
        if boolean and self.value < len(self.steps):
            self.label_update()
        else:
            self.close()


class WorkerThread(QThread):
    progressTrain = pyqtSignal(str)

class STMThread(WorkerThread):
    def __init__(self,STM):
        super().__init__()
        self.STM = STM
    def run(self):
        """模板匹配模型识别"""
        try:
            # 耗时任务
            self.STM.template_recognize_run()
        except Exception as e:
            self.progressTrain.emit(e)
        finally:
            self.progressTrain.emit('')


class ColorThread(WorkerThread):
    def __init__(self, CR, text):
        super().__init__()
        self.CR = CR
        self.text = text
    def run(self):
        """颜色识别模型训练"""
        # 耗时任务
        e = self.CR.colorrecognition.train(globalsdynamic.temp_path,self.text)
        e = str(e) if e else ''
        self.progressTrain.emit(e)

class CameraThread(QThread):
    progressRun = pyqtSignal(int)
    progressShow = pyqtSignal()

    def __init__(self, camera,parameters):
        super().__init__()
        self.camera = camera
        self.parameters = parameters

    def run(self):
        try:
            self.camera.run(self.parameters)
            self.camera.init_MV()
        except:
            self.progressRun.emit(0)
        else:
            if self.camera.cam and self.camera.data_buf:
                self.progressRun.emit(1)
            else:
                self.progressRun.emit(0)

# class ShowCameraThread(QThread):
#     def show(self,time=0.01):
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.show_next_image)
#         self.timer.start(1)  # 每隔time秒触发一次定时器
#     def show_next_image(self):
#         print('bbbb')
#         self.progressShow.emit()
#     def close(self):
#         self.timer.stop()

class MySpinBox(QSpinBox):
    returnPressed = pyqtSignal()
    def __init__(self, parent=None):
        super().__init__(parent)
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        # 通过在SpinBox上安装事件过滤器，并重写eventFilter方法来捕获回车键的按下事件。如果事件类型是QEvent.KeyPress并且是回车键（Qt.Key_Return或Qt.Key_Enter），则手动发出returnPressed信号
        if event.type() == QEvent.KeyPress and (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            self.returnPressed.emit()
            return True
        else:
            return super().eventFilter(obj, event)


class MyWidget(QWidget):
    size_changed = pyqtSignal(int, int)  # 定义一个大小改变的信号

    def resizeEvent(self, event):
        # 当控件大小改变时，发出size_changed信号，传递新的宽度和高度
        self.size_changed.emit(self.width(), self.height())

class MyLabel(QLabel):
    # 定义信号
    _signal_Press_pos = pyqtSignal(int, int)
    _signal_Press_get = pyqtSignal()
    sinw = pyqtSignal(int)
    flag_DoubleClick = True
    flag_getCoordinate = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._signal_Press_get.connect(self.isgetCoordinate)
        self.x0 = 0
        self.y0 = 0
        self.x1 = 1
        self.y1 = 1
        self.flag = False
        self.shape = ''

    def isgetCoordinate(self):
        self.flag_getCoordinate = True

    def drawRedDot(self, x, y):
        '''绘制红点'''
        painter = QPainter(self.image)
        pen = QPen(QColor("red"))
        pen.setWidth(3)  # 设置画笔宽度为3像素
        painter.setPen(pen)
        painter.setBrush(QColor("red"))
        painter.drawPoint(x, y)
        self.setPixmap(QPixmap.fromImage(self.image))

    def mousePressEvent(self, event):  # 鼠标单击
        self.flag = True  # 鼠标点击状态
        self.x0 = event.x()
        self.y0 = event.y()
        if event.button() == Qt.LeftButton and self.flag_getCoordinate:
            # 获取鼠标点击时的坐标
            x = event.x()
            y = event.y()

            # 获取label中的图像
            pixmap = self.pixmap()

            # 如果有图像
            if pixmap:
                # 将鼠标坐标转换为图像坐标
                image_x = int(x / self.width() * pixmap.width())
                image_y = int(y / self.height() * pixmap.height())
                self.drawRedDot(image_x, image_y)
                # 发射信号
                self._signal_Press_pos.emit(image_x, image_y)
                # return image_x, image_y
                self.flag_getCoordinate = False

    def mouseDoubleClickEvent(self, event):  # 鼠标双击
        if self.flag_DoubleClick == True:
            self.w = self.width()
            self.h = self.height()
            self.setWindowFlags(Qt.Window)  # 使得label位于最高级别的窗口
            self.showFullScreen()  # 全屏显示
            # self.setScaledContents (True)
            self.flag_DoubleClick = False
        else:
            self.setWindowFlags(Qt.SubWindow)  # 使得label回到子窗口级别
            self.showNormal()  # 恢复label原本大小
            self.resize(self.w, self.h)  # 使得label宽高恢复原样
            # self.setScaledContents (False)
            self.flag_DoubleClick = True
            setLabelCentral(self)

    # # 鼠标释放事件
    # def mouseReleaseEvent(self, event):
    #     self.flag = False  # 鼠标释放状态
    #     self.x1 = event.x()
    #     self.y1 = event.y()
    #     self.shape = ''
    #
    # # 鼠标移动事件
    # def mouseMoveEvent(self, event):
    #     if self.flag:
    #         self.x1 = event.x()
    #         self.y1 = event.y()
    #         self.update()
    #
    # # 绘制事件
    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     # 矩形
    #     if self.flag and self.move and self.shape=='矩形':
    #         rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
    #         painter = QPainter(self)
    #         painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
    #         painter.drawRect(rect)
    #     # 圆形
    #     if self.flag and self.move and self.shape == '圆形':  # 只有当鼠标按下并且移动状态
    #         rect = QRect(self.x0, self.y0, abs(self.x1 - self.x0), abs(self.y1 - self.y0))
    #         painter = QPainter(self)
    #         painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
    #         painter.drawEllipse(rect)
    #     # 圆环
    #     if self.flag and self.move and self.shape == '圆环':
    #         painter = QPainter(self)
    #         painter.setRenderHint(QPainter.Antialiasing)  # 设置抗锯齿
    #         painter.setPen(QPen(Qt.red))  # 设置画笔颜色
    #         painter.setBrush(Qt.NoBrush)  # 设置填充样式为无填充
    #
    #         outerRadius = 100  # 外圆半径
    #         innerRadius = 50  # 内圆半径
    #         centerX = self.width() / 2  # 圆心x坐标
    #         centerY = self.height() / 2  # 圆心y坐标
    #
    #         outerRect = QRectF(centerX - outerRadius, centerY - outerRadius, outerRadius * 2, outerRadius * 2)
    #         innerRect = QRectF(centerX - innerRadius, centerY - innerRadius, innerRadius * 2, innerRadius * 2)
    #
    #         painter.drawEllipse(outerRect)  # 绘制外圆
    #         painter.drawEllipse(innerRect)  # 绘制内圆

class TextLabel(QLabel):
    def mouseDoubleClickEvent(self, event):
        text, ok = QInputDialog().getText(QWidget(), '修改标签名', '输入文本:',text=self.text())
        if ok and text:
            self.setText(text)

class SliderButton(QAbstractButton):
    def __init__(self,parent = None):
        super(SliderButton, self).__init__(parent)
        # 内部圆直径
        self.innerDiameter = 12
        # 是否选中标志位
        self.checked = False
        # 鼠标形状
        self.setCursor(Qt.PointingHandCursor)
        # 设置遮罩，固定形状
        bitmap = QBitmap('icon/遮罩.png')
        self.resize(bitmap.width(),bitmap.height())
        self.setMask(bitmap)
        # 内边距
        self.innerMargin = (self.height() - self.innerDiameter) / 2
        # x坐标偏移量
        self.offset = self.innerMargin
        # 内部圆背景色
        self.innerColor = QColor(89,89,89)
        # 内部圆背景色选中
        self.innerColorChecked = QColor(255,255,255)
        # 外部背景色
        self.outerColor = QColor(64,64,64)
        # 外部背景色选中
        self.outerColorChecked = QColor(51,153,255)
        # 定时器ID
        self.timeId = None

    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)

        # 开启抗锯齿
        painter.setRenderHint(QPainter.Antialiasing)

        # 根据不同的选中状态切换内外颜色
        if self.checked:
            innerColor = self.innerColorChecked
            outerColor = self.outerColorChecked
        else:
            innerColor = self.innerColor
            outerColor = self.outerColor

        # 画外部圆角矩形
        painter.setBrush(outerColor)
        painter.drawRoundedRect(self.rect(),self.height() / 2,self.height() / 2)

        # 画内部圆形
        painter.setBrush(innerColor)
        painter.drawEllipse(QRectF(self.offset,self.innerMargin,self.innerDiameter,self.innerDiameter))

    def timerEvent(self, event):
        # 根据选中状态修改x坐标偏移值
        if self.checked:
            self.offset += 1
            if self.offset > (self.width() - self.innerDiameter - self.innerMargin):
                self.killTimer(self.timeId)
        else:
            self.offset -= 1
            if self.offset < self.innerMargin:
                self.killTimer(self.timeId)
        # 调用update，进行重绘
        self.update()

    def killTimer(self, timeId):
        # 删除定时器的同时，将timeId置为None
        super(SliderButton, self).killTimer(timeId)
        self.timeId = None

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.checked = not self.checked
            self.toggled.emit(self.checked)
            if self.timeId:
                self.killTimer(self.timeId)
            self.timeId = self.startTimer(5)

    def setChecked(self,checkState):
        # 如果状态没有变，不做处理
        if not checkState == self.checked:
            # 调用此方法改变状态不会触发动画，而是直接改变状态
            self.checked = checkState
            self.toggled.emit(checkState)
            if checkState:
                # 选中状态，偏移值设为最大值
                self.offset = self.width() - self.innerDiameter - self.innerMargin
            else:
                # 非选中状态，偏移值设置最小值
                self.offset = self.innerMargin
            # 更新界面
            self.update()

    def isChecked(self):
        return self.checked



class LightLabel(QLabel):
    """信号灯"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_ui()

    def set_ui(self,size=12):
        self.size = size
        self.setMinimumSize(QSize(size*2, size*2))
        self.setGeometry(QtCore.QRect(0, 0, size*2, size*2))
        self.setStyleSheet(
            "background-color: rgb(255, 0, 0);\n"f"border-radius: {size}px; border:\n"" 3px groove gray;border-style: outset;")

    def open_light(self):
        """开灯（改变标签背景为高亮的颜色）"""
        self.setStyleSheet(
            '''QLabel{{
            background-color: rgb(0, 234, 0);
            border-radius: {}px;
            border: 3px groove gray;
            border-style: outset;
        }}'''.format(self.size))

    def close_light(self):
        """关灯（改变标签背景为比较暗的颜色）"""
        self.setStyleSheet(
            '''QLabel{{
            background-color: rgb(255, 0, 0);
            border-radius: {}px;
            border: 3px groove gray;
            border-style: outset;
        }}'''.format(self.size))

class MyItemSelectionModel(QItemSelectionModel):
    def selection(self, selection, command):
        if command == QItemSelectionModel.SelectCurrent:
            # 获取当前选中的单元格的行和列
            current_index = selection.indexes()[0]
            row = current_index.row()
            column = current_index.column()

            # 如果是第2列，不允许选中
            if column == 1:
                return QItemSelection()

        return super().selection(selection, command)


class NewItemDialog(QDialog):
    '''对话框类'''

    def __init__(self, parent=None, name='对话框', default_text=''):
        super().__init__(parent)

        self.setWindowTitle(name)
        self.layout = QVBoxLayout()

        self.input_text = QLineEdit()
        self.input_text.setText(default_text)  # 设置默认值
        self.layout.addWidget(self.input_text)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.setText('确认')
        self.confirm_button.clicked.connect(self.on_confirm)
        self.layout.addWidget(self.confirm_button)

        self.setLayout(self.layout)

    def on_confirm(self):
        text = self.input_text.text()
        if text:
            self.accept()
        else:
            QMessageBox.warning(self, "错误", "项目名不能为空.")


class DeleteThread(QThread):
    _signal = pyqtSignal()

    def __init__(self, time=3):
        '''定时删除item'''
        super(DeleteThread, self).__init__()
        self.time = time

    def run(self):
        time.sleep(self.time)
        # item.scene().removeItem(item)
        self._signal.emit()

class MyListWidget(QListWidget):
    signal = pyqtSignal(list)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def context_menu(self, label):
        '''创建右键菜单'''
        self.label = label
        self.menu = QMenu(self)
        # 添加菜单项
        deleteAction = QAction("删除", self)
        deleteAction.triggered.connect(self.del_item)
        # 创建全部删除菜单项
        deleteAllAction = QAction("清空", self)
        deleteAllAction.triggered.connect(self.del_allitems)
        # 将菜单项添加到菜单中
        self.menu.addAction(deleteAction)
        self.menu.addAction(deleteAllAction)
        # 设置列表的上下文菜单策略
        self.setContextMenuPolicy(Qt.CustomContextMenu)

    def show_menu(self):
        '''显示右键菜单'''
        self.menu.exec_(QCursor.pos())  # 在鼠标位置显示
        # menu.exec_(self.viewport().mapToGlobal(position))


    def set_currentItem_matching_text(self, text):
        '''listwidget选中匹配项目'''
        # 查找具有匹配文本的项目
        matchingItems = self.findItems(text, Qt.MatchExactly)
        # 设置匹配项目为选中状态
        item = matchingItems[0]
        self.setCurrentItem(item)

    def get_listwidget_items(self):
        '''获取listwidget的选项列表'''
        itemlist = []
        # 获取项目总数
        itemCount = self.count()
        # 遍历获取每个项目
        for i in range(itemCount):
            item = self.item(i)
            itemlist.append(item)
        return itemlist
    def get_listwidget_item_names(self):
        '''获取listwidget的选项列表'''
        itemlist = []
        # 获取项目总数
        itemCount = self.count()
        # 遍历获取每个项目
        for i in range(itemCount):
            item = self.item(i)
            itemName = item.text()
            itemlist.append(itemName)
        return itemlist


    def del_item(self,db_name=None):
        '''删除选中选项'''
        # 更新数据库
        if db_name:
            id = "'" + str(self.currentRow()) + "'"
            # id = int(self.currentRow())
            globalsdynamic.db_child.delete_row_if(db_name, f"id = {id}")
            # self.rename_db(db_name)
        self.takeItem(self.currentRow()) # 用于删除当前选中的列表项
        if self.count() <= 0:
            self.label.clear()
            self.label.setText('图像展示')
            return
        path = self.currentItem().text()
        addImageNew(self.label, path, 374, 200)
        # self.get_listwidget_items()

    def del_allitems(self,db_name=None):
        '''清空选项'''
        self.clear()
        if self.count() <= 0:
            self.label.clear()
            self.label.setText('图像展示')
            return

        # 更新数据库
        if db_name:
            globalsdynamic.db_child.clear(db_name)
            # self.rename_db(db_name)

    def rename_db(self,db_name = None,name='id'):
        """重命名数据库的id列编号"""
        row_count = self.count() -1  # 总行数 除外最后一行空行
        # for i in range(row_count):
        #     # 更新数据库
        #     globalsdynamic.db_data.update_data_column(db_name,name,str(i),i+1)
        column0 = self.get_column_list(0)
        for i in range(len(column0)):
            self.table = {'id': str(i), 'name': str(column0[i])}
            globalsdynamic.db_child.insert_data(db_name, self.table)

class MyTableWidget(QTableWidget):
    signal = pyqtSignal(list)
    parameterName = 'input'
    def show_context_menu(self, pos):
        '''右键操作栏'''
        menu = QMenu(self)

        delete_action = QAction('删除', self)
        delete_action.triggered.connect(self.delete_row)
        menu.addAction(delete_action)

        clear_action = QAction('清空', self)
        clear_action.triggered.connect(self.clear_row)
        menu.addAction(clear_action)

        menu.exec_(self.viewport().mapToGlobal(pos))

    def set_row_data(self, row, text_list):
        """设置一行文本"""
        for column, text in enumerate(text_list):
            item = QTableWidgetItem(text)
            self.setItem(row, column, item)
        self.add_end_row()

    def get_column_data(self, column):
        """获取某列数据"""
        column_data = []
        for row in range(self.rowCount()):
            item = self.item(row, column)
            if item is not None:
                column_data.append(item.text())
        return column_data

    def rename_db(self,db_name = None):
        """重命名数据库的name列编号"""
        row_count = self.rowCount() -1  # 总行数 除外最后一行空行
        # for i in range(row_count):
        #     # 更新数据库
        #     globalsdynamic.db_data.update_data_column(db_name,name,str(i),i+1)
        column0 = self.get_column_list(0)
        for i in range(len(column0)):
            self.table = {'id': i, 'name': str(column0[i])}
            globalsdynamic.db_child.insert_data(db_name, self.table,'id')

    def delete_row(self,db_name = None):
        '''删除所选行'''
        try:
            selected_item = self.currentItem() # 选中的行
            if selected_item:
                row = selected_item.row()
                self.removeRow(row)
                # 更新数据库
                if db_name:
                    id = "'" + str(row) + "'"
                    globalsdynamic.db_child.delete_row_if(db_name, f"id = {id}")
                    # self.rename_db(db_name)

        except Exception as e:
            QMessageBox.information(self, "提示", f"删除失败：{e}")

    def clear_row(self,db_name = None):
        '''清空'''
        # 获取表格的行数和列数
        row_count = self.rowCount() # 总行数
        # 逐行删除
        for row in range(row_count-1):
            self.removeRow(0)

        # 更新数据库
        if db_name:
            globalsdynamic.db_child.clear(db_name)
            # self.rename_db(db_name)

    def find_same_name(self,text,column=0,skip_row=[]):
        """列查重"""
        for row in range(self.rowCount()):
            item = self.item(row, column)
            if not row in skip_row and item is not None and item.text() == text:
                return row
        return False

    def add_end_row(self):
        """增加最后空行"""
        # 获取QTableWidget的行数和列数
        row_count = self.rowCount()
        column_count = self.columnCount()

        # 判断最后一行是否非空
        last_row = row_count - 1
        is_last_row_nonempty = False

        for column in range(column_count):
            item = self.item(last_row, column)
            if item is not None and not item.text().strip() == "":
                is_last_row_nonempty = True
                break

        # 如果最后一行非空，则添加一行空行
        if is_last_row_nonempty:
            self.insertRow(row_count)


    def setcss(self,table):
        '''设置样式'''
        self.table = table
        self.num = len(self.table)
        self.setColumnCount(self.num)
        self.setHorizontalHeaderLabels(self.table)

        self.verticalHeader().setVisible(False) # 设置垂直表头为不可见
        header = self.horizontalHeader() # 获取表头部件
        header.setHighlightSections(False) # # 设置表头的高亮显示为不可选中

        self.setSelectionMode(QTableWidget.SingleSelection) # 设置选择模式为单选
        self.horizontalHeader().setDefaultAlignment(Qt.AlignCenter) # 设置表格的水平对齐方式为居中对齐
        self.setTextElideMode(Qt.ElideRight) # 设置表格的文本溢出策略为省略号
        self.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel) # 设置表格的水平滚动条策略为自动滚动
        self.setContextMenuPolicy(Qt.CustomContextMenu)  # 上下文菜单策略
        self.setFocusPolicy(Qt.NoFocus)  # 将表格的焦点策略设置为 Qt.NoFocus
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # 设置表格为自适应的伸缩模式

        # 设置表格样式
        self.verticalHeader().setStyleSheet("""
            QTableWidget {
                background-color: #f5f5f5;
                color: #333333;
                border: none;
                gridline-color: #cccccc;
                selection-background-color: #a6a6a6;
            }

            QTableWidget::item {
                padding: 5px;
            }
        """)
        self.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #b3c7e6;
                color: #333333;
                padding: 5px;
            }
        """)

        # 设置表格列宽
        self.setColumnWidth(0, 200)
        self.setColumnWidth(1, 200)

        # 设置表格字体
        font = QFont('Arial', 10)
        self.setFont(font)

        # 设置行交替颜色
        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            QTableView::item {
                background-color: #ffffff;
            }

            QTableView::item:alternate {
                background-color: #e0e0e0;
            }
        """)
        self.setStyleSheet("QTableWidget::item:selected { background-color: blue; }")

        # 设置右键菜单
        self.customContextMenuRequested.connect(self.show_context_menu)