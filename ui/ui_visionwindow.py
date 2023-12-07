# -*- coding: utf-8 -*-
import logging

from core.模板匹配.ShapTemplateMatchingWindow import ImageListWidget
from core.MyClass import *
from core.imageGraphicsClass import *
from core.自定义输出.OutputWindow import OutputtableWidget
from lib.path import Globals
from core.数据转换.QsciScintillaWindow import QsciTableWidget
from core.CodeCompilerClass import codeCompilerPy,codeCompilerVBS
from core.颜色识别.ColorRecognitionWindow import CRTableWidget
import resource_rc

logging.basicConfig(filename=Globals.filename, level=logging.DEBUG, format='\r\n%(asctime)s %(levelname)s：%(message)s')
# 打开日志文件并将其截断为零字节
with open(Globals.filename, 'w'):
    pass


class Ui_VisionWindow(object):
    '''视觉应用界面'''

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1042, 1058)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/logo/icon/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(55, 81, 134);")
        MainWindow.setIconSize(QSize(24, 24))
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        icon1 = QIcon()
        icon1.addFile(u":/file/icon/file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action.setIcon(icon1)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        icon2 = QIcon()
        icon2.addFile(u":/run/icon/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_2.setIcon(icon2)
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        icon3 = QIcon()
        icon3.addFile(u":/over/icon/over.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_3.setIcon(icon3)
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        icon4 = QIcon()
        icon4.addFile(u":/compose type/icon/compose.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_4.setIcon(icon4)
        self.actionlogo = QAction(MainWindow)
        self.actionlogo.setObjectName(u"actionlogo")
        icon5 = QIcon()
        icon5.addFile(u":/logo/icon/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.actionlogo.setIcon(icon5)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_14 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_1 = QWidget(self.centralwidget)
        self.widget_1.setObjectName(u"widget_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_1.sizePolicy().hasHeightForWidth())
        self.widget_1.setSizePolicy(sizePolicy1)
        self.gridLayout_13 = QGridLayout(self.widget_1)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget = QTabWidget(self.widget_1)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.tabWidget.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabsClosable(True)
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.widget_3 = QWidget(self.tab_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.widget_3)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy4)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout = QVBoxLayout(self.tab_3)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.tab_3)
        self.widget.setObjectName(u"widget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.widget.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_31 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_31)

        self.toolButton_14 = QToolButton(self.widget)
        self.toolButton_14.setObjectName(u"toolButton_14")
        self.toolButton_14.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.toolButton_14.sizePolicy().hasHeightForWidth())
        self.toolButton_14.setSizePolicy(sizePolicy6)
        self.toolButton_14.setMinimumSize(QSize(50, 0))
        self.toolButton_14.setMaximumSize(QSize(60, 16777215))
        font = QFont()
        font.setPointSize(9)
        self.toolButton_14.setFont(font)
        self.toolButton_14.setLayoutDirection(Qt.LeftToRight)
        self.toolButton_14.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.toolButton_14.setIcon(icon2)
        self.toolButton_14.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.toolButton_14)

        self.horizontalSpacer = QSpacerItem(0, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.toolButton_15 = QToolButton(self.widget)
        self.toolButton_15.setObjectName(u"toolButton_15")
        self.toolButton_15.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.toolButton_15.sizePolicy().hasHeightForWidth())
        self.toolButton_15.setSizePolicy(sizePolicy6)
        self.toolButton_15.setMinimumSize(QSize(50, 0))
        self.toolButton_15.setMaximumSize(QSize(60, 16777215))
        self.toolButton_15.setFont(font)
        self.toolButton_15.setLayoutDirection(Qt.LeftToRight)
        self.toolButton_15.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        icon6 = QIcon()
        icon6.addFile(u":/\u76f8\u673a/icon/\u9884\u89c8.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_15.setIcon(icon6)
        self.toolButton_15.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.toolButton_15)

        self.label_44 = QLabel(self.widget)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_2.addWidget(self.label_44)

        self.label_42 = LightLabel(self.widget)
        self.label_42.setObjectName(u"label_42")

        self.horizontalLayout_2.addWidget(self.label_42)

        self.horizontalSpacer_32 = QSpacerItem(10, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_32)

        self.verticalLayout.addWidget(self.widget)

        self.widget_4 = QWidget(self.tab_3)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.gridLayout_25 = QGridLayout(self.widget_11)
        self.gridLayout_25.setObjectName(u"gridLayout_25")

        self.verticalLayout_2.addWidget(self.widget_11)

        self.stackedWidget = QStackedWidget(self.widget_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy7)
        self.page_CC = QWidget()
        self.page_CC.setObjectName(u"page_CC")
        sizePolicy7.setHeightForWidth(self.page_CC.sizePolicy().hasHeightForWidth())
        self.page_CC.setSizePolicy(sizePolicy7)
        self.gridLayout = QGridLayout(self.page_CC)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.page_CC)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout_4 = QGridLayout(self.widget_6)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_3 = QTabWidget(self.widget_6)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        sizePolicy7.setHeightForWidth(self.tabWidget_3.sizePolicy().hasHeightForWidth())
        self.tabWidget_3.setSizePolicy(sizePolicy7)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.tab)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMinimumSize(QSize(0, 200))
        self.widget_17.setSizeIncrement(QSize(0, 0))
        self.gridLayout_20 = QGridLayout(self.widget_17)
        self.gridLayout_20.setSpacing(6)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(9, 9, 9, 9)
        self.groupBox_13 = QGroupBox(self.widget_17)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setMinimumSize(QSize(0, 0))
        self.gridLayout_23 = QGridLayout(self.groupBox_13)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.label_23 = QLabel(self.groupBox_13)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_23.addWidget(self.label_23, 2, 1, 1, 1)

        self.label_25 = QLabel(self.groupBox_13)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_23.addWidget(self.label_25, 0, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_13)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_23.addWidget(self.label_29, 0, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_13)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_23.addWidget(self.label_30, 2, 0, 1, 1)

        self.label_27 = QLabel(self.groupBox_13)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_23.addWidget(self.label_27, 1, 1, 1, 1)

        self.label_31 = QLabel(self.groupBox_13)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_23.addWidget(self.label_31, 3, 0, 1, 1)

        self.label_32 = QLabel(self.groupBox_13)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_23.addWidget(self.label_32, 3, 1, 1, 2)

        self.label_24 = QLabel(self.groupBox_13)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_23.addWidget(self.label_24, 2, 2, 1, 1)

        self.label_28 = QLabel(self.groupBox_13)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_23.addWidget(self.label_28, 1, 2, 1, 1)

        self.label_26 = QLabel(self.groupBox_13)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_23.addWidget(self.label_26, 0, 2, 1, 1)

        self.gridLayout_20.addWidget(self.groupBox_13, 4, 0, 1, 1)

        self.stackedWidget_4 = QStackedWidget(self.widget_17)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        sizePolicy5.setHeightForWidth(self.stackedWidget_4.sizePolicy().hasHeightForWidth())
        self.stackedWidget_4.setSizePolicy(sizePolicy5)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.page_5.sizePolicy().hasHeightForWidth())
        self.page_5.setSizePolicy(sizePolicy8)
        self.gridLayout_51 = QGridLayout(self.page_5)
        self.gridLayout_51.setSpacing(0)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.gridLayout_51.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_52 = QGridLayout()
        self.gridLayout_52.setSpacing(0)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.groupBox_22 = QGroupBox(self.page_5)
        self.groupBox_22.setObjectName(u"groupBox_22")
        sizePolicy7.setHeightForWidth(self.groupBox_22.sizePolicy().hasHeightForWidth())
        self.groupBox_22.setSizePolicy(sizePolicy7)
        self.groupBox_22.setFlat(False)
        self.groupBox_22.setCheckable(False)
        self.groupBox_22.setChecked(False)
        self.gridLayout_64 = QGridLayout(self.groupBox_22)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.gridLayout_64.setVerticalSpacing(0)
        self.gridLayout_64.setContentsMargins(6, 0, 6, 0)
        self.label_171 = QLabel(self.groupBox_22)
        self.label_171.setObjectName(u"label_171")
        sizePolicy3.setHeightForWidth(self.label_171.sizePolicy().hasHeightForWidth())
        self.label_171.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_171, 5, 1, 1, 1)

        self.label_172 = QLabel(self.groupBox_22)
        self.label_172.setObjectName(u"label_172")
        sizePolicy3.setHeightForWidth(self.label_172.sizePolicy().hasHeightForWidth())
        self.label_172.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_172, 0, 3, 1, 1)

        self.label_173 = QLabel(self.groupBox_22)
        self.label_173.setObjectName(u"label_173")
        sizePolicy3.setHeightForWidth(self.label_173.sizePolicy().hasHeightForWidth())
        self.label_173.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_173, 4, 3, 1, 1)

        self.label_174 = QLabel(self.groupBox_22)
        self.label_174.setObjectName(u"label_174")
        sizePolicy3.setHeightForWidth(self.label_174.sizePolicy().hasHeightForWidth())
        self.label_174.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_174, 0, 1, 1, 1)

        self.label_175 = QLabel(self.groupBox_22)
        self.label_175.setObjectName(u"label_175")
        sizePolicy3.setHeightForWidth(self.label_175.sizePolicy().hasHeightForWidth())
        self.label_175.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_175, 4, 1, 1, 1)

        self.label_176 = QLabel(self.groupBox_22)
        self.label_176.setObjectName(u"label_176")
        sizePolicy3.setHeightForWidth(self.label_176.sizePolicy().hasHeightForWidth())
        self.label_176.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_176, 6, 1, 1, 1)

        self.label_177 = QLabel(self.groupBox_22)
        self.label_177.setObjectName(u"label_177")
        sizePolicy3.setHeightForWidth(self.label_177.sizePolicy().hasHeightForWidth())
        self.label_177.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_177, 5, 3, 1, 1)

        self.label_178 = QLabel(self.groupBox_22)
        self.label_178.setObjectName(u"label_178")
        sizePolicy3.setHeightForWidth(self.label_178.sizePolicy().hasHeightForWidth())
        self.label_178.setSizePolicy(sizePolicy3)

        self.gridLayout_64.addWidget(self.label_178, 6, 3, 1, 1)

        self.lineEdit_4_2_1 = QLineEdit(self.groupBox_22)
        self.lineEdit_4_2_1.setObjectName(u"lineEdit_4_2_1")
        self.lineEdit_4_2_1.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_64.addWidget(self.lineEdit_4_2_1, 0, 2, 1, 1)

        self.lineEdit_4_2_2 = QLineEdit(self.groupBox_22)
        self.lineEdit_4_2_2.setObjectName(u"lineEdit_4_2_2")
        self.lineEdit_4_2_2.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_64.addWidget(self.lineEdit_4_2_2, 4, 2, 1, 1)

        self.lineEdit_4_2_3 = QLineEdit(self.groupBox_22)
        self.lineEdit_4_2_3.setObjectName(u"lineEdit_4_2_3")
        self.lineEdit_4_2_3.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_64.addWidget(self.lineEdit_4_2_3, 5, 2, 1, 1)

        self.lineEdit_4_2_4 = QLineEdit(self.groupBox_22)
        self.lineEdit_4_2_4.setObjectName(u"lineEdit_4_2_4")
        self.lineEdit_4_2_4.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_64.addWidget(self.lineEdit_4_2_4, 6, 2, 1, 1)

        self.gridLayout_52.addWidget(self.groupBox_22, 0, 1, 1, 1)

        self.groupBox_23 = QGroupBox(self.page_5)
        self.groupBox_23.setObjectName(u"groupBox_23")
        sizePolicy7.setHeightForWidth(self.groupBox_23.sizePolicy().hasHeightForWidth())
        self.groupBox_23.setSizePolicy(sizePolicy7)
        self.groupBox_23.setFlat(False)
        self.groupBox_23.setCheckable(False)
        self.groupBox_23.setChecked(False)
        self.gridLayout_65 = QGridLayout(self.groupBox_23)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.gridLayout_65.setVerticalSpacing(0)
        self.gridLayout_65.setContentsMargins(6, 0, 6, 0)
        self.label_179 = QLabel(self.groupBox_23)
        self.label_179.setObjectName(u"label_179")
        sizePolicy3.setHeightForWidth(self.label_179.sizePolicy().hasHeightForWidth())
        self.label_179.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_179, 0, 1, 1, 1)

        self.lineEdit_4_1_4 = QLineEdit(self.groupBox_23)
        self.lineEdit_4_1_4.setObjectName(u"lineEdit_4_1_4")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.lineEdit_4_1_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_1_4.setSizePolicy(sizePolicy9)
        self.lineEdit_4_1_4.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_65.addWidget(self.lineEdit_4_1_4, 6, 2, 1, 1)

        self.label_180 = QLabel(self.groupBox_23)
        self.label_180.setObjectName(u"label_180")
        sizePolicy3.setHeightForWidth(self.label_180.sizePolicy().hasHeightForWidth())
        self.label_180.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_180, 0, 3, 1, 1)

        self.label_181 = QLabel(self.groupBox_23)
        self.label_181.setObjectName(u"label_181")
        sizePolicy3.setHeightForWidth(self.label_181.sizePolicy().hasHeightForWidth())
        self.label_181.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_181, 5, 3, 1, 1)

        self.label_182 = QLabel(self.groupBox_23)
        self.label_182.setObjectName(u"label_182")
        sizePolicy3.setHeightForWidth(self.label_182.sizePolicy().hasHeightForWidth())
        self.label_182.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_182, 6, 1, 1, 1)

        self.label_183 = QLabel(self.groupBox_23)
        self.label_183.setObjectName(u"label_183")
        sizePolicy3.setHeightForWidth(self.label_183.sizePolicy().hasHeightForWidth())
        self.label_183.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_183, 5, 1, 1, 1)

        self.label_184 = QLabel(self.groupBox_23)
        self.label_184.setObjectName(u"label_184")
        sizePolicy3.setHeightForWidth(self.label_184.sizePolicy().hasHeightForWidth())
        self.label_184.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_184, 6, 3, 1, 1)

        self.lineEdit_4_1_3 = QLineEdit(self.groupBox_23)
        self.lineEdit_4_1_3.setObjectName(u"lineEdit_4_1_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_4_1_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_1_3.setSizePolicy(sizePolicy9)
        self.lineEdit_4_1_3.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_65.addWidget(self.lineEdit_4_1_3, 5, 2, 1, 1)

        self.label_185 = QLabel(self.groupBox_23)
        self.label_185.setObjectName(u"label_185")
        sizePolicy3.setHeightForWidth(self.label_185.sizePolicy().hasHeightForWidth())
        self.label_185.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_185, 4, 3, 1, 1)

        self.lineEdit_4_1_2 = QLineEdit(self.groupBox_23)
        self.lineEdit_4_1_2.setObjectName(u"lineEdit_4_1_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_4_1_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_1_2.setSizePolicy(sizePolicy9)
        self.lineEdit_4_1_2.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_65.addWidget(self.lineEdit_4_1_2, 4, 2, 1, 1)

        self.lineEdit_4_1_1 = QLineEdit(self.groupBox_23)
        self.lineEdit_4_1_1.setObjectName(u"lineEdit_4_1_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_4_1_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_1_1.setSizePolicy(sizePolicy9)
        self.lineEdit_4_1_1.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_65.addWidget(self.lineEdit_4_1_1, 0, 2, 1, 1)

        self.label_186 = QLabel(self.groupBox_23)
        self.label_186.setObjectName(u"label_186")
        sizePolicy3.setHeightForWidth(self.label_186.sizePolicy().hasHeightForWidth())
        self.label_186.setSizePolicy(sizePolicy3)

        self.gridLayout_65.addWidget(self.label_186, 4, 1, 1, 1)

        self.gridLayout_52.addWidget(self.groupBox_23, 0, 0, 1, 1)

        self.groupBox_24 = QGroupBox(self.page_5)
        self.groupBox_24.setObjectName(u"groupBox_24")
        sizePolicy7.setHeightForWidth(self.groupBox_24.sizePolicy().hasHeightForWidth())
        self.groupBox_24.setSizePolicy(sizePolicy7)
        self.groupBox_24.setCheckable(False)
        self.groupBox_24.setChecked(False)
        self.gridLayout_66 = QGridLayout(self.groupBox_24)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.gridLayout_66.setVerticalSpacing(0)
        self.gridLayout_66.setContentsMargins(6, 0, 6, 0)
        self.label_187 = QLabel(self.groupBox_24)
        self.label_187.setObjectName(u"label_187")
        sizePolicy3.setHeightForWidth(self.label_187.sizePolicy().hasHeightForWidth())
        self.label_187.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_187, 5, 1, 1, 1)

        self.label_188 = QLabel(self.groupBox_24)
        self.label_188.setObjectName(u"label_188")
        sizePolicy3.setHeightForWidth(self.label_188.sizePolicy().hasHeightForWidth())
        self.label_188.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_188, 0, 3, 1, 1)

        self.label_189 = QLabel(self.groupBox_24)
        self.label_189.setObjectName(u"label_189")
        sizePolicy3.setHeightForWidth(self.label_189.sizePolicy().hasHeightForWidth())
        self.label_189.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_189, 4, 3, 1, 1)

        self.label_190 = QLabel(self.groupBox_24)
        self.label_190.setObjectName(u"label_190")
        sizePolicy3.setHeightForWidth(self.label_190.sizePolicy().hasHeightForWidth())
        self.label_190.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_190, 0, 1, 1, 1)

        self.label_191 = QLabel(self.groupBox_24)
        self.label_191.setObjectName(u"label_191")
        sizePolicy3.setHeightForWidth(self.label_191.sizePolicy().hasHeightForWidth())
        self.label_191.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_191, 4, 1, 1, 1)

        self.label_192 = QLabel(self.groupBox_24)
        self.label_192.setObjectName(u"label_192")
        sizePolicy3.setHeightForWidth(self.label_192.sizePolicy().hasHeightForWidth())
        self.label_192.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_192, 6, 1, 1, 1)

        self.label_193 = QLabel(self.groupBox_24)
        self.label_193.setObjectName(u"label_193")
        sizePolicy3.setHeightForWidth(self.label_193.sizePolicy().hasHeightForWidth())
        self.label_193.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_193, 5, 3, 1, 1)

        self.label_194 = QLabel(self.groupBox_24)
        self.label_194.setObjectName(u"label_194")
        sizePolicy3.setHeightForWidth(self.label_194.sizePolicy().hasHeightForWidth())
        self.label_194.setSizePolicy(sizePolicy3)

        self.gridLayout_66.addWidget(self.label_194, 6, 3, 1, 1)

        self.lineEdit_4_3_1 = QLineEdit(self.groupBox_24)
        self.lineEdit_4_3_1.setObjectName(u"lineEdit_4_3_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_4_3_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_3_1.setSizePolicy(sizePolicy9)
        self.lineEdit_4_3_1.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_66.addWidget(self.lineEdit_4_3_1, 0, 2, 1, 1)

        self.lineEdit_4_3_2 = QLineEdit(self.groupBox_24)
        self.lineEdit_4_3_2.setObjectName(u"lineEdit_4_3_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_4_3_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_3_2.setSizePolicy(sizePolicy9)
        self.lineEdit_4_3_2.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_66.addWidget(self.lineEdit_4_3_2, 4, 2, 1, 1)

        self.lineEdit_4_3_3 = QLineEdit(self.groupBox_24)
        self.lineEdit_4_3_3.setObjectName(u"lineEdit_4_3_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_4_3_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_4_3_3.setSizePolicy(sizePolicy9)
        self.lineEdit_4_3_3.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_66.addWidget(self.lineEdit_4_3_3, 5, 2, 1, 1)

        self.lineEdit_4_3_4 = QLineEdit(self.groupBox_24)
        self.lineEdit_4_3_4.setObjectName(u"lineEdit_4_3_4")
        self.lineEdit_4_3_4.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_66.addWidget(self.lineEdit_4_3_4, 6, 2, 1, 1)

        self.gridLayout_52.addWidget(self.groupBox_24, 1, 0, 1, 1)

        self.groupBox_25 = QGroupBox(self.page_5)
        self.groupBox_25.setObjectName(u"groupBox_25")
        sizePolicy7.setHeightForWidth(self.groupBox_25.sizePolicy().hasHeightForWidth())
        self.groupBox_25.setSizePolicy(sizePolicy7)
        self.groupBox_25.setCheckable(False)
        self.groupBox_25.setChecked(False)
        self.gridLayout_67 = QGridLayout(self.groupBox_25)
        self.gridLayout_67.setObjectName(u"gridLayout_67")
        self.gridLayout_67.setVerticalSpacing(0)
        self.gridLayout_67.setContentsMargins(6, 0, 6, 0)
        self.label_195 = QLabel(self.groupBox_25)
        self.label_195.setObjectName(u"label_195")
        sizePolicy3.setHeightForWidth(self.label_195.sizePolicy().hasHeightForWidth())
        self.label_195.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_195, 5, 1, 1, 1)

        self.label_196 = QLabel(self.groupBox_25)
        self.label_196.setObjectName(u"label_196")
        sizePolicy3.setHeightForWidth(self.label_196.sizePolicy().hasHeightForWidth())
        self.label_196.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_196, 0, 3, 1, 1)

        self.label_197 = QLabel(self.groupBox_25)
        self.label_197.setObjectName(u"label_197")
        sizePolicy3.setHeightForWidth(self.label_197.sizePolicy().hasHeightForWidth())
        self.label_197.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_197, 4, 3, 1, 1)

        self.label_198 = QLabel(self.groupBox_25)
        self.label_198.setObjectName(u"label_198")
        sizePolicy3.setHeightForWidth(self.label_198.sizePolicy().hasHeightForWidth())
        self.label_198.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_198, 0, 1, 1, 1)

        self.label_199 = QLabel(self.groupBox_25)
        self.label_199.setObjectName(u"label_199")
        sizePolicy3.setHeightForWidth(self.label_199.sizePolicy().hasHeightForWidth())
        self.label_199.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_199, 4, 1, 1, 1)

        self.label_200 = QLabel(self.groupBox_25)
        self.label_200.setObjectName(u"label_200")
        sizePolicy3.setHeightForWidth(self.label_200.sizePolicy().hasHeightForWidth())
        self.label_200.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_200, 6, 1, 1, 1)

        self.label_201 = QLabel(self.groupBox_25)
        self.label_201.setObjectName(u"label_201")
        sizePolicy3.setHeightForWidth(self.label_201.sizePolicy().hasHeightForWidth())
        self.label_201.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_201, 5, 3, 1, 1)

        self.label_202 = QLabel(self.groupBox_25)
        self.label_202.setObjectName(u"label_202")
        sizePolicy3.setHeightForWidth(self.label_202.sizePolicy().hasHeightForWidth())
        self.label_202.setSizePolicy(sizePolicy3)

        self.gridLayout_67.addWidget(self.label_202, 6, 3, 1, 1)

        self.lineEdit_4_4_1 = QLineEdit(self.groupBox_25)
        self.lineEdit_4_4_1.setObjectName(u"lineEdit_4_4_1")
        self.lineEdit_4_4_1.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_67.addWidget(self.lineEdit_4_4_1, 0, 2, 1, 1)

        self.lineEdit_4_4_2 = QLineEdit(self.groupBox_25)
        self.lineEdit_4_4_2.setObjectName(u"lineEdit_4_4_2")
        self.lineEdit_4_4_2.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_67.addWidget(self.lineEdit_4_4_2, 4, 2, 1, 1)

        self.lineEdit_4_4_3 = QLineEdit(self.groupBox_25)
        self.lineEdit_4_4_3.setObjectName(u"lineEdit_4_4_3")
        self.lineEdit_4_4_3.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_67.addWidget(self.lineEdit_4_4_3, 5, 2, 1, 1)

        self.lineEdit_4_4_4 = QLineEdit(self.groupBox_25)
        self.lineEdit_4_4_4.setObjectName(u"lineEdit_4_4_4")
        self.lineEdit_4_4_4.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_67.addWidget(self.lineEdit_4_4_4, 6, 2, 1, 1)

        self.gridLayout_52.addWidget(self.groupBox_25, 1, 1, 1, 1)

        self.gridLayout_51.addLayout(self.gridLayout_52, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_5)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        sizePolicy8.setHeightForWidth(self.page_8.sizePolicy().hasHeightForWidth())
        self.page_8.setSizePolicy(sizePolicy8)
        self.gridLayout_68 = QGridLayout(self.page_8)
        self.gridLayout_68.setSpacing(0)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.gridLayout_68.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_69 = QGridLayout()
        self.gridLayout_69.setSpacing(0)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.groupBox_35 = QGroupBox(self.page_8)
        self.groupBox_35.setObjectName(u"groupBox_35")
        sizePolicy7.setHeightForWidth(self.groupBox_35.sizePolicy().hasHeightForWidth())
        self.groupBox_35.setSizePolicy(sizePolicy7)
        self.groupBox_35.setFont(font)
        self.groupBox_35.setCheckable(False)
        self.groupBox_35.setChecked(False)
        self.gridLayout_70 = QGridLayout(self.groupBox_35)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.gridLayout_70.setHorizontalSpacing(0)
        self.gridLayout_70.setVerticalSpacing(6)
        self.gridLayout_70.setContentsMargins(0, 6, 0, 6)
        self.label_283 = QLabel(self.groupBox_35)
        self.label_283.setObjectName(u"label_283")
        sizePolicy3.setHeightForWidth(self.label_283.sizePolicy().hasHeightForWidth())
        self.label_283.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_283, 5, 1, 1, 1)

        self.label_284 = QLabel(self.groupBox_35)
        self.label_284.setObjectName(u"label_284")
        sizePolicy3.setHeightForWidth(self.label_284.sizePolicy().hasHeightForWidth())
        self.label_284.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_284, 0, 3, 1, 1)

        self.label_285 = QLabel(self.groupBox_35)
        self.label_285.setObjectName(u"label_285")
        sizePolicy3.setHeightForWidth(self.label_285.sizePolicy().hasHeightForWidth())
        self.label_285.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_285, 4, 3, 1, 1)

        self.label_286 = QLabel(self.groupBox_35)
        self.label_286.setObjectName(u"label_286")
        sizePolicy3.setHeightForWidth(self.label_286.sizePolicy().hasHeightForWidth())
        self.label_286.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_286, 0, 1, 1, 1)

        self.label_287 = QLabel(self.groupBox_35)
        self.label_287.setObjectName(u"label_287")
        sizePolicy3.setHeightForWidth(self.label_287.sizePolicy().hasHeightForWidth())
        self.label_287.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_287, 4, 1, 1, 1)

        self.label_288 = QLabel(self.groupBox_35)
        self.label_288.setObjectName(u"label_288")
        sizePolicy3.setHeightForWidth(self.label_288.sizePolicy().hasHeightForWidth())
        self.label_288.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_288, 6, 1, 1, 1)

        self.label_289 = QLabel(self.groupBox_35)
        self.label_289.setObjectName(u"label_289")
        sizePolicy3.setHeightForWidth(self.label_289.sizePolicy().hasHeightForWidth())
        self.label_289.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_289, 5, 3, 1, 1)

        self.label_290 = QLabel(self.groupBox_35)
        self.label_290.setObjectName(u"label_290")
        sizePolicy3.setHeightForWidth(self.label_290.sizePolicy().hasHeightForWidth())
        self.label_290.setSizePolicy(sizePolicy3)

        self.gridLayout_70.addWidget(self.label_290, 6, 3, 1, 1)

        self.lineEdit_9_4_1 = QLineEdit(self.groupBox_35)
        self.lineEdit_9_4_1.setObjectName(u"lineEdit_9_4_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_4_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_4_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_4_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_4_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_70.addWidget(self.lineEdit_9_4_1, 0, 2, 1, 1)

        self.lineEdit_9_4_2 = QLineEdit(self.groupBox_35)
        self.lineEdit_9_4_2.setObjectName(u"lineEdit_9_4_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_4_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_4_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_4_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_4_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_70.addWidget(self.lineEdit_9_4_2, 4, 2, 1, 1)

        self.lineEdit_9_4_3 = QLineEdit(self.groupBox_35)
        self.lineEdit_9_4_3.setObjectName(u"lineEdit_9_4_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_4_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_4_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_4_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_4_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_70.addWidget(self.lineEdit_9_4_3, 5, 2, 1, 1)

        self.lineEdit_9_4_4 = QLineEdit(self.groupBox_35)
        self.lineEdit_9_4_4.setObjectName(u"lineEdit_9_4_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_4_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_4_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_4_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_4_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_70.addWidget(self.lineEdit_9_4_4, 6, 2, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_35, 1, 0, 1, 1)

        self.groupBox_36 = QGroupBox(self.page_8)
        self.groupBox_36.setObjectName(u"groupBox_36")
        sizePolicy7.setHeightForWidth(self.groupBox_36.sizePolicy().hasHeightForWidth())
        self.groupBox_36.setSizePolicy(sizePolicy7)
        self.groupBox_36.setFont(font)
        self.groupBox_36.setFlat(False)
        self.groupBox_36.setCheckable(False)
        self.groupBox_36.setChecked(False)
        self.gridLayout_71 = QGridLayout(self.groupBox_36)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.gridLayout_71.setHorizontalSpacing(0)
        self.gridLayout_71.setVerticalSpacing(6)
        self.gridLayout_71.setContentsMargins(0, 6, 0, 6)
        self.label_291 = QLabel(self.groupBox_36)
        self.label_291.setObjectName(u"label_291")
        sizePolicy3.setHeightForWidth(self.label_291.sizePolicy().hasHeightForWidth())
        self.label_291.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_291, 0, 1, 1, 1)

        self.lineEdit_9_8_4 = QLineEdit(self.groupBox_36)
        self.lineEdit_9_8_4.setObjectName(u"lineEdit_9_8_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_8_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_8_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_8_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_8_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_71.addWidget(self.lineEdit_9_8_4, 6, 2, 1, 1)

        self.label_292 = QLabel(self.groupBox_36)
        self.label_292.setObjectName(u"label_292")
        sizePolicy3.setHeightForWidth(self.label_292.sizePolicy().hasHeightForWidth())
        self.label_292.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_292, 0, 3, 1, 1)

        self.label_293 = QLabel(self.groupBox_36)
        self.label_293.setObjectName(u"label_293")
        sizePolicy3.setHeightForWidth(self.label_293.sizePolicy().hasHeightForWidth())
        self.label_293.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_293, 5, 3, 1, 1)

        self.label_294 = QLabel(self.groupBox_36)
        self.label_294.setObjectName(u"label_294")
        sizePolicy3.setHeightForWidth(self.label_294.sizePolicy().hasHeightForWidth())
        self.label_294.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_294, 6, 1, 1, 1)

        self.label_295 = QLabel(self.groupBox_36)
        self.label_295.setObjectName(u"label_295")
        sizePolicy3.setHeightForWidth(self.label_295.sizePolicy().hasHeightForWidth())
        self.label_295.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_295, 5, 1, 1, 1)

        self.label_296 = QLabel(self.groupBox_36)
        self.label_296.setObjectName(u"label_296")
        sizePolicy3.setHeightForWidth(self.label_296.sizePolicy().hasHeightForWidth())
        self.label_296.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_296, 6, 3, 1, 1)

        self.lineEdit_9_8_3 = QLineEdit(self.groupBox_36)
        self.lineEdit_9_8_3.setObjectName(u"lineEdit_9_8_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_8_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_8_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_8_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_8_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_71.addWidget(self.lineEdit_9_8_3, 5, 2, 1, 1)

        self.label_297 = QLabel(self.groupBox_36)
        self.label_297.setObjectName(u"label_297")
        sizePolicy3.setHeightForWidth(self.label_297.sizePolicy().hasHeightForWidth())
        self.label_297.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_297, 4, 3, 1, 1)

        self.lineEdit_9_8_2 = QLineEdit(self.groupBox_36)
        self.lineEdit_9_8_2.setObjectName(u"lineEdit_9_8_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_8_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_8_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_8_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_8_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_71.addWidget(self.lineEdit_9_8_2, 4, 2, 1, 1)

        self.lineEdit_9_8_1 = QLineEdit(self.groupBox_36)
        self.lineEdit_9_8_1.setObjectName(u"lineEdit_9_8_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_8_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_8_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_8_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_8_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_71.addWidget(self.lineEdit_9_8_1, 0, 2, 1, 1)

        self.label_298 = QLabel(self.groupBox_36)
        self.label_298.setObjectName(u"label_298")
        sizePolicy3.setHeightForWidth(self.label_298.sizePolicy().hasHeightForWidth())
        self.label_298.setSizePolicy(sizePolicy3)

        self.gridLayout_71.addWidget(self.label_298, 4, 1, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_36, 2, 1, 1, 1)

        self.groupBox_37 = QGroupBox(self.page_8)
        self.groupBox_37.setObjectName(u"groupBox_37")
        sizePolicy7.setHeightForWidth(self.groupBox_37.sizePolicy().hasHeightForWidth())
        self.groupBox_37.setSizePolicy(sizePolicy7)
        self.groupBox_37.setFont(font)
        self.groupBox_37.setFlat(False)
        self.groupBox_37.setCheckable(False)
        self.groupBox_37.setChecked(False)
        self.gridLayout_72 = QGridLayout(self.groupBox_37)
        self.gridLayout_72.setObjectName(u"gridLayout_72")
        self.gridLayout_72.setHorizontalSpacing(0)
        self.gridLayout_72.setVerticalSpacing(6)
        self.gridLayout_72.setContentsMargins(0, 6, 0, 6)
        self.label_299 = QLabel(self.groupBox_37)
        self.label_299.setObjectName(u"label_299")
        sizePolicy3.setHeightForWidth(self.label_299.sizePolicy().hasHeightForWidth())
        self.label_299.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_299, 0, 1, 1, 1)

        self.lineEdit_9_9_4 = QLineEdit(self.groupBox_37)
        self.lineEdit_9_9_4.setObjectName(u"lineEdit_9_9_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_9_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_9_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_9_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_9_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_72.addWidget(self.lineEdit_9_9_4, 6, 2, 1, 1)

        self.label_300 = QLabel(self.groupBox_37)
        self.label_300.setObjectName(u"label_300")
        sizePolicy3.setHeightForWidth(self.label_300.sizePolicy().hasHeightForWidth())
        self.label_300.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_300, 0, 3, 1, 1)

        self.label_301 = QLabel(self.groupBox_37)
        self.label_301.setObjectName(u"label_301")
        sizePolicy3.setHeightForWidth(self.label_301.sizePolicy().hasHeightForWidth())
        self.label_301.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_301, 5, 3, 1, 1)

        self.label_302 = QLabel(self.groupBox_37)
        self.label_302.setObjectName(u"label_302")
        sizePolicy3.setHeightForWidth(self.label_302.sizePolicy().hasHeightForWidth())
        self.label_302.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_302, 6, 1, 1, 1)

        self.label_303 = QLabel(self.groupBox_37)
        self.label_303.setObjectName(u"label_303")
        sizePolicy3.setHeightForWidth(self.label_303.sizePolicy().hasHeightForWidth())
        self.label_303.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_303, 5, 1, 1, 1)

        self.label_304 = QLabel(self.groupBox_37)
        self.label_304.setObjectName(u"label_304")
        sizePolicy3.setHeightForWidth(self.label_304.sizePolicy().hasHeightForWidth())
        self.label_304.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_304, 6, 3, 1, 1)

        self.lineEdit_9_9_3 = QLineEdit(self.groupBox_37)
        self.lineEdit_9_9_3.setObjectName(u"lineEdit_9_9_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_9_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_9_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_9_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_9_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_72.addWidget(self.lineEdit_9_9_3, 5, 2, 1, 1)

        self.label_305 = QLabel(self.groupBox_37)
        self.label_305.setObjectName(u"label_305")
        sizePolicy3.setHeightForWidth(self.label_305.sizePolicy().hasHeightForWidth())
        self.label_305.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_305, 4, 3, 1, 1)

        self.lineEdit_9_9_2 = QLineEdit(self.groupBox_37)
        self.lineEdit_9_9_2.setObjectName(u"lineEdit_9_9_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_9_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_9_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_9_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_9_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_72.addWidget(self.lineEdit_9_9_2, 4, 2, 1, 1)

        self.lineEdit_9_9_1 = QLineEdit(self.groupBox_37)
        self.lineEdit_9_9_1.setObjectName(u"lineEdit_9_9_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_9_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_9_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_9_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_9_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_72.addWidget(self.lineEdit_9_9_1, 0, 2, 1, 1)

        self.label_306 = QLabel(self.groupBox_37)
        self.label_306.setObjectName(u"label_306")
        sizePolicy3.setHeightForWidth(self.label_306.sizePolicy().hasHeightForWidth())
        self.label_306.setSizePolicy(sizePolicy3)

        self.gridLayout_72.addWidget(self.label_306, 4, 1, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_37, 2, 2, 1, 1)

        self.groupBox_38 = QGroupBox(self.page_8)
        self.groupBox_38.setObjectName(u"groupBox_38")
        sizePolicy7.setHeightForWidth(self.groupBox_38.sizePolicy().hasHeightForWidth())
        self.groupBox_38.setSizePolicy(sizePolicy7)
        self.groupBox_38.setFont(font)
        self.groupBox_38.setFlat(False)
        self.groupBox_38.setCheckable(False)
        self.groupBox_38.setChecked(False)
        self.gridLayout_73 = QGridLayout(self.groupBox_38)
        self.gridLayout_73.setObjectName(u"gridLayout_73")
        self.gridLayout_73.setHorizontalSpacing(0)
        self.gridLayout_73.setVerticalSpacing(6)
        self.gridLayout_73.setContentsMargins(0, 6, 0, 6)
        self.label_307 = QLabel(self.groupBox_38)
        self.label_307.setObjectName(u"label_307")
        sizePolicy3.setHeightForWidth(self.label_307.sizePolicy().hasHeightForWidth())
        self.label_307.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_307, 0, 1, 1, 1)

        self.lineEdit_9_7_4 = QLineEdit(self.groupBox_38)
        self.lineEdit_9_7_4.setObjectName(u"lineEdit_9_7_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_7_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_7_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_7_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_7_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_73.addWidget(self.lineEdit_9_7_4, 6, 2, 1, 1)

        self.label_308 = QLabel(self.groupBox_38)
        self.label_308.setObjectName(u"label_308")
        sizePolicy3.setHeightForWidth(self.label_308.sizePolicy().hasHeightForWidth())
        self.label_308.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_308, 0, 3, 1, 1)

        self.label_309 = QLabel(self.groupBox_38)
        self.label_309.setObjectName(u"label_309")
        sizePolicy3.setHeightForWidth(self.label_309.sizePolicy().hasHeightForWidth())
        self.label_309.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_309, 5, 3, 1, 1)

        self.label_310 = QLabel(self.groupBox_38)
        self.label_310.setObjectName(u"label_310")
        sizePolicy3.setHeightForWidth(self.label_310.sizePolicy().hasHeightForWidth())
        self.label_310.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_310, 6, 1, 1, 1)

        self.label_311 = QLabel(self.groupBox_38)
        self.label_311.setObjectName(u"label_311")
        sizePolicy3.setHeightForWidth(self.label_311.sizePolicy().hasHeightForWidth())
        self.label_311.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_311, 5, 1, 1, 1)

        self.label_312 = QLabel(self.groupBox_38)
        self.label_312.setObjectName(u"label_312")
        sizePolicy3.setHeightForWidth(self.label_312.sizePolicy().hasHeightForWidth())
        self.label_312.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_312, 6, 3, 1, 1)

        self.lineEdit_9_7_3 = QLineEdit(self.groupBox_38)
        self.lineEdit_9_7_3.setObjectName(u"lineEdit_9_7_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_7_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_7_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_7_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_7_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_73.addWidget(self.lineEdit_9_7_3, 5, 2, 1, 1)

        self.label_313 = QLabel(self.groupBox_38)
        self.label_313.setObjectName(u"label_313")
        sizePolicy3.setHeightForWidth(self.label_313.sizePolicy().hasHeightForWidth())
        self.label_313.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_313, 4, 3, 1, 1)

        self.lineEdit_9_7_2 = QLineEdit(self.groupBox_38)
        self.lineEdit_9_7_2.setObjectName(u"lineEdit_9_7_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_7_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_7_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_7_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_7_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_73.addWidget(self.lineEdit_9_7_2, 4, 2, 1, 1)

        self.lineEdit_9_7_1 = QLineEdit(self.groupBox_38)
        self.lineEdit_9_7_1.setObjectName(u"lineEdit_9_7_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_7_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_7_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_7_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_7_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_73.addWidget(self.lineEdit_9_7_1, 0, 2, 1, 1)

        self.label_314 = QLabel(self.groupBox_38)
        self.label_314.setObjectName(u"label_314")
        sizePolicy3.setHeightForWidth(self.label_314.sizePolicy().hasHeightForWidth())
        self.label_314.setSizePolicy(sizePolicy3)

        self.gridLayout_73.addWidget(self.label_314, 4, 1, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_38, 2, 0, 1, 1)

        self.groupBox_39 = QGroupBox(self.page_8)
        self.groupBox_39.setObjectName(u"groupBox_39")
        sizePolicy7.setHeightForWidth(self.groupBox_39.sizePolicy().hasHeightForWidth())
        self.groupBox_39.setSizePolicy(sizePolicy7)
        self.groupBox_39.setFont(font)
        self.groupBox_39.setFlat(False)
        self.groupBox_39.setCheckable(False)
        self.groupBox_39.setChecked(False)
        self.gridLayout_74 = QGridLayout(self.groupBox_39)
        self.gridLayout_74.setObjectName(u"gridLayout_74")
        self.gridLayout_74.setHorizontalSpacing(0)
        self.gridLayout_74.setVerticalSpacing(6)
        self.gridLayout_74.setContentsMargins(0, 6, 0, 6)
        self.label_315 = QLabel(self.groupBox_39)
        self.label_315.setObjectName(u"label_315")
        sizePolicy3.setHeightForWidth(self.label_315.sizePolicy().hasHeightForWidth())
        self.label_315.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_315, 5, 1, 1, 1)

        self.label_316 = QLabel(self.groupBox_39)
        self.label_316.setObjectName(u"label_316")
        sizePolicy3.setHeightForWidth(self.label_316.sizePolicy().hasHeightForWidth())
        self.label_316.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_316, 0, 3, 1, 1)

        self.label_317 = QLabel(self.groupBox_39)
        self.label_317.setObjectName(u"label_317")
        sizePolicy3.setHeightForWidth(self.label_317.sizePolicy().hasHeightForWidth())
        self.label_317.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_317, 4, 3, 1, 1)

        self.label_318 = QLabel(self.groupBox_39)
        self.label_318.setObjectName(u"label_318")
        sizePolicy3.setHeightForWidth(self.label_318.sizePolicy().hasHeightForWidth())
        self.label_318.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_318, 0, 1, 1, 1)

        self.label_319 = QLabel(self.groupBox_39)
        self.label_319.setObjectName(u"label_319")
        sizePolicy3.setHeightForWidth(self.label_319.sizePolicy().hasHeightForWidth())
        self.label_319.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_319, 4, 1, 1, 1)

        self.label_320 = QLabel(self.groupBox_39)
        self.label_320.setObjectName(u"label_320")
        sizePolicy3.setHeightForWidth(self.label_320.sizePolicy().hasHeightForWidth())
        self.label_320.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_320, 6, 1, 1, 1)

        self.label_321 = QLabel(self.groupBox_39)
        self.label_321.setObjectName(u"label_321")
        sizePolicy3.setHeightForWidth(self.label_321.sizePolicy().hasHeightForWidth())
        self.label_321.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_321, 5, 3, 1, 1)

        self.label_322 = QLabel(self.groupBox_39)
        self.label_322.setObjectName(u"label_322")
        sizePolicy3.setHeightForWidth(self.label_322.sizePolicy().hasHeightForWidth())
        self.label_322.setSizePolicy(sizePolicy3)

        self.gridLayout_74.addWidget(self.label_322, 6, 3, 1, 1)

        self.lineEdit_9_2_1 = QLineEdit(self.groupBox_39)
        self.lineEdit_9_2_1.setObjectName(u"lineEdit_9_2_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_2_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_2_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_2_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_2_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_74.addWidget(self.lineEdit_9_2_1, 0, 2, 1, 1)

        self.lineEdit_9_2_2 = QLineEdit(self.groupBox_39)
        self.lineEdit_9_2_2.setObjectName(u"lineEdit_9_2_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_2_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_2_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_2_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_2_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_74.addWidget(self.lineEdit_9_2_2, 4, 2, 1, 1)

        self.lineEdit_9_2_3 = QLineEdit(self.groupBox_39)
        self.lineEdit_9_2_3.setObjectName(u"lineEdit_9_2_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_2_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_2_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_2_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_2_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_74.addWidget(self.lineEdit_9_2_3, 5, 2, 1, 1)

        self.lineEdit_9_2_4 = QLineEdit(self.groupBox_39)
        self.lineEdit_9_2_4.setObjectName(u"lineEdit_9_2_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_2_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_2_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_2_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_2_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_74.addWidget(self.lineEdit_9_2_4, 6, 2, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_39, 0, 1, 1, 1)

        self.groupBox_40 = QGroupBox(self.page_8)
        self.groupBox_40.setObjectName(u"groupBox_40")
        sizePolicy7.setHeightForWidth(self.groupBox_40.sizePolicy().hasHeightForWidth())
        self.groupBox_40.setSizePolicy(sizePolicy7)
        self.groupBox_40.setFont(font)
        self.groupBox_40.setFlat(False)
        self.groupBox_40.setCheckable(False)
        self.groupBox_40.setChecked(False)
        self.gridLayout_75 = QGridLayout(self.groupBox_40)
        self.gridLayout_75.setObjectName(u"gridLayout_75")
        self.gridLayout_75.setHorizontalSpacing(0)
        self.gridLayout_75.setVerticalSpacing(6)
        self.gridLayout_75.setContentsMargins(0, 6, 0, 6)
        self.label_323 = QLabel(self.groupBox_40)
        self.label_323.setObjectName(u"label_323")
        sizePolicy3.setHeightForWidth(self.label_323.sizePolicy().hasHeightForWidth())
        self.label_323.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_323, 5, 1, 1, 1)

        self.label_324 = QLabel(self.groupBox_40)
        self.label_324.setObjectName(u"label_324")
        sizePolicy3.setHeightForWidth(self.label_324.sizePolicy().hasHeightForWidth())
        self.label_324.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_324, 0, 1, 1, 1)

        self.label_325 = QLabel(self.groupBox_40)
        self.label_325.setObjectName(u"label_325")
        sizePolicy3.setHeightForWidth(self.label_325.sizePolicy().hasHeightForWidth())
        self.label_325.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_325, 4, 3, 1, 1)

        self.lineEdit_9_1_2 = QLineEdit(self.groupBox_40)
        self.lineEdit_9_1_2.setObjectName(u"lineEdit_9_1_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_1_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_1_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_1_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_1_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_75.addWidget(self.lineEdit_9_1_2, 4, 2, 1, 1)

        self.label_326 = QLabel(self.groupBox_40)
        self.label_326.setObjectName(u"label_326")
        sizePolicy3.setHeightForWidth(self.label_326.sizePolicy().hasHeightForWidth())
        self.label_326.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_326, 4, 1, 1, 1)

        self.lineEdit_9_1_4 = QLineEdit(self.groupBox_40)
        self.lineEdit_9_1_4.setObjectName(u"lineEdit_9_1_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_1_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_1_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_1_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_1_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_75.addWidget(self.lineEdit_9_1_4, 6, 2, 1, 1)

        self.label_327 = QLabel(self.groupBox_40)
        self.label_327.setObjectName(u"label_327")
        sizePolicy3.setHeightForWidth(self.label_327.sizePolicy().hasHeightForWidth())
        self.label_327.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_327, 0, 3, 1, 1)

        self.label_328 = QLabel(self.groupBox_40)
        self.label_328.setObjectName(u"label_328")
        sizePolicy3.setHeightForWidth(self.label_328.sizePolicy().hasHeightForWidth())
        self.label_328.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_328, 5, 3, 1, 1)

        self.label_329 = QLabel(self.groupBox_40)
        self.label_329.setObjectName(u"label_329")
        sizePolicy3.setHeightForWidth(self.label_329.sizePolicy().hasHeightForWidth())
        self.label_329.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_329, 6, 1, 1, 1)

        self.lineEdit_9_1_3 = QLineEdit(self.groupBox_40)
        self.lineEdit_9_1_3.setObjectName(u"lineEdit_9_1_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_1_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_1_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_1_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_1_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_75.addWidget(self.lineEdit_9_1_3, 5, 2, 1, 1)

        self.label_330 = QLabel(self.groupBox_40)
        self.label_330.setObjectName(u"label_330")
        sizePolicy3.setHeightForWidth(self.label_330.sizePolicy().hasHeightForWidth())
        self.label_330.setSizePolicy(sizePolicy3)

        self.gridLayout_75.addWidget(self.label_330, 6, 3, 1, 1)

        self.lineEdit_9_1_1 = QLineEdit(self.groupBox_40)
        self.lineEdit_9_1_1.setObjectName(u"lineEdit_9_1_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_1_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_1_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_1_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_1_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_75.addWidget(self.lineEdit_9_1_1, 0, 2, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_40, 0, 0, 1, 1)

        self.groupBox_41 = QGroupBox(self.page_8)
        self.groupBox_41.setObjectName(u"groupBox_41")
        sizePolicy7.setHeightForWidth(self.groupBox_41.sizePolicy().hasHeightForWidth())
        self.groupBox_41.setSizePolicy(sizePolicy7)
        self.groupBox_41.setFont(font)
        self.groupBox_41.setFlat(False)
        self.groupBox_41.setCheckable(False)
        self.groupBox_41.setChecked(False)
        self.gridLayout_76 = QGridLayout(self.groupBox_41)
        self.gridLayout_76.setObjectName(u"gridLayout_76")
        self.gridLayout_76.setHorizontalSpacing(0)
        self.gridLayout_76.setVerticalSpacing(6)
        self.gridLayout_76.setContentsMargins(0, 6, 0, 6)
        self.label_335 = QLabel(self.groupBox_41)
        self.label_335.setObjectName(u"label_335")
        sizePolicy3.setHeightForWidth(self.label_335.sizePolicy().hasHeightForWidth())
        self.label_335.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_335, 5, 1, 1, 1)

        self.lineEdit_9_6_1 = QLineEdit(self.groupBox_41)
        self.lineEdit_9_6_1.setObjectName(u"lineEdit_9_6_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_6_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_6_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_6_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_6_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_76.addWidget(self.lineEdit_9_6_1, 0, 2, 1, 1)

        self.label_333 = QLabel(self.groupBox_41)
        self.label_333.setObjectName(u"label_333")
        sizePolicy3.setHeightForWidth(self.label_333.sizePolicy().hasHeightForWidth())
        self.label_333.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_333, 5, 3, 1, 1)

        self.label_331 = QLabel(self.groupBox_41)
        self.label_331.setObjectName(u"label_331")
        sizePolicy3.setHeightForWidth(self.label_331.sizePolicy().hasHeightForWidth())
        self.label_331.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_331, 0, 1, 1, 1)

        self.lineEdit_9_6_4 = QLineEdit(self.groupBox_41)
        self.lineEdit_9_6_4.setObjectName(u"lineEdit_9_6_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_6_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_6_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_6_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_6_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_76.addWidget(self.lineEdit_9_6_4, 6, 2, 1, 1)

        self.lineEdit_9_6_2 = QLineEdit(self.groupBox_41)
        self.lineEdit_9_6_2.setObjectName(u"lineEdit_9_6_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_6_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_6_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_6_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_6_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_76.addWidget(self.lineEdit_9_6_2, 4, 2, 1, 1)

        self.label_334 = QLabel(self.groupBox_41)
        self.label_334.setObjectName(u"label_334")
        sizePolicy3.setHeightForWidth(self.label_334.sizePolicy().hasHeightForWidth())
        self.label_334.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_334, 6, 1, 1, 1)

        self.label_332 = QLabel(self.groupBox_41)
        self.label_332.setObjectName(u"label_332")
        sizePolicy3.setHeightForWidth(self.label_332.sizePolicy().hasHeightForWidth())
        self.label_332.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_332, 0, 3, 1, 1)

        self.label_338 = QLabel(self.groupBox_41)
        self.label_338.setObjectName(u"label_338")
        sizePolicy3.setHeightForWidth(self.label_338.sizePolicy().hasHeightForWidth())
        self.label_338.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_338, 4, 1, 1, 1)

        self.lineEdit_9_6_3 = QLineEdit(self.groupBox_41)
        self.lineEdit_9_6_3.setObjectName(u"lineEdit_9_6_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_6_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_6_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_6_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_6_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_76.addWidget(self.lineEdit_9_6_3, 5, 2, 1, 1)

        self.label_337 = QLabel(self.groupBox_41)
        self.label_337.setObjectName(u"label_337")
        sizePolicy3.setHeightForWidth(self.label_337.sizePolicy().hasHeightForWidth())
        self.label_337.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_337, 4, 3, 1, 1)

        self.label_336 = QLabel(self.groupBox_41)
        self.label_336.setObjectName(u"label_336")
        sizePolicy3.setHeightForWidth(self.label_336.sizePolicy().hasHeightForWidth())
        self.label_336.setSizePolicy(sizePolicy3)

        self.gridLayout_76.addWidget(self.label_336, 6, 3, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_41, 1, 2, 1, 1)

        self.groupBox_42 = QGroupBox(self.page_8)
        self.groupBox_42.setObjectName(u"groupBox_42")
        sizePolicy7.setHeightForWidth(self.groupBox_42.sizePolicy().hasHeightForWidth())
        self.groupBox_42.setSizePolicy(sizePolicy7)
        self.groupBox_42.setFont(font)
        self.groupBox_42.setCheckable(False)
        self.groupBox_42.setChecked(False)
        self.gridLayout_77 = QGridLayout(self.groupBox_42)
        self.gridLayout_77.setObjectName(u"gridLayout_77")
        self.gridLayout_77.setHorizontalSpacing(0)
        self.gridLayout_77.setVerticalSpacing(6)
        self.gridLayout_77.setContentsMargins(0, 6, 0, 6)
        self.label_339 = QLabel(self.groupBox_42)
        self.label_339.setObjectName(u"label_339")
        sizePolicy3.setHeightForWidth(self.label_339.sizePolicy().hasHeightForWidth())
        self.label_339.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_339, 5, 1, 1, 1)

        self.label_340 = QLabel(self.groupBox_42)
        self.label_340.setObjectName(u"label_340")
        sizePolicy3.setHeightForWidth(self.label_340.sizePolicy().hasHeightForWidth())
        self.label_340.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_340, 0, 3, 1, 1)

        self.label_341 = QLabel(self.groupBox_42)
        self.label_341.setObjectName(u"label_341")
        sizePolicy3.setHeightForWidth(self.label_341.sizePolicy().hasHeightForWidth())
        self.label_341.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_341, 4, 3, 1, 1)

        self.label_342 = QLabel(self.groupBox_42)
        self.label_342.setObjectName(u"label_342")
        sizePolicy3.setHeightForWidth(self.label_342.sizePolicy().hasHeightForWidth())
        self.label_342.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_342, 0, 1, 1, 1)

        self.label_343 = QLabel(self.groupBox_42)
        self.label_343.setObjectName(u"label_343")
        sizePolicy3.setHeightForWidth(self.label_343.sizePolicy().hasHeightForWidth())
        self.label_343.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_343, 4, 1, 1, 1)

        self.label_344 = QLabel(self.groupBox_42)
        self.label_344.setObjectName(u"label_344")
        sizePolicy3.setHeightForWidth(self.label_344.sizePolicy().hasHeightForWidth())
        self.label_344.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_344, 6, 1, 1, 1)

        self.label_345 = QLabel(self.groupBox_42)
        self.label_345.setObjectName(u"label_345")
        sizePolicy3.setHeightForWidth(self.label_345.sizePolicy().hasHeightForWidth())
        self.label_345.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_345, 5, 3, 1, 1)

        self.label_346 = QLabel(self.groupBox_42)
        self.label_346.setObjectName(u"label_346")
        sizePolicy3.setHeightForWidth(self.label_346.sizePolicy().hasHeightForWidth())
        self.label_346.setSizePolicy(sizePolicy3)

        self.gridLayout_77.addWidget(self.label_346, 6, 3, 1, 1)

        self.lineEdit_9_5_1 = QLineEdit(self.groupBox_42)
        self.lineEdit_9_5_1.setObjectName(u"lineEdit_9_5_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_5_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_5_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_5_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_5_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_77.addWidget(self.lineEdit_9_5_1, 0, 2, 1, 1)

        self.lineEdit_9_5_2 = QLineEdit(self.groupBox_42)
        self.lineEdit_9_5_2.setObjectName(u"lineEdit_9_5_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_5_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_5_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_5_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_5_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_77.addWidget(self.lineEdit_9_5_2, 4, 2, 1, 1)

        self.lineEdit_9_5_3 = QLineEdit(self.groupBox_42)
        self.lineEdit_9_5_3.setObjectName(u"lineEdit_9_5_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_5_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_5_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_5_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_5_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_77.addWidget(self.lineEdit_9_5_3, 5, 2, 1, 1)

        self.lineEdit_9_5_4 = QLineEdit(self.groupBox_42)
        self.lineEdit_9_5_4.setObjectName(u"lineEdit_9_5_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_5_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_5_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_5_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_5_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_77.addWidget(self.lineEdit_9_5_4, 6, 2, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_42, 1, 1, 1, 1)

        self.groupBox_43 = QGroupBox(self.page_8)
        self.groupBox_43.setObjectName(u"groupBox_43")
        sizePolicy7.setHeightForWidth(self.groupBox_43.sizePolicy().hasHeightForWidth())
        self.groupBox_43.setSizePolicy(sizePolicy7)
        self.groupBox_43.setFont(font)
        self.groupBox_43.setFlat(False)
        self.groupBox_43.setCheckable(False)
        self.groupBox_43.setChecked(False)
        self.gridLayout_78 = QGridLayout(self.groupBox_43)
        self.gridLayout_78.setObjectName(u"gridLayout_78")
        self.gridLayout_78.setHorizontalSpacing(0)
        self.gridLayout_78.setVerticalSpacing(6)
        self.gridLayout_78.setContentsMargins(0, 6, 0, 6)
        self.label_347 = QLabel(self.groupBox_43)
        self.label_347.setObjectName(u"label_347")
        sizePolicy3.setHeightForWidth(self.label_347.sizePolicy().hasHeightForWidth())
        self.label_347.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_347, 0, 1, 1, 1)

        self.lineEdit_9_3_4 = QLineEdit(self.groupBox_43)
        self.lineEdit_9_3_4.setObjectName(u"lineEdit_9_3_4")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_3_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_3_4.setSizePolicy(sizePolicy9)
        self.lineEdit_9_3_4.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_3_4.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_78.addWidget(self.lineEdit_9_3_4, 6, 2, 1, 1)

        self.label_348 = QLabel(self.groupBox_43)
        self.label_348.setObjectName(u"label_348")
        sizePolicy3.setHeightForWidth(self.label_348.sizePolicy().hasHeightForWidth())
        self.label_348.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_348, 0, 3, 1, 1)

        self.label_349 = QLabel(self.groupBox_43)
        self.label_349.setObjectName(u"label_349")
        sizePolicy3.setHeightForWidth(self.label_349.sizePolicy().hasHeightForWidth())
        self.label_349.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_349, 5, 3, 1, 1)

        self.label_350 = QLabel(self.groupBox_43)
        self.label_350.setObjectName(u"label_350")
        sizePolicy3.setHeightForWidth(self.label_350.sizePolicy().hasHeightForWidth())
        self.label_350.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_350, 6, 1, 1, 1)

        self.label_351 = QLabel(self.groupBox_43)
        self.label_351.setObjectName(u"label_351")
        sizePolicy3.setHeightForWidth(self.label_351.sizePolicy().hasHeightForWidth())
        self.label_351.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_351, 5, 1, 1, 1)

        self.label_352 = QLabel(self.groupBox_43)
        self.label_352.setObjectName(u"label_352")
        sizePolicy3.setHeightForWidth(self.label_352.sizePolicy().hasHeightForWidth())
        self.label_352.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_352, 6, 3, 1, 1)

        self.lineEdit_9_3_3 = QLineEdit(self.groupBox_43)
        self.lineEdit_9_3_3.setObjectName(u"lineEdit_9_3_3")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_3_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_3_3.setSizePolicy(sizePolicy9)
        self.lineEdit_9_3_3.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_3_3.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_78.addWidget(self.lineEdit_9_3_3, 5, 2, 1, 1)

        self.label_353 = QLabel(self.groupBox_43)
        self.label_353.setObjectName(u"label_353")
        sizePolicy3.setHeightForWidth(self.label_353.sizePolicy().hasHeightForWidth())
        self.label_353.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_353, 4, 3, 1, 1)

        self.lineEdit_9_3_2 = QLineEdit(self.groupBox_43)
        self.lineEdit_9_3_2.setObjectName(u"lineEdit_9_3_2")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_3_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_3_2.setSizePolicy(sizePolicy9)
        self.lineEdit_9_3_2.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_3_2.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_78.addWidget(self.lineEdit_9_3_2, 4, 2, 1, 1)

        self.lineEdit_9_3_1 = QLineEdit(self.groupBox_43)
        self.lineEdit_9_3_1.setObjectName(u"lineEdit_9_3_1")
        sizePolicy9.setHeightForWidth(self.lineEdit_9_3_1.sizePolicy().hasHeightForWidth())
        self.lineEdit_9_3_1.setSizePolicy(sizePolicy9)
        self.lineEdit_9_3_1.setMinimumSize(QSize(40, 0))
        self.lineEdit_9_3_1.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_78.addWidget(self.lineEdit_9_3_1, 0, 2, 1, 1)

        self.label_354 = QLabel(self.groupBox_43)
        self.label_354.setObjectName(u"label_354")
        sizePolicy3.setHeightForWidth(self.label_354.sizePolicy().hasHeightForWidth())
        self.label_354.setSizePolicy(sizePolicy3)

        self.gridLayout_78.addWidget(self.label_354, 4, 1, 1, 1)

        self.gridLayout_69.addWidget(self.groupBox_43, 0, 2, 1, 1)

        self.gridLayout_68.addLayout(self.gridLayout_69, 0, 0, 1, 1)

        self.stackedWidget_4.addWidget(self.page_8)

        self.gridLayout_20.addWidget(self.stackedWidget_4, 3, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.widget_17)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy5.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy5)
        self.gridLayout_22 = QGridLayout(self.groupBox_4)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.horizontalSpacer_20 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_20, 0, 1, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.pushButton_38 = QPushButton(self.groupBox_4)
        self.pushButton_38.setObjectName(u"pushButton_38")
        sizePolicy.setHeightForWidth(self.pushButton_38.sizePolicy().hasHeightForWidth())
        self.pushButton_38.setSizePolicy(sizePolicy)
        self.pushButton_38.setMinimumSize(QSize(80, 0))
        self.pushButton_38.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_23.addWidget(self.pushButton_38)

        self.comboBox_16 = QComboBox(self.groupBox_4)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        sizePolicy.setHeightForWidth(self.comboBox_16.sizePolicy().hasHeightForWidth())
        self.comboBox_16.setSizePolicy(sizePolicy)
        self.comboBox_16.setMinimumSize(QSize(70, 0))
        self.comboBox_16.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_23.addWidget(self.comboBox_16)

        self.gridLayout_22.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)

        self.gridLayout_20.addWidget(self.groupBox_4, 1, 0, 1, 1)

        self.groupBox_12 = QGroupBox(self.widget_17)
        self.groupBox_12.setObjectName(u"groupBox_12")
        sizePolicy5.setHeightForWidth(self.groupBox_12.sizePolicy().hasHeightForWidth())
        self.groupBox_12.setSizePolicy(sizePolicy5)
        self.gridLayout_17 = QGridLayout(self.groupBox_12)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(9, 9, -1, -1)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_33 = QPushButton(self.groupBox_12)
        self.pushButton_33.setObjectName(u"pushButton_33")
        sizePolicy.setHeightForWidth(self.pushButton_33.sizePolicy().hasHeightForWidth())
        self.pushButton_33.setSizePolicy(sizePolicy)
        self.pushButton_33.setMinimumSize(QSize(80, 0))
        self.pushButton_33.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_33)

        self.comboBox_15 = QComboBox(self.groupBox_12)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        sizePolicy.setHeightForWidth(self.comboBox_15.sizePolicy().hasHeightForWidth())
        self.comboBox_15.setSizePolicy(sizePolicy)
        self.comboBox_15.setMinimumSize(QSize(70, 0))
        self.comboBox_15.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.comboBox_15)

        self.gridLayout_17.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_37 = QPushButton(self.groupBox_12)
        self.pushButton_37.setObjectName(u"pushButton_37")
        sizePolicy.setHeightForWidth(self.pushButton_37.sizePolicy().hasHeightForWidth())
        self.pushButton_37.setSizePolicy(sizePolicy)
        self.pushButton_37.setMinimumSize(QSize(80, 0))
        self.pushButton_37.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton_37)

        self.label_33 = QLabel(self.groupBox_12)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_7.addWidget(self.label_33)

        self.spinBox_11 = QSpinBox(self.groupBox_12)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setMinimum(0)
        self.spinBox_11.setValue(50)

        self.horizontalLayout_7.addWidget(self.spinBox_11)

        self.label_34 = QLabel(self.groupBox_12)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_7.addWidget(self.label_34)

        self.spinBox_12 = QSpinBox(self.groupBox_12)
        self.spinBox_12.setObjectName(u"spinBox_12")

        self.horizontalLayout_7.addWidget(self.spinBox_12)

        self.gridLayout_17.addLayout(self.horizontalLayout_7, 0, 1, 1, 1)

        self.gridLayout_20.addWidget(self.groupBox_12, 2, 0, 1, 1)

        self.groupBox_32 = QGroupBox(self.widget_17)
        self.groupBox_32.setObjectName(u"groupBox_32")
        self.gridLayout_98 = QGridLayout(self.groupBox_32)
        self.gridLayout_98.setObjectName(u"gridLayout_98")
        self.label_85 = QLabel(self.groupBox_32)
        self.label_85.setObjectName(u"label_85")
        sizePolicy3.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy3)
        self.label_85.setMinimumSize(QSize(60, 0))

        self.gridLayout_98.addWidget(self.label_85, 0, 0, 1, 1)

        self.comboBox_45 = QComboBox(self.groupBox_32)
        self.comboBox_45.setObjectName(u"comboBox_45")
        self.comboBox_45.setEditable(True)

        self.gridLayout_98.addWidget(self.comboBox_45, 0, 1, 1, 1)

        self.gridLayout_20.addWidget(self.groupBox_32, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.widget_17)

        self.widget_7 = QWidget(self.tab)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy5.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy5)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(75, 0))
        self.pushButton.setMaximumSize(QSize(75, 16777215))
        self.pushButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.pushButton_9 = QPushButton(self.widget_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        sizePolicy1.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy1)
        self.pushButton_9.setMinimumSize(QSize(75, 0))
        self.pushButton_9.setMaximumSize(QSize(75, 16777215))
        self.pushButton_9.setCheckable(False)
        self.pushButton_9.setChecked(False)
        self.pushButton_9.setAutoRepeat(False)
        self.pushButton_9.setAutoExclusive(False)

        self.horizontalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_13 = QPushButton(self.widget_7)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout_3.addWidget(self.pushButton_13)

        self.horizontalSpacer_8 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_8)

        self.pushButton_2 = QPushButton(self.widget_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy3.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy3)
        self.pushButton_2.setMinimumSize(QSize(75, 0))
        self.pushButton_2.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.verticalLayout_3.addWidget(self.widget_7)

        self.widget_22 = QWidget(self.tab)
        self.widget_22.setObjectName(u"widget_22")
        sizePolicy5.setHeightForWidth(self.widget_22.sizePolicy().hasHeightForWidth())
        self.widget_22.setSizePolicy(sizePolicy5)
        self.verticalLayout_5 = QVBoxLayout(self.widget_22)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_3.addWidget(self.widget_22)

        self.tabWidget_3.addTab(self.tab, "")

        self.gridLayout_4.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_12, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_CC)
        self.page_CR = QWidget()
        self.page_CR.setObjectName(u"page_CR")
        self.gridLayout_7 = QGridLayout(self.page_CR)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_23 = QWidget(self.page_CR)
        self.widget_23.setObjectName(u"widget_23")
        self.gridLayout_15 = QGridLayout(self.widget_23)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_6 = QTabWidget(self.widget_23)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_16 = QGridLayout(self.tab_10)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget_24 = QWidget(self.tab_10)
        self.widget_24.setObjectName(u"widget_24")
        self.gridLayout_19 = QGridLayout(self.widget_24)
        self.gridLayout_19.setSpacing(6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(9, 9, 9, 9)
        self.groupBox = QGroupBox(self.widget_24)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_21 = QGridLayout(self.groupBox)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.tableWidget = CRTableWidget(self.groupBox)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_21.addWidget(self.tableWidget, 0, 0, 1, 4)

        self.gridLayout_19.addWidget(self.groupBox, 0, 0, 1, 2)

        self.stackedWidget_2 = QStackedWidget(self.widget_24)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_47 = QGridLayout(self.page)
        self.gridLayout_47.setSpacing(6)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.gridLayout_47.setContentsMargins(0, 0, 0, 0)
        self.groupBox_11 = QGroupBox(self.page)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.gridLayout_46 = QGridLayout(self.groupBox_11)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.pushButton_15 = QPushButton(self.groupBox_11)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_46.addWidget(self.pushButton_15, 1, 4, 1, 1)

        self.label_43 = QLabel(self.groupBox_11)
        self.label_43.setObjectName(u"label_43")
        sizePolicy3.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy3)

        self.gridLayout_46.addWidget(self.label_43, 1, 0, 1, 1)

        self.pushButton_23 = QPushButton(self.groupBox_11)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout_46.addWidget(self.pushButton_23, 0, 4, 1, 1)

        self.label_37 = QLabel(self.groupBox_11)
        self.label_37.setObjectName(u"label_37")
        sizePolicy3.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy3)

        self.gridLayout_46.addWidget(self.label_37, 0, 0, 1, 1)

        self.label_35 = QLabel(self.groupBox_11)
        self.label_35.setObjectName(u"label_35")
        sizePolicy3.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy3)
        self.label_35.setMinimumSize(QSize(60, 0))
        self.label_35.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_46.addWidget(self.label_35, 0, 1, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.comboBox_12 = QComboBox(self.groupBox_11)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        sizePolicy9.setHeightForWidth(self.comboBox_12.sizePolicy().hasHeightForWidth())
        self.comboBox_12.setSizePolicy(sizePolicy9)
        self.comboBox_12.setMinimumSize(QSize(60, 0))
        self.comboBox_12.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_8.addWidget(self.comboBox_12)

        self.pushButton_17 = QPushButton(self.groupBox_11)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.horizontalLayout_8.addWidget(self.pushButton_17)

        self.gridLayout_46.addLayout(self.horizontalLayout_8, 1, 1, 1, 2)

        self.spinBox_19 = QSpinBox(self.groupBox_11)
        self.spinBox_19.setObjectName(u"spinBox_19")
        self.spinBox_19.setMinimumSize(QSize(70, 0))
        self.spinBox_19.setMaximumSize(QSize(70, 16777215))

        self.gridLayout_46.addWidget(self.spinBox_19, 0, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_46.addItem(self.horizontalSpacer_17, 0, 3, 1, 1)

        self.gridLayout_47.addWidget(self.groupBox_11, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_48 = QGridLayout(self.page_2)
        self.gridLayout_48.setSpacing(6)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.gridLayout_48.setContentsMargins(0, 0, 0, 0)
        self.groupBox_14 = QGroupBox(self.page_2)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_45 = QGridLayout(self.groupBox_14)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_36 = QLabel(self.groupBox_14)
        self.label_36.setObjectName(u"label_36")
        sizePolicy3.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy3)

        self.gridLayout_45.addWidget(self.label_36, 0, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.groupBox_14)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_45.addWidget(self.lineEdit_3, 0, 1, 1, 2)

        self.label_38 = QLabel(self.groupBox_14)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)

        self.gridLayout_45.addWidget(self.label_38, 1, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox_13 = QComboBox(self.groupBox_14)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        sizePolicy9.setHeightForWidth(self.comboBox_13.sizePolicy().hasHeightForWidth())
        self.comboBox_13.setSizePolicy(sizePolicy9)
        self.comboBox_13.setMinimumSize(QSize(60, 0))
        self.comboBox_13.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_10.addWidget(self.comboBox_13)

        self.pushButton_42 = QPushButton(self.groupBox_14)
        self.pushButton_42.setObjectName(u"pushButton_42")

        self.horizontalLayout_10.addWidget(self.pushButton_42)

        self.gridLayout_45.addLayout(self.horizontalLayout_10, 1, 1, 1, 1)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.pushButton_24 = QPushButton(self.groupBox_14)
        self.pushButton_24.setObjectName(u"pushButton_24")

        self.horizontalLayout_30.addWidget(self.pushButton_24)

        self.pushButton_39 = QPushButton(self.groupBox_14)
        self.pushButton_39.setObjectName(u"pushButton_39")

        self.horizontalLayout_30.addWidget(self.pushButton_39)

        self.gridLayout_45.addLayout(self.horizontalLayout_30, 1, 2, 1, 1)

        self.gridLayout_48.addWidget(self.groupBox_14, 0, 0, 1, 1)

        self.stackedWidget_2.addWidget(self.page_2)

        self.gridLayout_19.addWidget(self.stackedWidget_2, 1, 0, 1, 1)

        self.gridLayout_16.addWidget(self.widget_24, 0, 0, 1, 1)

        self.tabWidget_6.addTab(self.tab_10, "")

        self.gridLayout_15.addWidget(self.tabWidget_6, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_7, 0, 0, 1, 1)

        self.widget_25 = QWidget(self.widget_23)
        self.widget_25.setObjectName(u"widget_25")
        sizePolicy5.setHeightForWidth(self.widget_25.sizePolicy().hasHeightForWidth())
        self.widget_25.setSizePolicy(sizePolicy5)
        self.gridLayout_44 = QGridLayout(self.widget_25)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.gridLayout_44.setContentsMargins(20, -1, 22, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_44.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.pushButton_16 = QPushButton(self.widget_25)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.gridLayout_44.addWidget(self.pushButton_16, 0, 2, 1, 1)

        self.gridLayout_15.addWidget(self.widget_25, 2, 0, 1, 1)

        self.gridLayout_7.addWidget(self.widget_23, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_CR)
        self.page_IC = QWidget()
        self.page_IC.setObjectName(u"page_IC")
        self.gridLayout_6 = QGridLayout(self.page_IC)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.page_IC)
        self.widget_5.setObjectName(u"widget_5")
        self.gridLayout_24 = QGridLayout(self.widget_5)
        self.gridLayout_24.setSpacing(0)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_4 = QTabWidget(self.widget_5)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        sizePolicy6.setHeightForWidth(self.tabWidget_4.sizePolicy().hasHeightForWidth())
        self.tabWidget_4.setSizePolicy(sizePolicy6)
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_4 = QVBoxLayout(self.tab_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_8 = QWidget(self.tab_5)
        self.widget_8.setObjectName(u"widget_8")
        sizePolicy6.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy6)
        self.verticalLayout_7 = QVBoxLayout(self.widget_8)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 9, 9, -1)
        self.groupBox_2 = QGroupBox(self.widget_8)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy5.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy5)
        self.gridLayout_8 = QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(6)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(9, 9, 9, 9)
        self.radioButton_2 = QRadioButton(self.groupBox_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy10 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy10)
        self.radioButton_2.setChecked(False)

        self.gridLayout_8.addWidget(self.radioButton_2, 0, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_8.addWidget(self.label_4, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.groupBox_2)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy10.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy10)
        self.radioButton.setLayoutDirection(Qt.LeftToRight)
        self.radioButton.setChecked(True)

        self.gridLayout_8.addWidget(self.radioButton, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_4, 0, 1, 1, 1)

        self.verticalLayout_7.addWidget(self.groupBox_2)

        self.stackedWidget_3 = QStackedWidget(self.widget_8)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        sizePolicy1.setHeightForWidth(self.stackedWidget_3.sizePolicy().hasHeightForWidth())
        self.stackedWidget_3.setSizePolicy(sizePolicy1)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.gridLayout_26 = QGridLayout(self.page_6)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.groupBox_6 = QGroupBox(self.page_6)
        self.groupBox_6.setObjectName(u"groupBox_6")
        sizePolicy11 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy11)
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setSpacing(6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(9, 9, 9, 9)
        self.widget_29 = QWidget(self.groupBox_6)
        self.widget_29.setObjectName(u"widget_29")
        sizePolicy5.setHeightForWidth(self.widget_29.sizePolicy().hasHeightForWidth())
        self.widget_29.setSizePolicy(sizePolicy5)
        self.gridLayout_42 = QGridLayout(self.widget_29)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.gridLayout_42.setHorizontalSpacing(6)
        self.gridLayout_42.setVerticalSpacing(0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(6)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.pushButton_3 = QPushButton(self.widget_29)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.pushButton_3)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_10)

        self.pushButton_5 = QPushButton(self.widget_29)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_25.addWidget(self.pushButton_5)

        self.horizontalLayout_24.addLayout(self.horizontalLayout_25)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.horizontalLayout_24.addLayout(self.horizontalLayout_13)

        self.gridLayout_42.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)

        self.gridLayout_11.addWidget(self.widget_29, 3, 0, 1, 1)

        self.listWidget_2 = MyListWidget(self.groupBox_6)
        self.listWidget_2.setObjectName(u"listWidget_2")
        sizePolicy12 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.listWidget_2.sizePolicy().hasHeightForWidth())
        self.listWidget_2.setSizePolicy(sizePolicy12)
        self.listWidget_2.setMaximumSize(QSize(16777215, 120))

        self.gridLayout_11.addWidget(self.listWidget_2, 2, 0, 1, 1)

        self.widget_13 = QWidget(self.groupBox_6)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy5.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy5)
        self.gridLayout_27 = QGridLayout(self.widget_13)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(9, 9, 9, -1)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget_13)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lineEdit = QLineEdit(self.widget_13)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit)

        self.toolButton_2 = QToolButton(self.widget_13)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_5.addWidget(self.toolButton_2)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.gridLayout_27.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.gridLayout_11.addWidget(self.widget_13, 0, 0, 1, 1)

        self.widget_9 = QWidget(self.groupBox_6)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMinimumSize(QSize(0, 150))
        self.widget_9.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_41 = QGridLayout(self.widget_9)
        self.gridLayout_41.setSpacing(0)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.gridLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget_9)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_41.addWidget(self.label_2, 0, 0, 1, 1)

        self.gridLayout_11.addWidget(self.widget_9, 1, 0, 1, 1)

        self.gridLayout_26.addWidget(self.groupBox_6, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.gridLayout_30 = QGridLayout(self.page_7)
        self.gridLayout_30.setSpacing(0)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.widget_10 = QWidget(self.page_7)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy5.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy5)
        self.gridLayout_12 = QGridLayout(self.widget_10)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_30.addWidget(self.widget_10, 1, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.page_7)
        self.groupBox_7.setObjectName(u"groupBox_7")
        sizePolicy1.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy1)
        self.gridLayout_57 = QGridLayout(self.groupBox_7)
        self.gridLayout_57.setSpacing(6)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.gridLayout_57.setContentsMargins(9, 9, 9, 9)
        self.label_41 = QLabel(self.groupBox_7)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(80, 0))
        self.label_41.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_57.addWidget(self.label_41, 6, 0, 1, 1)

        self.widget_12 = QWidget(self.groupBox_7)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy5.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy5)
        self.gridLayout_56 = QGridLayout(self.widget_12)
        self.gridLayout_56.setSpacing(0)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.gridLayout_56.setContentsMargins(0, 0, 0, 0)
        self.pushButton_45 = QPushButton(self.widget_12)
        self.pushButton_45.setObjectName(u"pushButton_45")
        sizePolicy.setHeightForWidth(self.pushButton_45.sizePolicy().hasHeightForWidth())
        self.pushButton_45.setSizePolicy(sizePolicy)

        self.gridLayout_56.addWidget(self.pushButton_45, 0, 1, 1, 1)

        self.pushButton_44 = QPushButton(self.widget_12)
        self.pushButton_44.setObjectName(u"pushButton_44")
        sizePolicy.setHeightForWidth(self.pushButton_44.sizePolicy().hasHeightForWidth())
        self.pushButton_44.setSizePolicy(sizePolicy)

        self.gridLayout_56.addWidget(self.pushButton_44, 0, 3, 1, 1)

        self.pushButton_46 = QPushButton(self.widget_12)
        self.pushButton_46.setObjectName(u"pushButton_46")
        sizePolicy.setHeightForWidth(self.pushButton_46.sizePolicy().hasHeightForWidth())
        self.pushButton_46.setSizePolicy(sizePolicy)

        self.gridLayout_56.addWidget(self.pushButton_46, 0, 5, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_21, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_56.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.gridLayout_57.addWidget(self.widget_12, 9, 0, 1, 2)

        self.comboBox_14 = QComboBox(self.groupBox_7)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_57.addWidget(self.comboBox_14, 3, 1, 1, 1)

        self.widget_26 = QWidget(self.groupBox_7)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMinimumSize(QSize(0, 0))
        self.gridLayout_100 = QGridLayout(self.widget_26)
        self.gridLayout_100.setObjectName(u"gridLayout_100")
        self.gridLayout_100.setHorizontalSpacing(6)
        self.gridLayout_100.setVerticalSpacing(0)
        self.gridLayout_100.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_57.addWidget(self.widget_26, 4, 0, 1, 2)

        self.label_5 = QLabel(self.groupBox_7)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setMinimumSize(QSize(80, 0))
        self.label_5.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_57.addWidget(self.label_5, 1, 0, 1, 1)

        self.comboBox_17 = QComboBox(self.groupBox_7)
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.setObjectName(u"comboBox_17")
        self.comboBox_17.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_57.addWidget(self.comboBox_17, 6, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_57.addItem(self.verticalSpacer_6, 8, 0, 1, 2)

        self.label_66 = QLabel(self.groupBox_7)
        self.label_66.setObjectName(u"label_66")
        sizePolicy3.setHeightForWidth(self.label_66.sizePolicy().hasHeightForWidth())
        self.label_66.setSizePolicy(sizePolicy3)
        self.label_66.setMinimumSize(QSize(80, 0))
        self.label_66.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_57.addWidget(self.label_66, 2, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_7)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setMinimumSize(QSize(80, 0))
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_57.addWidget(self.label_3, 0, 0, 1, 1)

        self.comboBox_18 = QComboBox(self.groupBox_7)
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_57.addWidget(self.comboBox_18, 2, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.groupBox_7)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy5.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy5)

        self.gridLayout_57.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.label_40 = QLabel(self.groupBox_7)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(80, 0))
        self.label_40.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_57.addWidget(self.label_40, 3, 0, 1, 1)

        self.comboBox_7 = QComboBox(self.groupBox_7)
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_57.addWidget(self.comboBox_7, 1, 1, 1, 1)

        self.stackedWidget_8 = QStackedWidget(self.groupBox_7)
        self.stackedWidget_8.setObjectName(u"stackedWidget_8")
        sizePolicy5.setHeightForWidth(self.stackedWidget_8.sizePolicy().hasHeightForWidth())
        self.stackedWidget_8.setSizePolicy(sizePolicy5)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        sizePolicy5.setHeightForWidth(self.page_3.sizePolicy().hasHeightForWidth())
        self.page_3.setSizePolicy(sizePolicy5)
        self.gridLayout_95 = QGridLayout(self.page_3)
        self.gridLayout_95.setSpacing(0)
        self.gridLayout_95.setObjectName(u"gridLayout_95")
        self.gridLayout_95.setContentsMargins(0, 0, 0, 0)
        self.groupBox_33 = QGroupBox(self.page_3)
        self.groupBox_33.setObjectName(u"groupBox_33")
        sizePolicy5.setHeightForWidth(self.groupBox_33.sizePolicy().hasHeightForWidth())
        self.groupBox_33.setSizePolicy(sizePolicy5)
        self.gridLayout_102 = QGridLayout(self.groupBox_33)
        self.gridLayout_102.setObjectName(u"gridLayout_102")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_83 = QLabel(self.groupBox_33)
        self.label_83.setObjectName(u"label_83")
        sizePolicy.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy)
        self.label_83.setMinimumSize(QSize(0, 0))
        self.label_83.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_34.addWidget(self.label_83)

        self.comboBox_34 = QComboBox(self.groupBox_33)
        self.comboBox_34.addItem("")
        self.comboBox_34.setObjectName(u"comboBox_34")
        sizePolicy.setHeightForWidth(self.comboBox_34.sizePolicy().hasHeightForWidth())
        self.comboBox_34.setSizePolicy(sizePolicy)

        self.horizontalLayout_34.addWidget(self.comboBox_34)

        self.label_80 = QLabel(self.groupBox_33)
        self.label_80.setObjectName(u"label_80")
        sizePolicy5.setHeightForWidth(self.label_80.sizePolicy().hasHeightForWidth())
        self.label_80.setSizePolicy(sizePolicy5)

        self.horizontalLayout_34.addWidget(self.label_80)

        self.comboBox_42 = QComboBox(self.groupBox_33)
        self.comboBox_42.addItem("")
        self.comboBox_42.addItem("")
        self.comboBox_42.addItem("")
        self.comboBox_42.addItem("")
        self.comboBox_42.addItem("")
        self.comboBox_42.setObjectName(u"comboBox_42")
        sizePolicy.setHeightForWidth(self.comboBox_42.sizePolicy().hasHeightForWidth())
        self.comboBox_42.setSizePolicy(sizePolicy)

        self.horizontalLayout_34.addWidget(self.comboBox_42)

        self.label_84 = QLabel(self.groupBox_33)
        self.label_84.setObjectName(u"label_84")
        sizePolicy5.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy5)
        self.label_84.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_34.addWidget(self.label_84)

        self.comboBox_44 = QComboBox(self.groupBox_33)
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.addItem("")
        self.comboBox_44.setObjectName(u"comboBox_44")
        sizePolicy9.setHeightForWidth(self.comboBox_44.sizePolicy().hasHeightForWidth())
        self.comboBox_44.setSizePolicy(sizePolicy9)
        self.comboBox_44.setEditable(True)

        self.horizontalLayout_34.addWidget(self.comboBox_44)

        self.gridLayout_102.addLayout(self.horizontalLayout_34, 0, 0, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_28)

        self.pushButton_31 = QPushButton(self.groupBox_33)
        self.pushButton_31.setObjectName(u"pushButton_31")

        self.horizontalLayout_29.addWidget(self.pushButton_31)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_30)

        self.gridLayout_102.addLayout(self.horizontalLayout_29, 1, 0, 1, 1)

        self.gridLayout_95.addWidget(self.groupBox_33, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.page_3)
        self.page_16 = QWidget()
        self.page_16.setObjectName(u"page_16")
        self.gridLayout_103 = QGridLayout(self.page_16)
        self.gridLayout_103.setSpacing(0)
        self.gridLayout_103.setObjectName(u"gridLayout_103")
        self.gridLayout_103.setContentsMargins(0, 0, 0, 0)
        self.groupBox_27 = QGroupBox(self.page_16)
        self.groupBox_27.setObjectName(u"groupBox_27")
        self.gridLayout_108 = QGridLayout(self.groupBox_27)
        self.gridLayout_108.setObjectName(u"gridLayout_108")
        self.label_82 = QLabel(self.groupBox_27)
        self.label_82.setObjectName(u"label_82")
        sizePolicy1.setHeightForWidth(self.label_82.sizePolicy().hasHeightForWidth())
        self.label_82.setSizePolicy(sizePolicy1)
        self.label_82.setMinimumSize(QSize(80, 0))
        self.label_82.setMaximumSize(QSize(80, 16777215))

        self.gridLayout_108.addWidget(self.label_82, 0, 0, 1, 1)

        self.spinBox_21 = MySpinBox(self.groupBox_27)
        self.spinBox_21.setObjectName(u"spinBox_21")
        self.spinBox_21.setMinimum(1)
        self.spinBox_21.setMaximum(100000)
        self.spinBox_21.setValue(100)

        self.gridLayout_108.addWidget(self.spinBox_21, 0, 1, 1, 1)

        self.gridLayout_103.addWidget(self.groupBox_27, 0, 0, 1, 1)

        self.stackedWidget_8.addWidget(self.page_16)

        self.gridLayout_57.addWidget(self.stackedWidget_8, 5, 0, 1, 2)

        self.gridLayout_30.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_7)

        self.verticalLayout_7.addWidget(self.stackedWidget_3)

        self.widget_18 = QWidget(self.widget_8)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy5.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy5)
        self.gridLayout_28 = QGridLayout(self.widget_18)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setHorizontalSpacing(6)
        self.gridLayout_28.setVerticalSpacing(0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.pushButton_6 = QPushButton(self.widget_18)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.pushButton_6)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_13)

        self.pushButton_28 = QPushButton(self.widget_18)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setMinimumSize(QSize(50, 0))
        self.pushButton_28.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_12.addWidget(self.pushButton_28)

        self.horizontalLayout_19.addLayout(self.horizontalLayout_12)

        self.gridLayout_28.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)

        self.verticalLayout_7.addWidget(self.widget_18)

        self.verticalLayout_4.addWidget(self.widget_8)

        self.tabWidget_4.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_63 = QGridLayout(self.tab_4)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_63.addItem(self.verticalSpacer_13, 0, 0, 1, 1)

        self.groupBox_19 = QGroupBox(self.tab_4)
        self.groupBox_19.setObjectName(u"groupBox_19")
        sizePolicy2.setHeightForWidth(self.groupBox_19.sizePolicy().hasHeightForWidth())
        self.groupBox_19.setSizePolicy(sizePolicy2)
        self.formLayout_3 = QFormLayout(self.groupBox_19)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.groupBox_19)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.doubleSpinBox = QDoubleSpinBox(self.groupBox_19)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_45 = QLabel(self.groupBox_19)
        self.label_45.setObjectName(u"label_45")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_45)

        self.label_46 = QLabel(self.groupBox_19)
        self.label_46.setObjectName(u"label_46")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_46)

        self.spinBox_22 = QSpinBox(self.groupBox_19)
        self.spinBox_22.setObjectName(u"spinBox_22")
        self.spinBox_22.setMinimum(27)
        self.spinBox_22.setMaximum(25000000)
        self.spinBox_22.setSingleStep(100)
        self.spinBox_22.setValue(800)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.spinBox_22)

        self.label_47 = QLabel(self.groupBox_19)
        self.label_47.setObjectName(u"label_47")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_47)

        self.comboBox_4 = QComboBox(self.groupBox_19)
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.comboBox_4)

        self.label_48 = QLabel(self.groupBox_19)
        self.label_48.setObjectName(u"label_48")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_48)

        self.doubleSpinBox_2 = QDoubleSpinBox(self.groupBox_19)
        self.doubleSpinBox_2.setObjectName(u"doubleSpinBox_2")

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBox_2)

        self.label_65 = QLabel(self.groupBox_19)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_65)

        self.spinBox_23 = QSpinBox(self.groupBox_19)
        self.spinBox_23.setObjectName(u"spinBox_23")
        self.spinBox_23.setDisplayIntegerBase(10)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.spinBox_23)

        self.label_67 = QLabel(self.groupBox_19)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_3.setWidget(10, QFormLayout.LabelRole, self.label_67)

        self.label_71 = QLabel(self.groupBox_19)
        self.label_71.setObjectName(u"label_71")

        self.formLayout_3.setWidget(11, QFormLayout.LabelRole, self.label_71)

        self.spinBox_24 = QSpinBox(self.groupBox_19)
        self.spinBox_24.setObjectName(u"spinBox_24")
        self.spinBox_24.setValue(99)
        self.spinBox_24.setDisplayIntegerBase(10)

        self.formLayout_3.setWidget(11, QFormLayout.FieldRole, self.spinBox_24)

        self.label_72 = QLabel(self.groupBox_19)
        self.label_72.setObjectName(u"label_72")

        self.formLayout_3.setWidget(12, QFormLayout.LabelRole, self.label_72)

        self.label_92 = QLabel(self.groupBox_19)
        self.label_92.setObjectName(u"label_92")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_92)

        self.label_93 = QLabel(self.groupBox_19)
        self.label_93.setObjectName(u"label_93")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.label_93)

        self.comboBox_6 = QComboBox(self.groupBox_19)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.comboBox_6)

        self.label_94 = QLabel(self.groupBox_19)
        self.label_94.setObjectName(u"label_94")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_94)

        self.doubleSpinBox_5 = QDoubleSpinBox(self.groupBox_19)
        self.doubleSpinBox_5.setObjectName(u"doubleSpinBox_5")
        self.doubleSpinBox_5.setValue(0.500000000000000)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.doubleSpinBox_5)

        self.label_95 = QLabel(self.groupBox_19)
        self.label_95.setObjectName(u"label_95")

        self.formLayout_3.setWidget(13, QFormLayout.LabelRole, self.label_95)

        self.radioButton_3 = QRadioButton(self.groupBox_19)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.formLayout_3.setWidget(10, QFormLayout.FieldRole, self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.groupBox_19)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.formLayout_3.setWidget(12, QFormLayout.FieldRole, self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.groupBox_19)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.formLayout_3.setWidget(13, QFormLayout.FieldRole, self.radioButton_5)

        self.radioButton_6 = QRadioButton(self.groupBox_19)
        self.radioButton_6.setObjectName(u"radioButton_6")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.radioButton_6)

        self.radioButton_7 = QRadioButton(self.groupBox_19)
        self.radioButton_7.setObjectName(u"radioButton_7")

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.radioButton_7)

        self.gridLayout_63.addWidget(self.groupBox_19, 1, 0, 1, 1)

        self.widget_27 = QWidget(self.tab_4)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMinimumSize(QSize(0, 0))
        self.gridLayout_80 = QGridLayout(self.widget_27)
        self.gridLayout_80.setObjectName(u"gridLayout_80")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_80.addItem(self.horizontalSpacer_27, 0, 0, 1, 1)

        self.pushButton_54 = QPushButton(self.widget_27)
        self.pushButton_54.setObjectName(u"pushButton_54")

        self.gridLayout_80.addWidget(self.pushButton_54, 0, 1, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_80.addItem(self.horizontalSpacer_26, 0, 3, 1, 1)

        self.pushButton_55 = QPushButton(self.widget_27)
        self.pushButton_55.setObjectName(u"pushButton_55")

        self.gridLayout_80.addWidget(self.pushButton_55, 0, 2, 1, 1)

        self.gridLayout_63.addWidget(self.widget_27, 3, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_3, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_10 = QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_8 = QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_10.addWidget(self.pushButton_8, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_10.addWidget(self.pushButton_7, 1, 0, 1, 1)

        self.pushButton_10 = QPushButton(self.groupBox_3)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_10.addWidget(self.pushButton_10, 2, 0, 1, 1)

        self.pushButton_18 = QPushButton(self.groupBox_3)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout_10.addWidget(self.pushButton_18, 2, 1, 1, 1)

        self.widget_20 = QWidget(self.groupBox_3)
        self.widget_20.setObjectName(u"widget_20")
        self.gridLayout_43 = QGridLayout(self.widget_20)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")
        self.formLayout = QFormLayout(self.widget_21)
        self.formLayout.setObjectName(u"formLayout")
        self.label_7 = QLabel(self.widget_21)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(80, 0))
        self.label_7.setMaximumSize(QSize(80, 16777215))
        self.label_7.setSizeIncrement(QSize(0, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.comboBox = QComboBox(self.widget_21)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_4 = QPushButton(self.widget_21)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_16.addWidget(self.pushButton_4)

        self.pushButton_25 = QPushButton(self.widget_21)
        self.pushButton_25.setObjectName(u"pushButton_25")

        self.horizontalLayout_16.addWidget(self.pushButton_25)

        self.formLayout.setLayout(3, QFormLayout.SpanningRole, self.horizontalLayout_16)

        self.stackedWidget_14 = QStackedWidget(self.widget_21)
        self.stackedWidget_14.setObjectName(u"stackedWidget_14")
        self.stackedWidget_14Page1 = QWidget()
        self.stackedWidget_14Page1.setObjectName(u"stackedWidget_14Page1")
        self.formLayout_2 = QFormLayout(self.stackedWidget_14Page1)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_8 = QLabel(self.stackedWidget_14Page1)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.comboBox_2 = QComboBox(self.stackedWidget_14Page1)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_2)

        self.label_9 = QLabel(self.stackedWidget_14Page1)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.spinBox = QSpinBox(self.stackedWidget_14Page1)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setValue(5)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.spinBox)

        self.stackedWidget_14.addWidget(self.stackedWidget_14Page1)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.stackedWidget_14.addWidget(self.page_11)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.stackedWidget_14)

        self.gridLayout_43.addWidget(self.widget_21, 0, 0, 1, 1)

        self.gridLayout_10.addWidget(self.widget_20, 0, 0, 1, 2)

        self.gridLayout_9.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, 10, -1)
        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.pushButton_22 = QPushButton(self.tab_6)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.horizontalLayout_15.addWidget(self.pushButton_22)

        self.gridLayout_9.addLayout(self.horizontalLayout_15, 2, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_6, "")

        self.gridLayout_24.addWidget(self.tabWidget_4, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_24.addItem(self.verticalSpacer_5, 0, 0, 1, 1)

        self.gridLayout_6.addWidget(self.widget_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_IC)
        self.page_QSCI = QWidget()
        self.page_QSCI.setObjectName(u"page_QSCI")
        self.gridLayout_83 = QGridLayout(self.page_QSCI)
        self.gridLayout_83.setSpacing(0)
        self.gridLayout_83.setObjectName(u"gridLayout_83")
        self.gridLayout_83.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_8 = QTabWidget(self.page_QSCI)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_84 = QGridLayout(self.tab_14)
        self.gridLayout_84.setObjectName(u"gridLayout_84")
        self.gridLayout_84.setHorizontalSpacing(0)
        self.gridLayout_84.setContentsMargins(0, 0, 0, 0)
        self.widget_32 = QWidget(self.tab_14)
        self.widget_32.setObjectName(u"widget_32")
        self.gridLayout_87 = QGridLayout(self.widget_32)
        self.gridLayout_87.setObjectName(u"gridLayout_87")
        self.groupBox_26 = QGroupBox(self.widget_32)
        self.groupBox_26.setObjectName(u"groupBox_26")
        self.gridLayout_88 = QGridLayout(self.groupBox_26)
        self.gridLayout_88.setSpacing(0)
        self.gridLayout_88.setObjectName(u"gridLayout_88")
        self.gridLayout_88.setContentsMargins(0, 6, 0, 0)
        self.tabWidget_9 = QTabWidget(self.groupBox_26)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_89 = QGridLayout(self.tab_15)
        self.gridLayout_89.setSpacing(0)
        self.gridLayout_89.setObjectName(u"gridLayout_89")
        self.gridLayout_89.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_4 = QsciTableWidget(self.tab_15)
        self.tableWidget_4.setObjectName(u"tableWidget_4")

        self.gridLayout_89.addWidget(self.tableWidget_4, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.gridLayout_90 = QGridLayout(self.tab_16)
        self.gridLayout_90.setSpacing(0)
        self.gridLayout_90.setObjectName(u"gridLayout_90")
        self.gridLayout_90.setContentsMargins(0, 0, 0, 0)
        self.tableWidget_5 = QsciTableWidget(self.tab_16)
        if (self.tableWidget_5.columnCount() < 2):
            self.tableWidget_5.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget_5.setObjectName(u"tableWidget_5")

        self.gridLayout_90.addWidget(self.tableWidget_5, 0, 0, 1, 1)

        self.tabWidget_9.addTab(self.tab_16, "")

        self.gridLayout_88.addWidget(self.tabWidget_9, 0, 0, 1, 1)

        self.gridLayout_87.addWidget(self.groupBox_26, 0, 0, 1, 1)

        self.groupBox_21 = QGroupBox(self.widget_32)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.gridLayout_85 = QGridLayout(self.groupBox_21)
        self.gridLayout_85.setSpacing(0)
        self.gridLayout_85.setObjectName(u"gridLayout_85")
        self.gridLayout_85.setContentsMargins(0, 6, 0, 0)
        self.tabWidget_10 = QTabWidget(self.groupBox_21)
        self.tabWidget_10.setObjectName(u"tabWidget_10")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.gridLayout_92 = QGridLayout(self.tab_17)
        self.gridLayout_92.setSpacing(0)
        self.gridLayout_92.setObjectName(u"gridLayout_92")
        self.gridLayout_92.setContentsMargins(0, 0, 0, 0)
        self.widget_31 = codeCompilerPy()
        self.widget_31.setObjectName(u"widget_31")

        self.gridLayout_92.addWidget(self.widget_31, 0, 0, 1, 1)

        self.tabWidget_10.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.gridLayout_93 = QGridLayout(self.tab_18)
        self.gridLayout_93.setSpacing(0)
        self.gridLayout_93.setObjectName(u"gridLayout_93")
        self.gridLayout_93.setContentsMargins(0, 0, 0, 0)
        self.widget_34 = codeCompilerVBS()
        self.widget_34.setObjectName(u"widget_34")

        self.gridLayout_93.addWidget(self.widget_34, 0, 0, 1, 1)

        self.tabWidget_10.addTab(self.tab_18, "")

        self.gridLayout_85.addWidget(self.tabWidget_10, 0, 0, 1, 1)

        self.gridLayout_87.addWidget(self.groupBox_21, 1, 0, 1, 1)

        self.gridLayout_84.addWidget(self.widget_32, 0, 0, 1, 1)

        self.tabWidget_8.addTab(self.tab_14, "")

        self.gridLayout_83.addWidget(self.tabWidget_8, 1, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_83.addItem(self.verticalSpacer_11, 0, 0, 1, 1)

        self.widget_33 = QWidget(self.page_QSCI)
        self.widget_33.setObjectName(u"widget_33")
        self.gridLayout_91 = QGridLayout(self.widget_33)
        self.gridLayout_91.setObjectName(u"gridLayout_91")
        self.pushButton_47 = QPushButton(self.widget_33)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)

        self.gridLayout_91.addWidget(self.pushButton_47, 0, 3, 1, 1)

        self.pushButton_48 = QPushButton(self.widget_33)
        self.pushButton_48.setObjectName(u"pushButton_48")
        sizePolicy3.setHeightForWidth(self.pushButton_48.sizePolicy().hasHeightForWidth())
        self.pushButton_48.setSizePolicy(sizePolicy3)

        self.gridLayout_91.addWidget(self.pushButton_48, 0, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_33)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_91.addWidget(self.pushButton_14, 0, 0, 1, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_91.addItem(self.horizontalSpacer_19, 0, 1, 1, 1)

        self.gridLayout_83.addWidget(self.widget_33, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_QSCI)
        self.page_STM = QWidget()
        self.page_STM.setObjectName(u"page_STM")
        self.gridLayout_14 = QGridLayout(self.page_STM)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.page_STM)
        self.widget_14.setObjectName(u"widget_14")
        self.gridLayout_29 = QGridLayout(self.widget_14)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_29.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.tabWidget_5 = QTabWidget(self.widget_14)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        sizePolicy8.setHeightForWidth(self.tabWidget_5.sizePolicy().hasHeightForWidth())
        self.tabWidget_5.setSizePolicy(sizePolicy8)
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_31 = QGridLayout(self.tab_7)
        self.gridLayout_31.setSpacing(0)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.gridLayout_31.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.tab_7)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_8 = QVBoxLayout(self.widget_15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMinimumSize(QSize(0, 0))
        self.widget_19.setMaximumSize(QSize(16777215, 200))
        self.gridLayout_33 = QGridLayout(self.widget_19)
        self.gridLayout_33.setSpacing(0)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.widget_19)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 200))
        self.label_10.setMaximumSize(QSize(16777215, 200))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_33.addWidget(self.label_10, 0, 0, 1, 1)

        self.verticalLayout_8.addWidget(self.widget_19)

        self.groupBox_9 = QGroupBox(self.widget_15)
        self.groupBox_9.setObjectName(u"groupBox_9")
        sizePolicy5.setHeightForWidth(self.groupBox_9.sizePolicy().hasHeightForWidth())
        self.groupBox_9.setSizePolicy(sizePolicy5)
        self.gridLayout_37 = QGridLayout(self.groupBox_9)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.widget_171 = QWidget(self.groupBox_9)
        self.widget_171.setObjectName(u"widget_171")
        self.widget_171.setMinimumSize(QSize(0, 0))
        self.gridLayout_39 = QGridLayout(self.widget_171)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.widget_171)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.label_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEdit_2 = QLineEdit(self.widget_171)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy5.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy5)
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_21.addWidget(self.lineEdit_2)

        self.toolButton_3 = QToolButton(self.widget_171)
        self.toolButton_3.setObjectName(u"toolButton_3")

        self.horizontalLayout_21.addWidget(self.toolButton_3)

        self.horizontalLayout_18.addLayout(self.horizontalLayout_21)

        self.gridLayout_39.addLayout(self.horizontalLayout_18, 0, 0, 1, 1)

        self.gridLayout_37.addWidget(self.widget_171, 0, 0, 1, 2)

        self.verticalLayout_8.addWidget(self.groupBox_9)

        self.groupBox_8 = QGroupBox(self.widget_15)
        self.groupBox_8.setObjectName(u"groupBox_8")
        sizePolicy5.setHeightForWidth(self.groupBox_8.sizePolicy().hasHeightForWidth())
        self.groupBox_8.setSizePolicy(sizePolicy5)
        self.groupBox_8.setMinimumSize(QSize(0, 0))
        self.groupBox_8.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_36 = QGridLayout(self.groupBox_8)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.pushButton_34 = QPushButton(self.groupBox_8)
        self.pushButton_34.setObjectName(u"pushButton_34")
        sizePolicy.setHeightForWidth(self.pushButton_34.sizePolicy().hasHeightForWidth())
        self.pushButton_34.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.pushButton_34)

        self.pushButton_29 = QPushButton(self.groupBox_8)
        self.pushButton_29.setObjectName(u"pushButton_29")
        sizePolicy.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.pushButton_29)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_18)

        self.pushButton_35 = QPushButton(self.groupBox_8)
        self.pushButton_35.setObjectName(u"pushButton_35")
        sizePolicy.setHeightForWidth(self.pushButton_35.sizePolicy().hasHeightForWidth())
        self.pushButton_35.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.pushButton_35)

        self.pushButton_36 = QPushButton(self.groupBox_8)
        self.pushButton_36.setObjectName(u"pushButton_36")
        sizePolicy.setHeightForWidth(self.pushButton_36.sizePolicy().hasHeightForWidth())
        self.pushButton_36.setSizePolicy(sizePolicy)

        self.horizontalLayout_22.addWidget(self.pushButton_36)

        self.gridLayout_36.addLayout(self.horizontalLayout_22, 2, 0, 1, 1)

        self.listWidget_3 = ImageListWidget(self.groupBox_8)
        self.listWidget_3.setObjectName(u"listWidget_3")
        self.listWidget_3.setMinimumSize(QSize(0, 150))
        self.listWidget_3.setMaximumSize(QSize(16777215, 150))

        self.gridLayout_36.addWidget(self.listWidget_3, 0, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.comboBox_10 = QComboBox(self.groupBox_8)
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        sizePolicy6.setHeightForWidth(self.comboBox_10.sizePolicy().hasHeightForWidth())
        self.comboBox_10.setSizePolicy(sizePolicy6)
        self.comboBox_10.setMinimumSize(QSize(70, 0))
        self.comboBox_10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_28.addWidget(self.comboBox_10)

        self.pushButton_27 = QPushButton(self.groupBox_8)
        self.pushButton_27.setObjectName(u"pushButton_27")
        sizePolicy.setHeightForWidth(self.pushButton_27.sizePolicy().hasHeightForWidth())
        self.pushButton_27.setSizePolicy(sizePolicy)

        self.horizontalLayout_28.addWidget(self.pushButton_27)

        self.horizontalSpacer_15 = QSpacerItem(64, 22, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_15)

        self.horizontalLayout_11.addLayout(self.horizontalLayout_28)

        self.comboBox_9 = QComboBox(self.groupBox_8)
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        sizePolicy6.setHeightForWidth(self.comboBox_9.sizePolicy().hasHeightForWidth())
        self.comboBox_9.setSizePolicy(sizePolicy6)
        self.comboBox_9.setMinimumSize(QSize(70, 0))
        self.comboBox_9.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_11.addWidget(self.comboBox_9)

        self.pushButton_26 = QPushButton(self.groupBox_8)
        self.pushButton_26.setObjectName(u"pushButton_26")
        sizePolicy.setHeightForWidth(self.pushButton_26.sizePolicy().hasHeightForWidth())
        self.pushButton_26.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.pushButton_26)

        self.horizontalLayout_9.addLayout(self.horizontalLayout_11)

        self.gridLayout_36.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.verticalLayout_8.addWidget(self.groupBox_8)

        self.gridLayout_31.addWidget(self.widget_15, 0, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        sizePolicy1.setHeightForWidth(self.tab_8.sizePolicy().hasHeightForWidth())
        self.tab_8.setSizePolicy(sizePolicy1)
        self.verticalLayout_6 = QVBoxLayout(self.tab_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.groupBox_10 = QGroupBox(self.tab_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        sizePolicy2.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy2)
        self.groupBox_10.setMinimumSize(QSize(0, 320))
        self.gridLayout_38 = QGridLayout(self.groupBox_10)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_11 = QLabel(self.groupBox_10)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_21 = QLabel(self.groupBox_10)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_38.addWidget(self.label_21, 1, 0, 1, 1)

        self.label_18 = QLabel(self.groupBox_10)
        self.label_18.setObjectName(u"label_18")
        sizePolicy3.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy3)
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.label_18, 6, 0, 1, 1)

        self.spinBox_8 = QSpinBox(self.groupBox_10)
        self.spinBox_8.setObjectName(u"spinBox_8")

        self.gridLayout_38.addWidget(self.spinBox_8, 5, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_10)
        self.label_17.setObjectName(u"label_17")
        sizePolicy3.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy3)
        self.label_17.setMinimumSize(QSize(90, 0))
        self.label_17.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_38.addWidget(self.label_17, 7, 0, 1, 1)

        self.spinBox_7 = QSpinBox(self.groupBox_10)
        self.spinBox_7.setObjectName(u"spinBox_7")

        self.gridLayout_38.addWidget(self.spinBox_7, 1, 1, 1, 2)

        self.spinBox_2 = QSpinBox(self.groupBox_10)
        self.spinBox_2.setObjectName(u"spinBox_2")

        self.gridLayout_38.addWidget(self.spinBox_2, 2, 1, 1, 2)

        self.spinBox_3 = QSpinBox(self.groupBox_10)
        self.spinBox_3.setObjectName(u"spinBox_3")

        self.gridLayout_38.addWidget(self.spinBox_3, 3, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_10)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.label_15, 5, 0, 1, 1)

        self.spinBox_13 = QSpinBox(self.groupBox_10)
        self.spinBox_13.setObjectName(u"spinBox_13")

        self.gridLayout_38.addWidget(self.spinBox_13, 5, 2, 1, 1)

        self.spinBox_9 = QSpinBox(self.groupBox_10)
        self.spinBox_9.setObjectName(u"spinBox_9")

        self.gridLayout_38.addWidget(self.spinBox_9, 6, 1, 1, 2)

        self.spinBox_5 = QSpinBox(self.groupBox_10)
        self.spinBox_5.setObjectName(u"spinBox_5")

        self.gridLayout_38.addWidget(self.spinBox_5, 3, 2, 1, 1)

        self.comboBox_8 = QComboBox(self.groupBox_10)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")

        self.gridLayout_38.addWidget(self.comboBox_8, 0, 1, 1, 2)

        self.label_12 = QLabel(self.groupBox_10)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.groupBox_10)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_38.addWidget(self.label_13, 3, 0, 1, 1)

        self.spinBox_10 = QSpinBox(self.groupBox_10)
        self.spinBox_10.setObjectName(u"spinBox_10")

        self.gridLayout_38.addWidget(self.spinBox_10, 7, 1, 1, 2)

        self.verticalLayout_6.addWidget(self.groupBox_10)

        self.groupBox_16 = QGroupBox(self.tab_8)
        self.groupBox_16.setObjectName(u"groupBox_16")
        sizePolicy2.setHeightForWidth(self.groupBox_16.sizePolicy().hasHeightForWidth())
        self.groupBox_16.setSizePolicy(sizePolicy2)
        self.groupBox_16.setSizeIncrement(QSize(0, 0))
        self.groupBox_16.setBaseSize(QSize(0, 0))
        self.gridLayout_40 = QGridLayout(self.groupBox_16)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_19 = QLabel(self.groupBox_16)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(90, 0))

        self.gridLayout_40.addWidget(self.label_19, 3, 0, 1, 1)

        self.label_16 = QLabel(self.groupBox_16)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMinimumSize(QSize(90, 0))
        font1 = QFont()
        font1.setUnderline(False)
        self.label_16.setFont(font1)
        self.label_16.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.label_16.setLayoutDirection(Qt.LeftToRight)
        self.label_16.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_16, 0, 0, 1, 1)

        self.stackedWidget_10 = QStackedWidget(self.groupBox_16)
        self.stackedWidget_10.setObjectName(u"stackedWidget_10")
        sizePolicy5.setHeightForWidth(self.stackedWidget_10.sizePolicy().hasHeightForWidth())
        self.stackedWidget_10.setSizePolicy(sizePolicy5)
        self.page_17 = QWidget()
        self.page_17.setObjectName(u"page_17")
        self.gridLayout_97 = QGridLayout(self.page_17)
        self.gridLayout_97.setObjectName(u"gridLayout_97")
        self.gridLayout_97.setVerticalSpacing(0)
        self.gridLayout_97.setContentsMargins(0, 0, 0, 0)
        self.spinBox_15 = QSpinBox(self.page_17)
        self.spinBox_15.setObjectName(u"spinBox_15")

        self.gridLayout_97.addWidget(self.spinBox_15, 0, 1, 1, 1)

        self.label_61 = QLabel(self.page_17)
        self.label_61.setObjectName(u"label_61")
        sizePolicy.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy)
        self.label_61.setMinimumSize(QSize(90, 0))

        self.gridLayout_97.addWidget(self.label_61, 0, 0, 1, 1)

        self.stackedWidget_10.addWidget(self.page_17)
        self.page_18 = QWidget()
        self.page_18.setObjectName(u"page_18")
        self.gridLayout_58 = QGridLayout(self.page_18)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_58.setVerticalSpacing(0)
        self.gridLayout_58.setContentsMargins(0, 0, 0, 0)
        self.comboBox_30 = QComboBox(self.page_18)
        self.comboBox_30.setObjectName(u"comboBox_30")

        self.gridLayout_58.addWidget(self.comboBox_30, 0, 1, 1, 1)

        self.label_62 = QLabel(self.page_18)
        self.label_62.setObjectName(u"label_62")
        sizePolicy3.setHeightForWidth(self.label_62.sizePolicy().hasHeightForWidth())
        self.label_62.setSizePolicy(sizePolicy3)
        self.label_62.setMinimumSize(QSize(78, 0))

        self.gridLayout_58.addWidget(self.label_62, 0, 0, 1, 1)

        self.stackedWidget_10.addWidget(self.page_18)

        self.gridLayout_40.addWidget(self.stackedWidget_10, 4, 0, 1, 3)

        self.spinBox_6 = QSpinBox(self.groupBox_16)
        self.spinBox_6.setObjectName(u"spinBox_6")

        self.gridLayout_40.addWidget(self.spinBox_6, 0, 1, 1, 2)

        self.spinBox_4 = QSpinBox(self.groupBox_16)
        self.spinBox_4.setObjectName(u"spinBox_4")

        self.gridLayout_40.addWidget(self.spinBox_4, 1, 1, 1, 2)

        self.label_14 = QLabel(self.groupBox_16)
        self.label_14.setObjectName(u"label_14")
        sizePolicy3.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy3)
        self.label_14.setMinimumSize(QSize(90, 0))
        self.label_14.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_40.addWidget(self.label_14, 1, 0, 1, 1)

        self.comboBox_11 = QComboBox(self.groupBox_16)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")

        self.gridLayout_40.addWidget(self.comboBox_11, 3, 1, 1, 2)

        self.verticalLayout_6.addWidget(self.groupBox_16)

        self.tabWidget_5.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_55 = QGridLayout(self.tab_9)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_55.addItem(self.verticalSpacer_9, 0, 0, 1, 1)

        self.groupBox_17 = QGroupBox(self.tab_9)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setMinimumSize(QSize(0, 300))
        self.gridLayout_59 = QGridLayout(self.groupBox_17)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.checkBox_24 = QCheckBox(self.groupBox_17)
        self.checkBox_24.setObjectName(u"checkBox_24")
        sizePolicy5.setHeightForWidth(self.checkBox_24.sizePolicy().hasHeightForWidth())
        self.checkBox_24.setSizePolicy(sizePolicy5)
        self.checkBox_24.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_24.setCheckable(True)
        self.checkBox_24.setChecked(True)
        self.checkBox_24.setAutoRepeat(False)
        self.checkBox_24.setAutoExclusive(False)
        self.checkBox_24.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_24, 3, 0, 1, 1)

        self.checkBox_25 = QCheckBox(self.groupBox_17)
        self.checkBox_25.setObjectName(u"checkBox_25")
        sizePolicy5.setHeightForWidth(self.checkBox_25.sizePolicy().hasHeightForWidth())
        self.checkBox_25.setSizePolicy(sizePolicy5)
        self.checkBox_25.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_25.setCheckable(True)
        self.checkBox_25.setChecked(True)
        self.checkBox_25.setAutoRepeat(False)
        self.checkBox_25.setAutoExclusive(False)
        self.checkBox_25.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_25, 2, 0, 1, 1)

        self.checkBox_17 = QCheckBox(self.groupBox_17)
        self.checkBox_17.setObjectName(u"checkBox_17")
        sizePolicy5.setHeightForWidth(self.checkBox_17.sizePolicy().hasHeightForWidth())
        self.checkBox_17.setSizePolicy(sizePolicy5)
        self.checkBox_17.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_17.setCheckable(True)
        self.checkBox_17.setChecked(True)
        self.checkBox_17.setAutoRepeat(False)
        self.checkBox_17.setAutoExclusive(False)
        self.checkBox_17.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_17, 5, 0, 1, 1)

        self.checkBox_21 = QCheckBox(self.groupBox_17)
        self.checkBox_21.setObjectName(u"checkBox_21")
        sizePolicy5.setHeightForWidth(self.checkBox_21.sizePolicy().hasHeightForWidth())
        self.checkBox_21.setSizePolicy(sizePolicy5)
        self.checkBox_21.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_21.setCheckable(True)
        self.checkBox_21.setChecked(True)
        self.checkBox_21.setAutoRepeat(False)
        self.checkBox_21.setAutoExclusive(False)
        self.checkBox_21.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_21, 6, 0, 1, 1)

        self.checkBox_15 = QCheckBox(self.groupBox_17)
        self.checkBox_15.setObjectName(u"checkBox_15")
        sizePolicy5.setHeightForWidth(self.checkBox_15.sizePolicy().hasHeightForWidth())
        self.checkBox_15.setSizePolicy(sizePolicy5)
        self.checkBox_15.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_15.setCheckable(True)
        self.checkBox_15.setChecked(True)
        self.checkBox_15.setAutoRepeat(False)
        self.checkBox_15.setAutoExclusive(False)
        self.checkBox_15.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_15, 8, 0, 1, 1)

        self.checkBox_13 = QCheckBox(self.groupBox_17)
        self.checkBox_13.setObjectName(u"checkBox_13")
        sizePolicy5.setHeightForWidth(self.checkBox_13.sizePolicy().hasHeightForWidth())
        self.checkBox_13.setSizePolicy(sizePolicy5)
        self.checkBox_13.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_13.setCheckable(True)
        self.checkBox_13.setChecked(True)
        self.checkBox_13.setAutoRepeat(False)
        self.checkBox_13.setAutoExclusive(False)
        self.checkBox_13.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_13, 5, 1, 1, 1)

        self.checkBox_22 = QCheckBox(self.groupBox_17)
        self.checkBox_22.setObjectName(u"checkBox_22")
        sizePolicy5.setHeightForWidth(self.checkBox_22.sizePolicy().hasHeightForWidth())
        self.checkBox_22.setSizePolicy(sizePolicy5)
        self.checkBox_22.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_22.setCheckable(True)
        self.checkBox_22.setChecked(True)
        self.checkBox_22.setAutoRepeat(False)
        self.checkBox_22.setAutoExclusive(False)
        self.checkBox_22.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_22, 7, 1, 1, 1)

        self.checkBox_19 = QCheckBox(self.groupBox_17)
        self.checkBox_19.setObjectName(u"checkBox_19")
        sizePolicy5.setHeightForWidth(self.checkBox_19.sizePolicy().hasHeightForWidth())
        self.checkBox_19.setSizePolicy(sizePolicy5)
        self.checkBox_19.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_19.setCheckable(True)
        self.checkBox_19.setChecked(True)
        self.checkBox_19.setAutoRepeat(False)
        self.checkBox_19.setAutoExclusive(False)
        self.checkBox_19.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_19, 6, 1, 1, 1)

        self.checkBox_33 = QCheckBox(self.groupBox_17)
        self.checkBox_33.setObjectName(u"checkBox_33")
        sizePolicy5.setHeightForWidth(self.checkBox_33.sizePolicy().hasHeightForWidth())
        self.checkBox_33.setSizePolicy(sizePolicy5)
        self.checkBox_33.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_33.setCheckable(True)
        self.checkBox_33.setChecked(True)
        self.checkBox_33.setAutoRepeat(False)
        self.checkBox_33.setAutoExclusive(False)
        self.checkBox_33.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_33, 3, 1, 1, 1)

        self.checkBox_16 = QCheckBox(self.groupBox_17)
        self.checkBox_16.setObjectName(u"checkBox_16")
        sizePolicy5.setHeightForWidth(self.checkBox_16.sizePolicy().hasHeightForWidth())
        self.checkBox_16.setSizePolicy(sizePolicy5)
        self.checkBox_16.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_16.setCheckable(True)
        self.checkBox_16.setChecked(True)
        self.checkBox_16.setAutoRepeat(False)
        self.checkBox_16.setAutoExclusive(False)
        self.checkBox_16.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_16, 7, 0, 1, 1)

        self.checkBox_34 = QCheckBox(self.groupBox_17)
        self.checkBox_34.setObjectName(u"checkBox_34")
        sizePolicy5.setHeightForWidth(self.checkBox_34.sizePolicy().hasHeightForWidth())
        self.checkBox_34.setSizePolicy(sizePolicy5)
        self.checkBox_34.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_34.setCheckable(True)
        self.checkBox_34.setChecked(True)
        self.checkBox_34.setAutoRepeat(False)
        self.checkBox_34.setAutoExclusive(False)
        self.checkBox_34.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_34, 2, 1, 1, 1)

        self.checkBox_26 = QCheckBox(self.groupBox_17)
        self.checkBox_26.setObjectName(u"checkBox_26")
        sizePolicy5.setHeightForWidth(self.checkBox_26.sizePolicy().hasHeightForWidth())
        self.checkBox_26.setSizePolicy(sizePolicy5)
        self.checkBox_26.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_26.setCheckable(True)
        self.checkBox_26.setChecked(True)
        self.checkBox_26.setAutoRepeat(False)
        self.checkBox_26.setAutoExclusive(False)
        self.checkBox_26.setTristate(False)

        self.gridLayout_59.addWidget(self.checkBox_26, 8, 1, 1, 1)

        self.gridLayout_55.addWidget(self.groupBox_17, 1, 0, 1, 1)

        self.tabWidget_5.addTab(self.tab_9, "")

        self.gridLayout_29.addWidget(self.tabWidget_5, 1, 0, 1, 1)

        self.gridLayout_14.addWidget(self.widget_14, 0, 0, 1, 1)

        self.widget_16 = QWidget(self.page_STM)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy5.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy5)
        self.gridLayout_34 = QGridLayout(self.widget_16)
        self.gridLayout_34.setSpacing(6)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.gridLayout_34.setContentsMargins(9, 9, 9, 9)
        self.pushButton_11 = QPushButton(self.widget_16)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_34.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.pushButton_30 = QPushButton(self.widget_16)
        self.pushButton_30.setObjectName(u"pushButton_30")
        sizePolicy.setHeightForWidth(self.pushButton_30.sizePolicy().hasHeightForWidth())
        self.pushButton_30.setSizePolicy(sizePolicy)

        self.gridLayout_34.addWidget(self.pushButton_30, 0, 5, 1, 1)

        self.pushButton_32 = QPushButton(self.widget_16)
        self.pushButton_32.setObjectName(u"pushButton_32")
        sizePolicy.setHeightForWidth(self.pushButton_32.sizePolicy().hasHeightForWidth())
        self.pushButton_32.setSizePolicy(sizePolicy)

        self.gridLayout_34.addWidget(self.pushButton_32, 0, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_34.addItem(self.horizontalSpacer_16, 0, 3, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_16)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_34.addWidget(self.pushButton_12, 0, 4, 1, 1)

        self.gridLayout_14.addWidget(self.widget_16, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_STM)
        self.page_Modbus = QWidget()
        self.page_Modbus.setObjectName(u"page_Modbus")
        self.gridLayout_49 = QGridLayout(self.page_Modbus)
        self.gridLayout_49.setSpacing(0)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.gridLayout_49.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_8 = QSpacerItem(20, 364, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_49.addItem(self.verticalSpacer_8, 0, 0, 1, 1)

        self.widget_38 = QWidget(self.page_Modbus)
        self.widget_38.setObjectName(u"widget_38")
        self.gridLayout_101 = QGridLayout(self.widget_38)
        self.gridLayout_101.setObjectName(u"gridLayout_101")
        self.pushButton_49 = QPushButton(self.widget_38)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy3.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy3)

        self.gridLayout_101.addWidget(self.pushButton_49, 0, 1, 1, 1)

        self.pushButton_21 = QPushButton(self.widget_38)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout_101.addWidget(self.pushButton_21, 0, 2, 1, 1)

        self.horizontalSpacer_22 = QSpacerItem(20, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_101.addItem(self.horizontalSpacer_22, 0, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.widget_38)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.gridLayout_101.addWidget(self.pushButton_20, 0, 0, 1, 1)

        self.pushButton_50 = QPushButton(self.widget_38)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy)

        self.gridLayout_101.addWidget(self.pushButton_50, 0, 5, 1, 1)

        self.gridLayout_49.addWidget(self.widget_38, 2, 0, 1, 1)

        self.tabWidget_11 = QTabWidget(self.page_Modbus)
        self.tabWidget_11.setObjectName(u"tabWidget_11")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.gridLayout_86 = QGridLayout(self.tab_19)
        self.gridLayout_86.setObjectName(u"gridLayout_86")
        self.gridLayout_86.setHorizontalSpacing(0)
        self.gridLayout_86.setContentsMargins(0, 0, 0, 0)
        self.widget_35 = QWidget(self.tab_19)
        self.widget_35.setObjectName(u"widget_35")
        self.gridLayout_94 = QGridLayout(self.widget_35)
        self.gridLayout_94.setObjectName(u"gridLayout_94")
        self.groupBox_29 = QGroupBox(self.widget_35)
        self.groupBox_29.setObjectName(u"groupBox_29")
        self.gridLayout_104 = QGridLayout(self.groupBox_29)
        self.gridLayout_104.setObjectName(u"gridLayout_104")
        self.stackedWidget_7 = QStackedWidget(self.groupBox_29)
        self.stackedWidget_7.setObjectName(u"stackedWidget_7")
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.gridLayout_106 = QGridLayout(self.page_14)
        self.gridLayout_106.setObjectName(u"gridLayout_106")
        self.gridLayout_106.setHorizontalSpacing(6)
        self.gridLayout_106.setVerticalSpacing(0)
        self.gridLayout_106.setContentsMargins(0, 0, 0, 0)
        self.comboBox_28 = QComboBox(self.page_14)
        self.comboBox_28.addItem("")
        self.comboBox_28.setObjectName(u"comboBox_28")
        self.comboBox_28.setEnabled(True)
        self.comboBox_28.setEditable(False)

        self.gridLayout_106.addWidget(self.comboBox_28, 1, 1, 1, 1)

        self.label_59 = QLabel(self.page_14)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_106.addWidget(self.label_59, 1, 0, 1, 1)

        self.stackedWidget_7.addWidget(self.page_14)
        self.page_15 = QWidget()
        self.page_15.setObjectName(u"page_15")
        self.gridLayout_107 = QGridLayout(self.page_15)
        self.gridLayout_107.setObjectName(u"gridLayout_107")
        self.gridLayout_107.setVerticalSpacing(0)
        self.gridLayout_107.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.page_15)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_107.addWidget(self.label_60, 0, 0, 1, 1)

        self.comboBox_29 = QComboBox(self.page_15)
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.addItem("")
        self.comboBox_29.setObjectName(u"comboBox_29")

        self.gridLayout_107.addWidget(self.comboBox_29, 0, 1, 1, 1)

        self.stackedWidget_7.addWidget(self.page_15)

        self.gridLayout_104.addWidget(self.stackedWidget_7, 1, 0, 1, 2)

        self.comboBox_27 = QComboBox(self.groupBox_29)
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.addItem("")
        self.comboBox_27.setObjectName(u"comboBox_27")

        self.gridLayout_104.addWidget(self.comboBox_27, 0, 1, 1, 1)

        self.label_58 = QLabel(self.groupBox_29)
        self.label_58.setObjectName(u"label_58")
        sizePolicy1.setHeightForWidth(self.label_58.sizePolicy().hasHeightForWidth())
        self.label_58.setSizePolicy(sizePolicy1)
        self.label_58.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_104.addWidget(self.label_58, 0, 0, 1, 1)

        self.gridLayout_94.addWidget(self.groupBox_29, 4, 0, 1, 1)

        self.stackedWidget_6 = QStackedWidget(self.widget_35)
        self.stackedWidget_6.setObjectName(u"stackedWidget_6")
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.gridLayout_53 = QGridLayout(self.page_12)
        self.gridLayout_53.setSpacing(0)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.gridLayout_53.setContentsMargins(0, 0, 0, 0)
        self.groupBox_28 = QGroupBox(self.page_12)
        self.groupBox_28.setObjectName(u"groupBox_28")
        self.gridLayout_54 = QGridLayout(self.groupBox_28)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.lineEdit_5 = QLineEdit(self.groupBox_28)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy5.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy5)
        self.lineEdit_5.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_54.addWidget(self.lineEdit_5, 1, 1, 1, 1)

        self.label_52 = QLabel(self.groupBox_28)
        self.label_52.setObjectName(u"label_52")
        sizePolicy8.setHeightForWidth(self.label_52.sizePolicy().hasHeightForWidth())
        self.label_52.setSizePolicy(sizePolicy8)
        self.label_52.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_54.addWidget(self.label_52, 1, 0, 1, 1)

        self.label_51 = QLabel(self.groupBox_28)
        self.label_51.setObjectName(u"label_51")
        sizePolicy8.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy8)
        self.label_51.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_54.addWidget(self.label_51, 0, 0, 1, 1)

        self.lineEdit_4 = QLineEdit(self.groupBox_28)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_54.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.gridLayout_53.addWidget(self.groupBox_28, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.page_12)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.gridLayout_105 = QGridLayout(self.page_13)
        self.gridLayout_105.setSpacing(0)
        self.gridLayout_105.setObjectName(u"gridLayout_105")
        self.gridLayout_105.setContentsMargins(0, 0, 0, 0)
        self.groupBox_31 = QGroupBox(self.page_13)
        self.groupBox_31.setObjectName(u"groupBox_31")
        self.gridLayout_18 = QGridLayout(self.groupBox_31)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_53 = QLabel(self.groupBox_31)
        self.label_53.setObjectName(u"label_53")
        sizePolicy1.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy1)
        self.label_53.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_17.addWidget(self.label_53)

        self.comboBox_22 = QComboBox(self.groupBox_31)
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")
        sizePolicy9.setHeightForWidth(self.comboBox_22.sizePolicy().hasHeightForWidth())
        self.comboBox_22.setSizePolicy(sizePolicy9)

        self.horizontalLayout_17.addWidget(self.comboBox_22)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_29)

        self.label_49 = QLabel(self.groupBox_31)
        self.label_49.setObjectName(u"label_49")
        sizePolicy8.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy8)
        self.label_49.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_17.addWidget(self.label_49)

        self.comboBox_21 = QComboBox(self.groupBox_31)
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        sizePolicy9.setHeightForWidth(self.comboBox_21.sizePolicy().hasHeightForWidth())
        self.comboBox_21.setSizePolicy(sizePolicy9)

        self.horizontalLayout_17.addWidget(self.comboBox_21)

        self.gridLayout_18.addLayout(self.horizontalLayout_17, 0, 0, 1, 1)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_57 = QLabel(self.groupBox_31)
        self.label_57.setObjectName(u"label_57")
        sizePolicy1.setHeightForWidth(self.label_57.sizePolicy().hasHeightForWidth())
        self.label_57.setSizePolicy(sizePolicy1)
        self.label_57.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_27.addWidget(self.label_57)

        self.comboBox_26 = QComboBox(self.groupBox_31)
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.setObjectName(u"comboBox_26")
        sizePolicy9.setHeightForWidth(self.comboBox_26.sizePolicy().hasHeightForWidth())
        self.comboBox_26.setSizePolicy(sizePolicy9)

        self.horizontalLayout_27.addWidget(self.comboBox_26)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_24)

        self.label_56 = QLabel(self.groupBox_31)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_27.addWidget(self.label_56)

        self.comboBox_25 = QComboBox(self.groupBox_31)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")
        sizePolicy9.setHeightForWidth(self.comboBox_25.sizePolicy().hasHeightForWidth())
        self.comboBox_25.setSizePolicy(sizePolicy9)

        self.horizontalLayout_27.addWidget(self.comboBox_25)

        self.gridLayout_18.addLayout(self.horizontalLayout_27, 2, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_54 = QLabel(self.groupBox_31)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_26.addWidget(self.label_54)

        self.comboBox_23 = QComboBox(self.groupBox_31)
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        sizePolicy9.setHeightForWidth(self.comboBox_23.sizePolicy().hasHeightForWidth())
        self.comboBox_23.setSizePolicy(sizePolicy9)

        self.horizontalLayout_26.addWidget(self.comboBox_23)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_23)

        self.label_55 = QLabel(self.groupBox_31)
        self.label_55.setObjectName(u"label_55")
        sizePolicy1.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy1)
        self.label_55.setMinimumSize(QSize(60, 0))

        self.horizontalLayout_26.addWidget(self.label_55)

        self.comboBox_24 = QComboBox(self.groupBox_31)
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.setObjectName(u"comboBox_24")
        sizePolicy9.setHeightForWidth(self.comboBox_24.sizePolicy().hasHeightForWidth())
        self.comboBox_24.setSizePolicy(sizePolicy9)

        self.horizontalLayout_26.addWidget(self.comboBox_24)

        self.gridLayout_18.addLayout(self.horizontalLayout_26, 1, 0, 1, 1)

        self.gridLayout_105.addWidget(self.groupBox_31, 0, 0, 1, 1)

        self.stackedWidget_6.addWidget(self.page_13)

        self.gridLayout_94.addWidget(self.stackedWidget_6, 2, 0, 1, 1)

        self.stackedWidget_9 = QStackedWidget(self.widget_35)
        self.stackedWidget_9.setObjectName(u"stackedWidget_9")
        self.page_19 = QWidget()
        self.page_19.setObjectName(u"page_19")
        self.gridLayout_114 = QGridLayout(self.page_19)
        self.gridLayout_114.setSpacing(0)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.gridLayout_114.setContentsMargins(0, 0, 0, 0)
        self.groupBox_34 = QGroupBox(self.page_19)
        self.groupBox_34.setObjectName(u"groupBox_34")
        self.gridLayout_113 = QGridLayout(self.groupBox_34)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.label_76 = QLabel(self.groupBox_34)
        self.label_76.setObjectName(u"label_76")
        sizePolicy3.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy3)
        self.label_76.setMinimumSize(QSize(60, 0))
        self.label_76.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_113.addWidget(self.label_76, 0, 0, 1, 1)

        self.label_79 = QLabel(self.groupBox_34)
        self.label_79.setObjectName(u"label_79")
        sizePolicy3.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy3)
        self.label_79.setMinimumSize(QSize(60, 0))

        self.gridLayout_113.addWidget(self.label_79, 0, 3, 1, 1)

        self.comboBox_39 = QComboBox(self.groupBox_34)
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.addItem("")
        self.comboBox_39.setObjectName(u"comboBox_39")

        self.gridLayout_113.addWidget(self.comboBox_39, 0, 1, 1, 1)

        self.spinBox_20 = QSpinBox(self.groupBox_34)
        self.spinBox_20.setObjectName(u"spinBox_20")
        sizePolicy.setHeightForWidth(self.spinBox_20.sizePolicy().hasHeightForWidth())
        self.spinBox_20.setSizePolicy(sizePolicy)
        self.spinBox_20.setMinimum(1)
        self.spinBox_20.setMaximum(9999)

        self.gridLayout_113.addWidget(self.spinBox_20, 0, 4, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_113.addItem(self.horizontalSpacer_12, 0, 2, 1, 1)

        self.gridLayout_114.addWidget(self.groupBox_34, 0, 0, 1, 1)

        self.stackedWidget_9.addWidget(self.page_19)
        self.page_20 = QWidget()
        self.page_20.setObjectName(u"page_20")
        self.gridLayout_116 = QGridLayout(self.page_20)
        self.gridLayout_116.setSpacing(0)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.gridLayout_116.setContentsMargins(0, 0, 0, 0)
        self.groupBox_44 = QGroupBox(self.page_20)
        self.groupBox_44.setObjectName(u"groupBox_44")
        self.gridLayout_115 = QGridLayout(self.groupBox_44)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.comboBox_40 = QComboBox(self.groupBox_44)
        self.comboBox_40.addItem("")
        self.comboBox_40.addItem("")
        self.comboBox_40.setObjectName(u"comboBox_40")

        self.gridLayout_115.addWidget(self.comboBox_40, 1, 1, 1, 1)

        self.label_77 = QLabel(self.groupBox_44)
        self.label_77.setObjectName(u"label_77")
        sizePolicy3.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy3)
        self.label_77.setMinimumSize(QSize(60, 0))
        self.label_77.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_115.addWidget(self.label_77, 1, 0, 1, 1)

        self.label_78 = QLabel(self.groupBox_44)
        self.label_78.setObjectName(u"label_78")
        sizePolicy3.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy3)
        self.label_78.setMinimumSize(QSize(60, 0))
        self.label_78.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_115.addWidget(self.label_78, 0, 0, 1, 1)

        self.comboBox_41 = QComboBox(self.groupBox_44)
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.addItem("")
        self.comboBox_41.setObjectName(u"comboBox_41")

        self.gridLayout_115.addWidget(self.comboBox_41, 0, 1, 1, 1)

        self.gridLayout_116.addWidget(self.groupBox_44, 0, 0, 1, 1)

        self.stackedWidget_9.addWidget(self.page_20)

        self.gridLayout_94.addWidget(self.stackedWidget_9, 3, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.widget_35)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_50 = QGridLayout(self.groupBox_5)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_69 = QLabel(self.groupBox_5)
        self.label_69.setObjectName(u"label_69")
        sizePolicy1.setHeightForWidth(self.label_69.sizePolicy().hasHeightForWidth())
        self.label_69.setSizePolicy(sizePolicy1)
        self.label_69.setMinimumSize(QSize(0, 0))

        self.gridLayout_50.addWidget(self.label_69, 2, 0, 1, 1)

        self.comboBox_20 = QComboBox(self.groupBox_5)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")

        self.gridLayout_50.addWidget(self.comboBox_20, 0, 1, 1, 1)

        self.spinBox_14 = QSpinBox(self.groupBox_5)
        self.spinBox_14.setObjectName(u"spinBox_14")

        self.gridLayout_50.addWidget(self.spinBox_14, 1, 1, 1, 1)

        self.label_50 = QLabel(self.groupBox_5)
        self.label_50.setObjectName(u"label_50")

        self.gridLayout_50.addWidget(self.label_50, 1, 0, 1, 1)

        self.label_39 = QLabel(self.groupBox_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMaximumSize(QSize(60, 16777215))
        self.label_39.setLayoutDirection(Qt.LeftToRight)
        self.label_39.setTextFormat(Qt.AutoText)
        self.label_39.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_50.addWidget(self.label_39, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(89, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_50.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.spinBox_17 = QSpinBox(self.groupBox_5)
        self.spinBox_17.setObjectName(u"spinBox_17")
        sizePolicy9.setHeightForWidth(self.spinBox_17.sizePolicy().hasHeightForWidth())
        self.spinBox_17.setSizePolicy(sizePolicy9)
        self.spinBox_17.setMinimum(1)

        self.gridLayout_50.addWidget(self.spinBox_17, 2, 1, 1, 1)

        self.label_68 = QLabel(self.groupBox_5)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout_50.addWidget(self.label_68, 0, 3, 1, 1)

        self.comboBox_33 = QComboBox(self.groupBox_5)
        self.comboBox_33.addItem("")
        self.comboBox_33.addItem("")
        self.comboBox_33.setObjectName(u"comboBox_33")

        self.gridLayout_50.addWidget(self.comboBox_33, 0, 4, 1, 1)

        self.label_70 = QLabel(self.groupBox_5)
        self.label_70.setObjectName(u"label_70")
        sizePolicy3.setHeightForWidth(self.label_70.sizePolicy().hasHeightForWidth())
        self.label_70.setSizePolicy(sizePolicy3)

        self.gridLayout_50.addWidget(self.label_70, 1, 3, 1, 1)

        self.spinBox_18 = QSpinBox(self.groupBox_5)
        self.spinBox_18.setObjectName(u"spinBox_18")
        sizePolicy9.setHeightForWidth(self.spinBox_18.sizePolicy().hasHeightForWidth())
        self.spinBox_18.setSizePolicy(sizePolicy9)
        self.spinBox_18.setMinimum(0)
        self.spinBox_18.setValue(0)

        self.gridLayout_50.addWidget(self.spinBox_18, 1, 4, 1, 1)

        self.gridLayout_94.addWidget(self.groupBox_5, 1, 0, 1, 1)

        self.groupBox_30 = QGroupBox(self.widget_35)
        self.groupBox_30.setObjectName(u"groupBox_30")
        self.gridLayout_96 = QGridLayout(self.groupBox_30)
        self.gridLayout_96.setObjectName(u"gridLayout_96")
        self.label_81 = QLabel(self.groupBox_30)
        self.label_81.setObjectName(u"label_81")
        sizePolicy3.setHeightForWidth(self.label_81.sizePolicy().hasHeightForWidth())
        self.label_81.setSizePolicy(sizePolicy3)
        self.label_81.setMinimumSize(QSize(60, 0))

        self.gridLayout_96.addWidget(self.label_81, 0, 0, 1, 1)

        self.comboBox_43 = QComboBox(self.groupBox_30)
        self.comboBox_43.setObjectName(u"comboBox_43")
        self.comboBox_43.setEditable(True)

        self.gridLayout_96.addWidget(self.comboBox_43, 0, 1, 1, 1)

        self.gridLayout_94.addWidget(self.groupBox_30, 0, 0, 1, 1)

        self.gridLayout_86.addWidget(self.widget_35, 0, 0, 1, 1)

        self.tabWidget_11.addTab(self.tab_19, "")

        self.gridLayout_49.addWidget(self.tabWidget_11, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_Modbus)
        self.widget_38.raise_()
        self.tabWidget_11.raise_()
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_60 = QGridLayout(self.page_4)
        self.gridLayout_60.setSpacing(0)
        self.gridLayout_60.setObjectName(u"gridLayout_60")
        self.gridLayout_60.setContentsMargins(0, 0, 0, 0)
        self.widget_30 = QWidget(self.page_4)
        self.widget_30.setObjectName(u"widget_30")
        sizePolicy5.setHeightForWidth(self.widget_30.sizePolicy().hasHeightForWidth())
        self.widget_30.setSizePolicy(sizePolicy5)
        self.gridLayout_62 = QGridLayout(self.widget_30)
        self.gridLayout_62.setObjectName(u"gridLayout_62")
        self.gridLayout_62.setContentsMargins(20, -1, 22, -1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_62.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.widget_30)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.gridLayout_62.addWidget(self.pushButton_19, 0, 2, 1, 1)

        self.gridLayout_60.addWidget(self.widget_30, 2, 0, 1, 1)

        self.tabWidget_7 = QTabWidget(self.page_4)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_61 = QGridLayout(self.tab_12)
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.groupBox_18 = QGroupBox(self.tab_12)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.gridLayout_79 = QGridLayout(self.groupBox_18)
        self.gridLayout_79.setObjectName(u"gridLayout_79")
        self.tableWidget_2 = OutputtableWidget(self.groupBox_18)
        if (self.tableWidget_2.columnCount() < 2):
            self.tableWidget_2.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        sizePolicy6.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy6)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setStretchLastSection(False)

        self.gridLayout_79.addWidget(self.tableWidget_2, 0, 0, 1, 1)

        self.gridLayout_61.addWidget(self.groupBox_18, 0, 0, 1, 1)

        self.tabWidget_7.addTab(self.tab_12, "")

        self.gridLayout_60.addWidget(self.tabWidget_7, 1, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_60.addItem(self.verticalSpacer_10, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_add = QWidget()
        self.page_add.setObjectName(u"page_add")
        self.gridLayout_35 = QGridLayout(self.page_add)
        self.gridLayout_35.setSpacing(0)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_12 = QTabWidget(self.page_add)
        self.tabWidget_12.setObjectName(u"tabWidget_12")
        sizePolicy9.setHeightForWidth(self.tabWidget_12.sizePolicy().hasHeightForWidth())
        self.tabWidget_12.setSizePolicy(sizePolicy9)
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.gridLayout_99 = QGridLayout(self.tab_20)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.groupBox_15 = QGroupBox(self.tab_20)
        self.groupBox_15.setObjectName(u"groupBox_15")
        sizePolicy5.setHeightForWidth(self.groupBox_15.sizePolicy().hasHeightForWidth())
        self.groupBox_15.setSizePolicy(sizePolicy5)
        self.gridLayout_109 = QGridLayout(self.groupBox_15)
        self.gridLayout_109.setObjectName(u"gridLayout_109")
        self.label_63 = QLabel(self.groupBox_15)
        self.label_63.setObjectName(u"label_63")

        self.gridLayout_109.addWidget(self.label_63, 0, 0, 1, 1)

        self.comboBox_31 = QComboBox(self.groupBox_15)
        self.comboBox_31.addItem("")
        self.comboBox_31.addItem("")
        self.comboBox_31.addItem("")
        self.comboBox_31.setObjectName(u"comboBox_31")

        self.gridLayout_109.addWidget(self.comboBox_31, 0, 1, 1, 1)

        self.label_64 = QLabel(self.groupBox_15)
        self.label_64.setObjectName(u"label_64")

        self.gridLayout_109.addWidget(self.label_64, 1, 0, 1, 1)

        self.spinBox_16 = QSpinBox(self.groupBox_15)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setMinimum(2)
        self.spinBox_16.setMaximum(10)

        self.gridLayout_109.addWidget(self.spinBox_16, 1, 1, 1, 1)

        self.gridLayout_99.addWidget(self.groupBox_15, 0, 0, 1, 1)

        self.tabWidget_12.addTab(self.tab_20, "")

        self.gridLayout_35.addWidget(self.tabWidget_12, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_35.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.widget_36 = QWidget(self.page_add)
        self.widget_36.setObjectName(u"widget_36")
        sizePolicy5.setHeightForWidth(self.widget_36.sizePolicy().hasHeightForWidth())
        self.widget_36.setSizePolicy(sizePolicy5)
        self.gridLayout_110 = QGridLayout(self.widget_36)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.gridLayout_110.setContentsMargins(20, -1, 22, -1)
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_110.addItem(self.horizontalSpacer_25, 0, 1, 1, 1)

        self.pushButton_40 = QPushButton(self.widget_36)
        self.pushButton_40.setObjectName(u"pushButton_40")

        self.gridLayout_110.addWidget(self.pushButton_40, 0, 2, 1, 1)

        self.gridLayout_35.addWidget(self.widget_36, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_add)
        self.page_Split = QWidget()
        self.page_Split.setObjectName(u"page_Split")
        self.stackedWidget.addWidget(self.page_Split)

        self.verticalLayout_2.addWidget(self.stackedWidget)

        self.verticalLayout.addWidget(self.widget_4)

        self.tabWidget_2.addTab(self.tab_3, "")

        self.gridLayout_3.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.widget_3, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 0, 0)
        self.treeWidget = QTreeWidget(self.tab_2)
        icon7 = QIcon()
        icon7.addFile(u":/\u5217\u8868/icon/icon_\u5217\u8868.png", QSize(), QIcon.Normal, QIcon.Off)
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(True)
        font2.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setFont(0, font2);
        __qtreewidgetitem.setIcon(0, icon7);
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        icon8 = QIcon()
        icon8.addFile(u":/\u89c6\u89c9/icon/\u56fe\u50cf\u7c7b\u578b.png", QSize(), QIcon.Normal, QIcon.Off)
        brush = QBrush(QColor(0, 85, 127, 255))
        brush.setStyle(Qt.NoBrush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.NoBrush)
        font3 = QFont()
        font3.setFamily(u"\u534e\u6587\u65b0\u9b4f")
        font3.setPointSize(18)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        font3.setWeight(50)
        icon9 = QIcon()
        icon9.addFile(u":/\u89c6\u89c9/icon/\u6a21\u677f\u5339\u914d.png", QSize(), QIcon.Normal, QIcon.Off)
        brush2 = QBrush(QColor(0, 85, 127, 255))
        brush2.setStyle(Qt.NoBrush)
        font4 = QFont()
        font4.setFamily(u"\u534e\u6587\u65b0\u9b4f")
        font4.setPointSize(18)
        icon10 = QIcon()
        icon10.addFile(u":/\u89c6\u89c9/icon/\u989c\u8272\u8bc6\u522b.png", QSize(), QIcon.Normal, QIcon.Off)
        brush3 = QBrush(QColor(0, 85, 127, 255))
        brush3.setStyle(Qt.NoBrush)
        icon11 = QIcon()
        icon11.addFile(u":/\u89c6\u89c9/icon/\u76f8\u673a\u6807\u5b9a.png", QSize(), QIcon.Normal, QIcon.Off)
        brush4 = QBrush(QColor(0, 85, 127, 255))
        brush4.setStyle(Qt.NoBrush)
        icon12 = QIcon()
        icon12.addFile(u":/\u89c6\u89c9/icon/Modbus\u901a\u8baf-z.png", QSize(), QIcon.Normal, QIcon.Off)
        brush5 = QBrush(QColor(0, 85, 127, 255))
        brush5.setStyle(Qt.NoBrush)
        icon13 = QIcon()
        icon13.addFile(u":/\u89c6\u89c9/icon/\u6570\u636e\u8f6c\u6362.png", QSize(), QIcon.Normal, QIcon.Off)
        brush6 = QBrush(QColor(0, 85, 127, 255))
        brush6.setStyle(Qt.NoBrush)
        icon14 = QIcon()
        icon14.addFile(u":/\u7bad\u5934/icon/\u53f3\u7bad\u5934.png", QSize(), QIcon.Normal, QIcon.Off)
        brush7 = QBrush(QColor(0, 85, 127, 255))
        brush7.setStyle(Qt.NoBrush)
        brush8 = QBrush(QColor(0, 85, 127, 255))
        brush8.setStyle(Qt.NoBrush)
        brush9 = QBrush(QColor(0, 85, 127, 255))
        brush9.setStyle(Qt.NoBrush)
        brush10 = QBrush(QColor(0, 0, 0, 255))
        brush10.setStyle(Qt.NoBrush)
        __qtreewidgetitem1 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1.setTextAlignment(0, Qt.AlignLeading | Qt.AlignVCenter);
        __qtreewidgetitem1.setFont(0, font3);
        __qtreewidgetitem1.setBackground(0, brush1);
        __qtreewidgetitem1.setForeground(0, brush);
        __qtreewidgetitem1.setIcon(0, icon8);
        __qtreewidgetitem2 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem2.setFont(0, font4);
        __qtreewidgetitem2.setForeground(0, brush2);
        __qtreewidgetitem2.setIcon(0, icon9);
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem3.setFont(0, font4);
        __qtreewidgetitem3.setForeground(0, brush3);
        __qtreewidgetitem3.setIcon(0, icon10);
        __qtreewidgetitem4 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem4.setFont(0, font4);
        __qtreewidgetitem4.setForeground(0, brush4);
        __qtreewidgetitem4.setIcon(0, icon11);
        __qtreewidgetitem5 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem5.setFont(0, font4);
        __qtreewidgetitem5.setForeground(0, brush5);
        __qtreewidgetitem5.setIcon(0, icon12);
        __qtreewidgetitem6 = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem6.setFont(0, font4);
        __qtreewidgetitem6.setForeground(0, brush6);
        __qtreewidgetitem6.setIcon(0, icon13);
        __qtreewidgetitem7 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem7.setFont(0, font4);
        __qtreewidgetitem7.setForeground(0, brush7);
        __qtreewidgetitem7.setIcon(0, icon14);
        __qtreewidgetitem8 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem8.setFont(0, font4);
        __qtreewidgetitem8.setForeground(0, brush8);
        __qtreewidgetitem8.setIcon(0, icon14);
        __qtreewidgetitem9 = QTreeWidgetItem(__qtreewidgetitem6)
        __qtreewidgetitem9.setFont(0, font4);
        __qtreewidgetitem9.setBackground(0, brush10);
        __qtreewidgetitem9.setForeground(0, brush9);
        __qtreewidgetitem9.setIcon(0, icon14);
        QTreeWidgetItem(__qtreewidgetitem6)
        self.treeWidget.setObjectName(u"treeWidget")
        sizePolicy3.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy3)
        self.treeWidget.setMaximumSize(QSize(250, 16777215))
        self.treeWidget.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setIconSize(QSize(42, 42))
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.header().setCascadingSectionResizes(False)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setLayoutDirection(Qt.LeftToRight)
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.gridLayout_32 = QGridLayout(self.widget_2)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.label_20 = QLabel(self.widget_2)
        self.label_20.setObjectName(u"label_20")
        sizePolicy1.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy1)

        self.gridLayout_32.addWidget(self.label_20, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.widget_2)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayout_13.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_14.addWidget(self.widget_1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(1)
        self.stackedWidget_8.setCurrentIndex(1)
        self.stackedWidget_14.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(1)
        self.tabWidget_5.setCurrentIndex(2)
        self.stackedWidget_10.setCurrentIndex(0)
        self.tabWidget_11.setCurrentIndex(0)
        self.stackedWidget_7.setCurrentIndex(0)
        self.stackedWidget_6.setCurrentIndex(1)
        self.stackedWidget_9.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_12.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u5de5\u4e1a\u89c6\u89c9\u96c6\u6210\u5e73\u53f0", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u6587\u4ef6", None))
        # if QT_CONFIG(tooltip)
        self.action.setToolTip(QCoreApplication.translate("MainWindow", u"file", None))
        # endif // QT_CONFIG(tooltip)
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        # if QT_CONFIG(tooltip)
        self.action_2.setToolTip(QCoreApplication.translate("MainWindow", u"run", None))
        # endif // QT_CONFIG(tooltip)
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        # if QT_CONFIG(tooltip)
        self.action_3.setToolTip(QCoreApplication.translate("MainWindow", u"over", None))
        # endif // QT_CONFIG(tooltip)
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u6392\u7248", None))
        # if QT_CONFIG(tooltip)
        self.action_4.setToolTip(QCoreApplication.translate("MainWindow", u"\u6392\u7248", None))
        # endif // QT_CONFIG(tooltip)
        self.actionlogo.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        # if QT_CONFIG(tooltip)
        self.actionlogo.setToolTip(QCoreApplication.translate("MainWindow", u"logo", None))
        # endif // QT_CONFIG(tooltip)
        self.toolButton_14.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u884c", None))
        self.toolButton_15.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.label_44.setText(
            QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u8fde\u63a5\u72b6\u6001\uff1a", None))
        self.label_42.setText("")
        # if QT_CONFIG(statustip)
        self.stackedWidget.setStatusTip(QCoreApplication.translate("MainWindow", u"1000000", None))
        # endif // QT_CONFIG(statustip)
        self.groupBox_13.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u72b6\u6001", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u77e9\u9635\uff1a", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u4f4d\u79fb\u77e9\u9635\uff1a", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u8bef\u5dee\uff1a", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u70b9", None))
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_172.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_174.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_177.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_23.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u70b9", None))
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_180.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_183.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.lineEdit_4_1_1.setText("")
        self.label_186.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.groupBox_24.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u70b9", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_25.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u70b9", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_35.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u70b9", None))
        self.label_283.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_284.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_285.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_286.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_287.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_288.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_289.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_290.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_36.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u516b\u70b9", None))
        self.label_291.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_292.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_293.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_294.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_295.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_296.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_297.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.lineEdit_9_8_1.setText("")
        self.label_298.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.groupBox_37.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e5d\u70b9", None))
        self.label_299.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_300.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_301.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_302.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_303.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_304.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_305.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.lineEdit_9_9_1.setText("")
        self.label_306.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.groupBox_38.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e03\u70b9", None))
        self.label_307.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_308.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_309.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_310.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_312.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_313.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.lineEdit_9_7_1.setText("")
        self.label_314.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.groupBox_39.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u70b9", None))
        self.label_315.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_316.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_317.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_318.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_319.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_320.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_321.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_322.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_40.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u70b9", None))
        self.label_323.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_324.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_325.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_326.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_327.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_328.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_329.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_330.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.lineEdit_9_1_1.setText("")
        self.groupBox_41.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u516d\u70b9", None))
        self.label_335.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.lineEdit_9_6_1.setText("")
        self.label_333.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_331.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_334.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_332.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_338.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_337.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_336.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_42.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e94\u70b9", None))
        self.label_339.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_340.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_341.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_342.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_343.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.label_344.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_345.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_346.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.groupBox_43.setTitle(QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u70b9", None))
        self.label_347.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfX", None))
        self.label_348.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.label_349.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_350.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807Y", None))
        self.label_351.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807X", None))
        self.label_352.setText(QCoreApplication.translate("MainWindow", u"mm", None))
        self.label_353.setText(QCoreApplication.translate("MainWindow", u"Pix", None))
        self.lineEdit_9_3_1.setText("")
        self.label_354.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cfY", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u65b9\u6cd5", None))
        self.pushButton_38.setText(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u65b9\u5f0f", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"\u56db\u70b9\u6807\u5b9a", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e5d\u70b9\u6807\u5b9a", None))

        self.groupBox_12.setTitle(
            QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u76ee\u6807\u83b7\u53d6", None))
        self.pushButton_33.setText(QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u9009\u53d6", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e00\u70b9", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e8c\u70b9", None))
        self.comboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7b2c\u4e09\u70b9", None))
        self.comboBox_15.setItemText(3, QCoreApplication.translate("MainWindow", u"\u7b2c\u56db\u70b9", None))

        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u641c\u7d22", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u5706:", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f:", None))
        self.groupBox_32.setTitle(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u540d\u79f0", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u6807\u5b9a\u540d\u79f0\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6807\u5b9a", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab),
                                    QCoreApplication.translate("MainWindow", u"\u6807\u5750\u6807\u5b9a", None))
        # if QT_CONFIG(tooltip)
        self.page_CR.setToolTip(QCoreApplication.translate("MainWindow",
                                                           u"<html><head/><body><p>\u989c\u8272\u8bc6\u522b</p></body></html>",
                                                           None))
        # endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6837\u672c\u5217\u8868", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("MainWindow", u"\u989c\u8272\u8bc6\u522b", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6d4b\u8bd5", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6d4b\u8bd5\uff1a", None))
        self.pushButton_23.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u6837\u672c", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u8bad\u7ec3\u6837\u672c\uff1a", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u8fed\u4ee3\u6b21\u6570\uff1a", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"\u77e9\u5f62", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5706\u5f62", None))
        self.comboBox_12.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5706\u73af", None))

        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u6d4b\u533a\u57df", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("MainWindow", u"\u989c\u8272\u6837\u672c", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u6837\u672c\u540d\u79f0\uff1a", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u6837\u672c\u533a\u57df\uff1a", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"\u77e9\u5f62", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5706\u5f62", None))

        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u533a\u57df", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainWindow", u"\u6837\u672c\u91c7\u96c6", None))
        self.pushButton_39.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_10),
                                    QCoreApplication.translate("MainWindow", u"\u989c\u8272\u8bc6\u522b", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u6e90", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u91c7\u96c6", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u6765\u6e90\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u6587\u4ef6", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6a21\u677f", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8def\u5f84\uff1a", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5c55\u793a", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u53c2\u6570", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c\u65b9\u5411\uff1a", None))
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5", None))
        self.pushButton_44.setText(QCoreApplication.translate("MainWindow", u"\u65ad\u5f00", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u56fe\u50cf", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"\u624b\u52a8\u89e6\u53d1", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5b9a\u65f6\u89e6\u53d1", None))
        self.comboBox_14.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5916\u90e8\u89e6\u53d1", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673aIP\uff1a", None))
        self.comboBox_17.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6b63\u5e38", None))
        self.comboBox_17.setItemText(1, QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c90\u5ea6", None))
        self.comboBox_17.setItemText(2, QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c180\u5ea6", None))
        self.comboBox_17.setItemText(3, QCoreApplication.translate("MainWindow", u"\u65cb\u8f6c270\u5ea6", None))
        self.comboBox_17.setItemText(4, QCoreApplication.translate("MainWindow", u"\u4e0a\u4e0b\u7ffb\u8f6c", None))
        self.comboBox_17.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5de6\u53f3\u955c\u50cf", None))

        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u540d\u79f0\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u54c1\u724c\uff1a   ", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6d77\u5eb7\u5a01\u89c6", None))

        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u65b9\u5f0f\uff1a", None))
        self.groupBox_33.setTitle(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u6761\u4ef6", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u8f83\u503c\uff1a", None))
        self.comboBox_34.setItemText(0, QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u6570\u636e", None))

        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u8f83\u6761\u4ef6\uff1a", None))
        self.comboBox_42.setItemText(0, QCoreApplication.translate("MainWindow", u"=", None))
        self.comboBox_42.setItemText(1, QCoreApplication.translate("MainWindow", u">", None))
        self.comboBox_42.setItemText(2, QCoreApplication.translate("MainWindow", u"<", None))
        self.comboBox_42.setItemText(3, QCoreApplication.translate("MainWindow", u">=", None))
        self.comboBox_42.setItemText(4, QCoreApplication.translate("MainWindow", u"<=", None))

        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u6bd4\u8f83\u503c\uff1a", None))
        self.comboBox_44.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_44.setItemText(1, QCoreApplication.translate("MainWindow", u"OK", None))
        self.comboBox_44.setItemText(2, QCoreApplication.translate("MainWindow", u"NG", None))

        self.pushButton_31.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u6536\u8bbe\u7f6e", None))
        self.groupBox_27.setTitle(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u95f4\u9694", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u89e6\u53d1\u95f4\u9694(ms)\uff1a", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u4e3a\u6a21\u677f", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_5),
                                    QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u6570\u636e", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("MainWindow", u"\u5e38\u7528\u5c5e\u6027", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u9891\u7387(fps)\uff1a", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u66dd\u5149\uff1a", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u66dd\u5149\u65f6\u95f4(us)\uff1a", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u52a8\u589e\u76ca\uff1a", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8fde\u7eed", None))

        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u589e\u76ca(db)\uff1a", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u4eae\u5ea6\uff1a", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u8272\u8c03\u4f7f\u80fd\uff1a", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u8272\u8c03\uff1a", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u9971\u548c\u5ea6\u4f7f\u80fd\uff1a", None))
        self.label_92.setText(
            QCoreApplication.translate("MainWindow", u"\u4f3d\u9a6c\u77eb\u6b63\u4f7f\u80fd\uff1a", None))
        self.label_93.setText(
            QCoreApplication.translate("MainWindow", u"\u4f3d\u9a6c\u77eb\u6b63\u9009\u62e9\u5668\uff1a", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7528\u6237", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"sRGB", None))

        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u4f3d\u9a6c\u77eb\u6b63\uff1a", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"\u767d\u5e73\u8861\uff1a", None))
        self.radioButton_3.setText("")
        self.radioButton_4.setText("")
        self.radioButton_5.setText("")
        self.radioButton_6.setText("")
        self.radioButton_7.setText("")
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_55.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_4),
                                    QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u5c5e\u6027", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u9884\u5904\u7406\u6307\u4ee4", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6307\u4ee4", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u6307\u4ee4", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6548\u679c", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6307\u4ee4", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6307\u4ee4\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u5316", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e8c\u503c\u5316", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5747\u503c\u6ee4\u6ce2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u4e2d\u503c\u6ee4\u6ce2", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u6ee4\u6ce2", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u9ad8\u65af\u6ee4\u6ce2", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u5f00/\u95ed\u8fd0\u7b97", None))

        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u6548\u679c", None))
        self.label_8.setText(
            QCoreApplication.translate("MainWindow", u"\u53c2\u65701\uff1a\u5f52\u4e00\u5316\uff1a", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5426", None))

        self.label_9.setText(
            QCoreApplication.translate("MainWindow", u"\u53c2\u65702\uff1a\u5377\u79ef\u6838\uff1a", None))
        self.pushButton_22.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6),
                                    QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u6ee4\u6ce2", None))
        self.groupBox_26.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_15),
                                    QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u53c2\u6570", None))
        ___qtablewidgetitem = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem1 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u540d\u79f0", None));
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_16),
                                    QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u53c2\u6570", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("MainWindow", u"\u811a\u672c", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_17),
                                     QCoreApplication.translate("MainWindow", u"Python", None))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_18),
                                     QCoreApplication.translate("MainWindow", u"VBS", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_14),
                                    QCoreApplication.translate("MainWindow", u"\u811a\u672c\u5904\u7406", None))
        self.pushButton_47.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.pushButton_48.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"\u6d4b\u8bd5\u8fd0\u884c", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5c55\u793a", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u9009\u62e9", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u672c\u5730\u6587\u4ef6\uff1a", None))
        self.toolButton_3.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u591a\u6a21\u677f\u7ba1\u7406", None))
        self.pushButton_34.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u589e\u6a21\u677f", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u6a21\u677f", None))
        self.pushButton_35.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u6a21\u677f", None))
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6a21\u677f", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"\u77e9\u5f62", None))
        self.comboBox_10.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5706\u5f62", None))
        self.comboBox_10.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5706\u73af", None))

        self.pushButton_27.setText(QCoreApplication.translate("MainWindow", u"\u91c7\u96c6\u533a\u57df", None))
        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"\u77e9\u5f62", None))
        self.comboBox_9.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5706\u5f62", None))

        self.pushButton_26.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u533a\u57df", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_7),
                                    QCoreApplication.translate("MainWindow", u"\u6a21\u677f", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u672c\u53c2\u6570", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u5339\u914d\u6a21\u5f0f\uff1a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u6700\u5927\u76ee\u6807\u6570\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u53e0\u7cfb\u6570(%)\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u8d2a\u5a6a\u7cfb\u6570(%)\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6da8\u7f29\u8303\u56f4\uff1a", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8f6e\u5ed3\u5339\u914d", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7070\u5ea6\u5339\u914d", None))

        self.label_12.setText(
            QCoreApplication.translate("MainWindow", u"\u6700\u5c0f\u5339\u914d\u5ea6(%)\uff1a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u5ea6\u8303\u56f4\uff1a", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("MainWindow", u"\u9ad8\u7ea7\u53c2\u6570", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u76ee\u6807\uff1a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u89d2\u5ea6\u6b65\u957f\uff1a", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u6570\u91cf\uff1a", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u6a21\u677f\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u5b57\u5854\u5c42\u6570\uff1a", None))
        self.comboBox_11.setItemText(0,
                                     QCoreApplication.translate("MainWindow", u"\u5355\u6a21\u677f\u8bc6\u522b", None))
        self.comboBox_11.setItemText(1,
                                     QCoreApplication.translate("MainWindow", u"\u591a\u6a21\u677f\u8bc6\u522b", None))

        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_8),
                                    QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa", None))
        self.checkBox_24.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u4e2d\u5fc3X\uff0c\u6570\u503c", None))
        self.checkBox_25.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u4e2d\u5fc3\uff0c\u70b9", None))
        self.checkBox_17.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u4e2d\u5fc3Y\uff0c\u6570\u503c", None))
        self.checkBox_21.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u89d2\u5ea6\uff0c\u6570\u503c", None))
        self.checkBox_15.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u6a21\u677f\u6570\uff0c\u6570\u503c",
                                       None))
        self.checkBox_13.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5b66\u4e60\u6a21\u677f\u540d\uff0c\u5b57\u7b26",
                                       None))
        self.checkBox_22.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u7ed3\u679c\uff0c\u5b57\u7b26", None))
        self.checkBox_19.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5f97\u5206\uff0c\u6570\u503c", None))
        self.checkBox_33.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u8bc6\u522b\u6a21\u677f\u540d\uff0c\u5b57\u7b26",
                                       None))
        self.checkBox_16.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u6570\u91cf\uff0c\u6570\u503c", None))
        self.checkBox_34.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u68c0\u51fa\u6a21\u677f\u540d\uff0c\u5b57\u7b26",
                                       None))
        self.checkBox_26.setText(
            QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u56fe\u50cf\uff0c\u56fe\u50cf", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_9),
                                    QCoreApplication.translate("MainWindow", u"\u5217\u8868", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u5b66\u4e60", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.pushButton_32.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u6d4b\u8bd5", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_49.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"\u901a\u8baf\u6d4b\u8bd5", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.groupBox_29.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u683c\u5f0f", None))
        self.comboBox_28.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))

        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u683c\u5f0f\uff1a", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u683c\u5f0f\uff1a", None))
        self.comboBox_29.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_29.setItemText(1, QCoreApplication.translate("MainWindow", u"0.0", None))
        self.comboBox_29.setItemText(2, QCoreApplication.translate("MainWindow", u"0.00", None))
        self.comboBox_29.setItemText(3, QCoreApplication.translate("MainWindow", u"0.000", None))
        self.comboBox_29.setItemText(4, QCoreApplication.translate("MainWindow", u"0.0000", None))
        self.comboBox_29.setItemText(5, QCoreApplication.translate("MainWindow", u"0.00000", None))
        self.comboBox_29.setItemText(6, QCoreApplication.translate("MainWindow", u"0.000000", None))

        self.comboBox_27.setItemText(0, QCoreApplication.translate("MainWindow", u"Siged(\u6574\u6570\uff09", None))
        self.comboBox_27.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                   u"Unsiged(\u65e0\u7b26\u53f7\u6574\u6570)", None))
        self.comboBox_27.setItemText(2,
                                     QCoreApplication.translate("MainWindow", u"Float(\u5355\u7cbe\u5ea6\u6570)", None))
        self.comboBox_27.setItemText(3, QCoreApplication.translate("MainWindow",
                                                                   u"Float Inverse(\u8d1f\u5355\u7cbe\u5ea6\u6570)",
                                                                   None))
        self.comboBox_27.setItemText(4, QCoreApplication.translate("MainWindow", u"Double(\u53cc\u7cbe\u5ea6\u6570)",
                                                                   None))
        self.comboBox_27.setItemText(5, QCoreApplication.translate("MainWindow",
                                                                   u"Double Inverse(\u8d1f\u53cc\u7cbe\u5ea6\u6570)",
                                                                   None))

        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u7c7b\u578b\uff1a", None))
        self.groupBox_28.setTitle(QCoreApplication.translate("MainWindow", u"\u7f51\u53e3\u53c2\u6570", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740\uff1a", None))
        self.groupBox_31.setTitle(QCoreApplication.translate("MainWindow", u"\u4e32\u53e3\u53c2\u6570", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a ", None))
        self.comboBox_22.setItemText(0, QCoreApplication.translate("MainWindow", u"com1", None))
        self.comboBox_22.setItemText(1, QCoreApplication.translate("MainWindow", u"com2", None))
        self.comboBox_22.setItemText(2, QCoreApplication.translate("MainWindow", u"com3", None))
        self.comboBox_22.setItemText(3, QCoreApplication.translate("MainWindow", u"com4", None))
        self.comboBox_22.setItemText(4, QCoreApplication.translate("MainWindow", u"com5", None))
        self.comboBox_22.setItemText(5, QCoreApplication.translate("MainWindow", u"com6", None))
        self.comboBox_22.setItemText(6, QCoreApplication.translate("MainWindow", u"com7", None))
        self.comboBox_22.setItemText(7, QCoreApplication.translate("MainWindow", u"com8", None))
        self.comboBox_22.setItemText(8, QCoreApplication.translate("MainWindow", u"com9", None))
        self.comboBox_22.setItemText(9, QCoreApplication.translate("MainWindow", u"com10", None))
        self.comboBox_22.setItemText(10, QCoreApplication.translate("MainWindow", u"com11", None))
        self.comboBox_22.setItemText(11, QCoreApplication.translate("MainWindow", u"com12", None))
        self.comboBox_22.setItemText(12, QCoreApplication.translate("MainWindow", u"com13", None))
        self.comboBox_22.setItemText(13, QCoreApplication.translate("MainWindow", u"com14", None))
        self.comboBox_22.setItemText(14, QCoreApplication.translate("MainWindow", u"com15", None))
        self.comboBox_22.setItemText(15, QCoreApplication.translate("MainWindow", u"com16", None))
        self.comboBox_22.setItemText(16, QCoreApplication.translate("MainWindow", u"com17", None))
        self.comboBox_22.setItemText(17, QCoreApplication.translate("MainWindow", u"com18", None))
        self.comboBox_22.setItemText(18, QCoreApplication.translate("MainWindow", u"com19", None))
        self.comboBox_22.setItemText(19, QCoreApplication.translate("MainWindow", u"com20", None))
        self.comboBox_22.setItemText(20, QCoreApplication.translate("MainWindow", u"com21", None))
        self.comboBox_22.setItemText(21, QCoreApplication.translate("MainWindow", u"com22", None))
        self.comboBox_22.setItemText(22, QCoreApplication.translate("MainWindow", u"com23", None))
        self.comboBox_22.setItemText(23, QCoreApplication.translate("MainWindow", u"com24", None))
        self.comboBox_22.setItemText(24, QCoreApplication.translate("MainWindow", u"com25", None))
        self.comboBox_22.setItemText(25, QCoreApplication.translate("MainWindow", u"com26", None))
        self.comboBox_22.setItemText(26, QCoreApplication.translate("MainWindow", u"com27", None))
        self.comboBox_22.setItemText(27, QCoreApplication.translate("MainWindow", u"com28", None))
        self.comboBox_22.setItemText(28, QCoreApplication.translate("MainWindow", u"com29", None))
        self.comboBox_22.setItemText(29, QCoreApplication.translate("MainWindow", u"com30", None))
        self.comboBox_22.setItemText(30, QCoreApplication.translate("MainWindow", u"com31", None))
        self.comboBox_22.setItemText(31, QCoreApplication.translate("MainWindow", u"com32", None))

        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\uff1a", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"RTU", None))

        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u6821\u9a8c\uff1a ", None))
        self.comboBox_26.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_26.setItemText(1, QCoreApplication.translate("MainWindow", u"Odd", None))
        self.comboBox_26.setItemText(2, QCoreApplication.translate("MainWindow", u"Even", None))

        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62\u4f4d\uff1a", None))
        self.comboBox_25.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_25.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))

        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u6ce2\u7279\u7387\uff1a", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("MainWindow", u"300", None))
        self.comboBox_23.setItemText(1, QCoreApplication.translate("MainWindow", u"600", None))
        self.comboBox_23.setItemText(2, QCoreApplication.translate("MainWindow", u"1200", None))
        self.comboBox_23.setItemText(3, QCoreApplication.translate("MainWindow", u"2400", None))
        self.comboBox_23.setItemText(4, QCoreApplication.translate("MainWindow", u"4800", None))
        self.comboBox_23.setItemText(5, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_23.setItemText(6, QCoreApplication.translate("MainWindow", u"14400", None))
        self.comboBox_23.setItemText(7, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_23.setItemText(8, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_23.setItemText(9, QCoreApplication.translate("MainWindow", u"56000", None))
        self.comboBox_23.setItemText(10, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_23.setItemText(11, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_23.setItemText(12, QCoreApplication.translate("MainWindow", u"128000", None))
        self.comboBox_23.setItemText(13, QCoreApplication.translate("MainWindow", u"153600", None))
        self.comboBox_23.setItemText(14, QCoreApplication.translate("MainWindow", u"230400", None))
        self.comboBox_23.setItemText(15, QCoreApplication.translate("MainWindow", u"256000", None))
        self.comboBox_23.setItemText(16, QCoreApplication.translate("MainWindow", u"460800", None))
        self.comboBox_23.setItemText(17, QCoreApplication.translate("MainWindow", u"921600", None))

        self.comboBox_23.setCurrentText(QCoreApplication.translate("MainWindow", u"300", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4f4d\uff1a ", None))
        self.comboBox_24.setItemText(0, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_24.setItemText(1, QCoreApplication.translate("MainWindow", u"8", None))

        self.comboBox_24.setCurrentText(QCoreApplication.translate("MainWindow", u"7", None))
        self.groupBox_34.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u7801", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u7801\uff1a", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u5bc4\u5b58\u5668\u6570\u91cf\uff1a", None))
        self.comboBox_39.setItemText(0, QCoreApplication.translate("MainWindow", u"Read(01) \u7ebf\u5708\u72b6\u6001",
                                                                   None))
        self.comboBox_39.setItemText(1, QCoreApplication.translate("MainWindow", u"Read(02) \u8f93\u5165\u72b6\u6001",
                                                                   None))
        self.comboBox_39.setItemText(2, QCoreApplication.translate("MainWindow",
                                                                   u"Read(03) \u4fdd\u6301\u5bc4\u5b58\u5668", None))
        self.comboBox_39.setItemText(3, QCoreApplication.translate("MainWindow",
                                                                   u"Read(04) \u8f93\u5165\u5bc4\u5b58\u5668", None))

        self.groupBox_44.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u7801", None))
        self.comboBox_40.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u53c2\u6570", None))
        self.comboBox_40.setItemText(1, QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u503c", None))

        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u4f20\u9012\u76ee\u6807\uff1a", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u7801\uff1a", None))
        self.comboBox_41.setItemText(0, QCoreApplication.translate("MainWindow", u"Wirte(05) \u5355\u7ebf\u5708", None))
        self.comboBox_41.setItemText(1, QCoreApplication.translate("MainWindow", u"Wirte(06) \u5355\u5bc4\u5b58\u5668",
                                                                   None))
        self.comboBox_41.setItemText(2, QCoreApplication.translate("MainWindow", u"Wirte(15) \u591a\u7ebf\u5708", None))
        self.comboBox_41.setItemText(3, QCoreApplication.translate("MainWindow", u"Wirte(16) \u591a\u5bc4\u5b58\u5668",
                                                                   None))

        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Modbus\u53c2\u6570", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u7ad9ID\uff1a", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7f51\u53e3", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4e32\u53e3", None))

        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u65f6(ms)\uff1a", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u63a5\u53e3\uff1a", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c\uff1a", None))
        self.comboBox_33.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bfb", None))
        self.comboBox_33.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5199", None))

        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740\uff1a", None))
        self.groupBox_30.setTitle(QCoreApplication.translate("MainWindow", u"Modbus\u540d\u79f0", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Modbus\u540d\u79f0\uff1a", None))
        self.tabWidget_11.setTabText(self.tabWidget_11.indexOf(self.tab_19),
                                     QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u901a\u8baf", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u5217\u8868", None))
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7c7b\u578b", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u503c", None));
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_12),
                                    QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u8f93\u51fa", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u53c2\u6570", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u7c7b\u578b\uff1a", None))
        self.comboBox_31.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6570\u503c", None))
        self.comboBox_31.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5b57\u7b26", None))
        self.comboBox_31.setItemText(2, QCoreApplication.translate("MainWindow", u"\u70b9", None))

        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u5165\u6570\u91cf\uff1a", None))
        self.tabWidget_12.setTabText(self.tabWidget_12.indexOf(self.tab_20),
                                     QCoreApplication.translate("MainWindow", u"\u5408\u5e76\u6570\u636e", None))
        self.pushButton_40.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3),
                                    QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u540d", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u5de5\u5177\u5217\u8868",
                                                                 None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u8bbe\u5907", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"\u6a21\u677f\u5339\u914d", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"\u989c\u8272\u8bc6\u522b", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"\u5750\u6807\u6807\u5b9a", None));
        ___qtreewidgetitem5 = self.treeWidget.topLevelItem(4)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("MainWindow", u"\u7f51\u7edc\u901a\u8baf", None));
        ___qtreewidgetitem6 = self.treeWidget.topLevelItem(5)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5de5\u5177", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem6.child(0)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5408\u5e76", None));
        ___qtreewidgetitem8 = ___qtreewidgetitem6.child(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("MainWindow", u"\u6570\u636e\u8f6c\u6362", None));
        ___qtreewidgetitem9 = ___qtreewidgetitem6.child(2)
        ___qtreewidgetitem9.setText(0,
                                    QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u8f93\u51fa", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5750\u6807", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  QCoreApplication.translate("MainWindow", u"\u4efb\u52a1\u540d", None))

    # retranslateUi

    def setcss(self):
        # 重写控件
        # self.label_42 = LightLabel(self.label_42)
        # self.tableWidget = CRTableWidget(self.tableWidget)
        # self.listWidget_2 = MyListWidget(self.listWidget_2)
        # self.spinBox_21 = MySpinBox(self.spinBox_21)
        # self.listWidget_3 = ImageListWidget(self.listWidget_3)
        # self.tableWidget_2 = OutputtableWidget(self.tableWidget_2)
        # self.tableWidget_4 = QsciTableWidget(self.tableWidget_4)
        # self.tableWidget_5 = QsciTableWidget(self.tableWidget_5)
        # self.widget_31 = codeCompilerPy()
        # self.widget_34 = codeCompilerVBS()


        # 图像显示窗口
        self.View = PlaybackWindow(parent=self.widget_2)
        self.gridLayout_32.addWidget(self.View)

        self.stackedWidget_14.hide()
        self.stackedWidget.hide()

        self.widget_2.resize(QSize(804, 476))

        # 设置位置和大小
        self.label_20.setGeometry(100, 100, 200, 20)
        # 设置字体颜色为白色
        self.label_20.setStyleSheet("color: white")

        # self.setTabel()
        self.tableWidget.setcss(['样本名', '样本区域' , '坐标系比例'])
        self.tableWidget_5.setcss(['类型','名称' ])
        self.tableWidget_4.setcss(['类型','名称'])
        self.tableWidget_2.setcss(['类型', '自定义值'])


        # # 设置参数窗口在流程树上面
        # self.stackedWidget.raise_()


        # 设置运行按钮样式
        self.toolButton_14.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_14.setStyleSheet(
            "background-color: rgb(58, 111, 50);\n"f"border-radius: 10px; border:\n"" 3px groove gray;border-style: outset;")
        self.toolButton_15.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_15.setStyleSheet(
            "background-color: rgb(58, 111, 50);\n"f"border-radius: 10px; border:\n"" 3px groove gray;border-style: outset;")

        # 设置流程树样式
        self.treeWidget.expandAll() # 默认展开
        self.treeWidget.setStyle(QStyleFactory.create("windows")) # 连线设置
        self.treeWidget.setStyleSheet("""
            QTreeView {
                outline: 0px;
            }
            QTreeView::item{
                padding:5px;
            }
            QTreeWidget::item 
            { border: 0px solid gray; }
        """)
        # 设置流程树下拉按钮样式
        self.treeWidget.setStyleSheet("""
                    QTreeWidget::branch:has-children:!has-siblings:closed,
                    QTreeWidget::branch:closed:has-children:has-siblings {
                        image: url(icon/展开2.png);
                        image-size: 16px;
                    }
                    QTreeWidget::branch:open:has-children:!has-siblings,
                    QTreeWidget::branch:open:has-children:has-siblings {
                        image: url(icon/收起2.png);
                        image-size: 16px;
                    }
                    """)
