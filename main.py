# !/usr/bin/env python
# -*- encoding: utf-8 -*-

# 静态载入
import functools
import json
import logging
import os
import sys
from PyQt5.QtCore import QTimer, Qt, QCoreApplication
from PyQt5.QtGui import QFontMetrics
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget, QMessageBox, QProgressDialog
from PyQt5.uic.properties import QtCore
from qt_material import apply_stylesheet

from core.PopUpWindow import AwaitWindow
from core.init_window import init_visionWindow, init_mainWindow
# 本地包导入
from core.VisionWinodw import Visionwindow
from lib.file import write_json, make_new_folder
from lib.path import path_join, Globals, globalsdynamic
from lib.utils import resizeGL
from ui.ui_mainwindow import Ui_MainWindow, Ui_configure
from ui.ui_visionwindow import Ui_VisionWindow

QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling) # 自适应分辨率的字体大小

# 日志文件
logging.basicConfig(filename='log/example.log', level=logging.DEBUG,format='\r\n%(asctime)s %(levelname)s：%(message)s')
# 打开日志文件并将其截断为零字节
with open(path_join(Globals.project_path,'log/example.log'), 'w'):
    pass

class MainWindow(Ui_MainWindow, QMainWindow):
    '''主界面'''
    def __init__(self):
        super().__init__()
        # 主窗口
        self.setupUi(self)
        self.setcss()
        # 视觉窗口
        self.is_first_move = True
        self.ChildConfigure = Ui_configure()
        self.ChildVision = Ui_VisionWindow()
        self.ChildVision.setupUi(self)
        self.ChildVision.setcss()

        # 获取显示器分辨率
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        Globals.screenheight = self.screenRect.height()
        Globals.screenwidth = self.screenRect.width()

        # 自适应屏幕大小
        self.height = int(Globals.screenheight * 0.7)
        self.width = int(Globals.screenwidth * 0.7)
        # self.resize(self.width, self.height)

        # Globals.datas_path = path_join(Globals.project_path, 'data') # 项目文件存储目录
        # 等待窗口
        self.awaitWindow = AwaitWindow(self)

        # 响应事件类
        # self.imageCapture = ImageCapture(self)

        # 窗口切换
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)
        self.child_window1 = self.widget_2
        self.child_window2 = self.ChildVision.widget_1
        self.stacked_widget.addWidget(self.child_window1)
        self.stacked_widget.addWidget(self.child_window2)
        self.stacked_widget.setCurrentWidget(self.child_window1)

        # 图像全屏
        self.isFull = False
        self.nofullpagetype = self.stackedWidget_3.currentIndex()

        # 设置默认值
        self.comboBox.setCurrentIndex(3)

        self.signalSlotConnection()
        # 设置主窗口为模态模式
        # self.setWindowModality(Qt.ApplicationModal)
        # self.show()

        QTimer.singleShot(100, self.init)
        QTimer.singleShot(100, lambda : resizeGL(self))

    def init(self):
        init_mainWindow(self)
        # font_metrics = QFontMetrics(self.label_321.font())
        # self.label_321.setMaximumWidth(int(self.label_321.parentWidget().width() * 9 / 10))

    def signalSlotConnection(self):
        '''信号-槽'''
        self.ptn_ok.clicked.connect(self.composeOk)
        self.toolButton.clicked.connect(self.fireuConfig)

        for i in range(len(self.class_page_btns1)):
            for j in range(len(self.class_page_btns1[i])):
                label = self.label_central_class[i][j]
                # lambda表达式中的参数捕获的是循环变量的最后一个值
                func = functools.partial(self.show_child_window, parentlabel=label)
                self.class_page_btns1[i][j].clicked.connect(func)
        self.ChildVision.tabWidget.tabCloseRequested.connect(self.close_child_window)# 关闭选项卡

        self.ChildConfigure._signal.connect(self.addLabel)

    #

    def resizeSwitchWindow(self):
        '''切换窗口后大小位置重置'''
        current_child_window = self.stacked_widget.currentWidget()
        if current_child_window == self.child_window1:
            # 在这里处理第一个子窗口的resizeEvent逻辑
            resizeGL(self)
            self.widget_3.move(9, abs(int((self.widget_10.height()-self.widget_3.height())/2)))
            # self.widget_3.move(0,abs(int(self.widget_10.height()-self.widget_3.height()/2)))

    def composeOk(self):
        '''切换图像显示模块的排版'''
        self.comboBox_type = int(self.comboBox.currentIndex())
        self.stackedWidget_3.setCurrentIndex(self.comboBox_type)
        self.nofullpagetype = self.comboBox_type
        resizeGL(self)

    def show_child_window(self,parentlabel):
        '''打开视觉界面'''
        label_name = parentlabel.objectName()
        child_name = label_name.split('_')[1]

        # 更新项目路径
        Globals.db_main.insert_data('Now', {'name': 'now', 'child': child_name})
        # globalsdynamic.update_main_path()
        # make_new_file(globalsdynamic.data_path)
        globalsdynamic.update_main_path()

        if not globalsdynamic.data_path:
            QMessageBox.warning(self, "错误", "请先选择一个项目工程.")
            return None

        self.ChildVisionCode = Visionwindow(self)

        self.ChildVision.parentlabel = parentlabel
        # self.ChildVision.stackedWidget.show()

        self.stacked_widget.setCurrentWidget(self.child_window2)
        init_visionWindow(self.ChildVision) # 初始化视觉窗口
        # resizeGL(self.ChildVision,'child_window2')

    def close_child_window(self):
        '''关闭视觉界面'''
        self.ChildVisionCode.close() # 关闭视觉界面
        self.ChildVision.stackedWidget.close()
        self.ChildVision.widget_11.show()
        # self.ChildVision.stackedWidget.hide()
        self.stacked_widget.setCurrentWidget(self.child_window1)
        # resizeGL(self.ChildVision,'child_window2')
        # 关闭流程树
        self.ChildVision.nodeEditWind.close()
        # 清空样板
        blackimg_path = path_join(Globals.project_path, 'icon/black.jpg')
        if os.path.exists(blackimg_path):
            self.ChildVision.View.showImgpath(blackimg_path)

        self.resizeSwitchWindow()

    def fireuConfig(self):
        '''打开 参数配置 窗口'''
        self.ChildConfigure.show()
    def addLabel(self,row,value):
        '''接收 参数配置 窗口参数'''
        print("接收到信号")

        if row and value:
            self.label_311.setText(row)
            self.label_321.setText(value)
            self.ChildConfigure.hide()

            # 关闭数据库连接
            if globalsdynamic.db_child:
                globalsdynamic.db_child.close()

            # 保存选择的项目文件
            data = {'name': 'now',
                    'row': row,
                    'value': value}
            Globals.db_main.create_tables('Now', ['name','row','value','child'])
            Globals.db_main.insert_data('Now', data)
            # 初始化
            globalsdynamic.update_main_path()
            init_mainWindow(self)


    def resizeEvent(self, event):
        '''重写移动事件'''
        super().resizeEvent(event)

        if self.is_first_move:
            # 在第一次移动时执行特定的代码逻辑
            self.is_first_move = False
            return
        self.resizeSwitchWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    # setup stylesheet
    # apply_stylesheet(app, theme='dark_teal.xml')
    window.show()
    sys.exit(app.exec_())