# !/usr/bin/env python
# -*- encoding: utf-8 -*-
'''弹窗窗口'''
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from lib.path import Globals


class AwaitWindow(QDialog):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent = parent
        """等待窗口"""

    def show_progress(self,time=100):

        self.value = 0

        self.parent.progress_dialog = QProgressDialog(self.parent)
        self.parent.progress_dialog.setWindowTitle("等待窗口")
        self.parent.progress_dialog.setLabelText("正在执行任务...")
        self.parent.progress_dialog.setCancelButton(None)
        self.parent.progress_dialog.setWindowModality(Qt.WindowModal)
        self.parent.progress_dialog.show()
        self.parent.progress_dialog.canceled.connect(self.complete_progress) # 关闭
        self.timer = None
        if time:
            self.timer = QTimer()
            self.timer.timeout.connect(self.update_progress)
            self.timer.start(time)  # 1秒后进度条加1
    def update_progress(self,value=None):
        """更新等待窗口进度"""
        # 不确定任务完成时间
        if value != None:
            self.value = value
        if self.value < 100:
            self.parent.progress_dialog.setValue(self.value)
            self.value = self.value + 1
        if self.value == -1:
            self.parent.progress_dialog.hide()
            if self.timer:
                self.timer.stop()
    def complete_progress(self,e='取消'):
        """等待窗口关闭"""
        if self.timer:
            self.timer.stop()
        if e == '取消':
            # QMessageBox.warning(self, "提示", f"训练取消！")
            return
        elif e != '成功':
            self.parent.progress_dialog.close()
            QMessageBox.warning(self.parent, "错误", f"任务失败：{e}！")
        else:
            self.parent.progress_dialog.close()
            # QMessageBox.warning(self.parent, "提示", f"训练完成！")




class QsciParameterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        """参数输入窗口"""
        self.parent = parent
        self.setWindowTitle("添加数据类型")

        # 创建参数标签和文本框
        self.parameter_label1 = QLabel("类型：")
        # 创建 QComboBox 控件
        self.combo_box1 = QComboBox()

        for type in Globals.types:
            self.combo_box1.addItem(type)

        # 创建参数标签和文本框
        self.parameter_label2 = QLabel("名称：")
        self.parameter_edit2 = QLineEdit()
        # self.parameter_edit2.textChanged.connect(self.adjust_width)

        # 创建确定按钮和取消按钮
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # 创建布局并添加控件
        layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_2 = QHBoxLayout()
        h_layout_1.addWidget(self.parameter_label1)
        h_layout_1.addWidget(self.combo_box1)
        h_layout_1.addWidget(self.parameter_label2)
        h_layout_1.addWidget(self.parameter_edit2)
        h_layout_2.addWidget(self.ok_button)
        h_layout_2.addWidget(self.cancel_button)
        layout.addLayout(h_layout_1)
        layout.addLayout(h_layout_2)
        self.setLayout(layout)

        # 槽
        self.combo_box1.currentIndexChanged.connect(self.selection_changed)
        self.selection_changed(0)

    def selection_changed(self, index):
        # 获取选中的选项
        selected_option = self.combo_box1.currentText()
        name = self.parent.objectName()
        if name == 'tableWidget_4':
            self.parentText = '输入'
        elif name == 'tableWidget_5':
            self.parentText = '输出'
        else:
            self.parentText = ''
        text = self.parentText + selected_option + str(self.parent.currentRow()+1)
        self.parameter_edit2.setText(text)

    # def adjust_width(self, text):
    #     # 获取 QLineEdit 推荐的宽度
    #     width = self.parameter_edit2.fontMetrics().boundingRect(text).width() + 10
    #
    #     # 设置 QLineEdit 的宽度
    #     self.parameter_edit2.setFixedWidth(width)

    def get_parameter(self):
        # 获取参数文本框中的内容
        return [self.combo_box1.currentText(),self.parameter_edit2.text()]

class ModbusParameterDialog(QDialog, object):
    def __init__(self, parent=None,IsaddLayout= True):
        super().__init__(parent)
        """参数输入窗口"""
        self.parent = parent
        self.IsaddLayout = IsaddLayout
        self.setupUi(self)

        # 槽
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)

    def selection_changed(self, index=None):
        # 获取选中的选项
        selected_option = self.comboBox_3.currentText().split(' ')[-1]
        text = selected_option + str(self.parent.currentRow() + 1)
        self.lineEdit_4.setText(text)

    def get_parameter(self):
        """获取参数文本框中的内容"""
        return [self.comboBox.currentText(),self.lineEdit_4.text(),self.comboBox_3.currentText(),self.spinBox_3.text(),self.spinBox_2.text(),self.spinBox.text()]

    def accept(self):
        lineEdits = [self.lineEdit_4] if self.IsaddLayout else []
        # 检查所有的QLineEdit是否都有值
        for children in lineEdits:
            if not children.text():
                QMessageBox.information(self, "错误", "请填写所有选项！")
                # super().reject()
                return
        super().accept()

    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(305, 177)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel()
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.comboBox = QComboBox()
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label = QLabel()
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_4 = QLineEdit()
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout.addWidget(self.lineEdit_4)

        if self.IsaddLayout == True:
            self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(Frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox_3 = QComboBox(Frame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_2.addWidget(self.comboBox_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(Frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.spinBox_3 = QSpinBox(Frame)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy1.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy1)
        self.spinBox_3.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.spinBox_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.label_4 = QLabel(Frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.spinBox_2 = QSpinBox(Frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy1.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy1)
        self.spinBox_2.setMinimum(1)

        self.horizontalLayout_3.addWidget(self.spinBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(Frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.spinBox = QSpinBox(Frame)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy1.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy1)
        self.spinBox.setMinimum(1)

        self.horizontalLayout_4.addWidget(self.spinBox)

        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(Frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_5.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.pushButton_2 = QPushButton(Frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 0))
        self.pushButton_2.setMaximumSize(QSize(105, 16777215))

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"\u7c7b\u578b\uff1a  ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Frame", u"\u6570\u503c", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Frame", u"\u5b57\u7b26", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Frame", u"\u70b9", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Frame", u"\u5217\u8868", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Frame", u"\u56fe\u50cf", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Frame", u"\u8ddf\u968f", None))

        self.label.setText(QCoreApplication.translate("Frame", u"\u540d\u79f0\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"\u529f\u80fd\u7801\uff1a", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Frame", u"Read(01) \u7ebf\u5708\u72b6\u6001", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Frame", u"Read(02) \u8f93\u5165\u72b6\u6001", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Frame", u"Read(03) \u4fdd\u6301\u5bc4\u5b58\u5668", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Frame", u"Read(04) \u8f93\u5165\u5bc4\u5b58\u5668", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Frame", u"Read(05\uff09 \u5355\u7ebf\u5708", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Frame", u"Read(06) \u5355\u5bc4\u5b58\u5668", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("Frame", u"Read(15) \u591a\u7ebf\u5708", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("Frame", u"Read(16) \u591a\u5bc4\u5b58\u5668", None))

        self.label_3.setText(QCoreApplication.translate("Frame", u"\u4ece\u7ad9ID\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"\u5730\u5740\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"\u6570\u91cf\uff1a  ", None))
        self.pushButton.setText(QCoreApplication.translate("Frame", u"\u786e\u8ba4", None))
        self.pushButton_2.setText(QCoreApplication.translate("Frame", u"\u53d6\u6d88", None))
    # retranslateUi


