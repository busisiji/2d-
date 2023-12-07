# -*- coding: utf-8 -*-
import logging

from lib.file import delete_folder, make_new_folder, rename_file, write_new_json
from lib.path import  get_file_name
from core.MyClass import *
from core.imageGraphicsClass import *
import resource_rc

logging.basicConfig(filename=Globals.filename, level=logging.DEBUG, format='\r\n%(asctime)s %(levelname)s：%(message)s')
# 打开日志文件并将其截断为零字节
with open(Globals.filename, 'w'):
    pass

class CustomStyle(QProxyStyle):
    def drawControl(self, element, option, painter, widget=None):
        if element == QProxyStyle.CE_PushButton:
            # 保持原有的绘制逻辑
            super().drawControl(element, option, painter, widget)
        else:
            # 其他控件的绘制逻辑
            super().drawControl(element, option, painter, widget)
    def subControlRect(self, control, option, subControl, widget):
        super().subControlRect(control, option, subControl, widget)
        if control == QStyle.CC_ToolButton and subControl == QStyle.SC_ToolButtonMenu:
            rect = super().subControlRect(control, option, subControl, widget)
            rect.setWidth(20)  # 设置箭头宽度
            rect.setHeight(20)  # 设置箭头高度
            return rect
        return super().subControlRect(control, option, subControl, widget)

class Ui_MainWindow(object):
    '''主界面'''

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1214, 853)
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
        self.gridLayout_18 = QGridLayout(self.centralwidget)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.gridLayout_13 = QGridLayout(self.widget_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.gridLayout_10 = QGridLayout(self.widget_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tabWidget = QTabWidget(self.widget_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy2.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy2)
        self.gridLayout_11 = QGridLayout(self.tab)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_30)

        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.label)

        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_31)

        self.gridLayout_11.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_36)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        sizePolicy2.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.label_3)

        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.horizontalLayout_17.addWidget(self.label_10)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_37)

        self.gridLayout_11.addLayout(self.horizontalLayout_17, 1, 0, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_38)

        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        sizePolicy2.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.label_4)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)

        self.horizontalLayout_18.addWidget(self.label_11)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_39)

        self.gridLayout_11.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.widget_4, 2, 0, 1, 1)

        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_10 = QWidget(self.widget)
        self.widget_10.setObjectName(u"widget_10")
        sizePolicy1.setHeightForWidth(self.widget_10.sizePolicy().hasHeightForWidth())
        self.widget_10.setSizePolicy(sizePolicy1)
        self.widget_10.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.horizontalLayout = QHBoxLayout(self.widget_10)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(9, 9, 9, 9)
        self.widget_5 = QWidget(self.widget_10)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.gridLayout_12 = QGridLayout(self.widget_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.widget_10)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
        self.gridLayout = QGridLayout(self.widget_3)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.gridLayout_19 = QGridLayout(self.widget_6)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_6 = QLabel(self.widget_6)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_321 = QLabel(self.widget_6)
        self.label_321.setObjectName(u"label_321")
        sizePolicy1.setHeightForWidth(self.label_321.sizePolicy().hasHeightForWidth())
        self.label_321.setSizePolicy(sizePolicy1)
        self.label_321.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_19.addWidget(self.label_321, 1, 2, 1, 1)

        self.label_311 = QLabel(self.widget_6)
        self.label_311.setObjectName(u"label_311")
        sizePolicy1.setHeightForWidth(self.label_311.sizePolicy().hasHeightForWidth())
        self.label_311.setSizePolicy(sizePolicy1)
        self.label_311.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_311, 1, 1, 1, 1)

        self.label_8 = QLabel(self.widget_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_19.addWidget(self.label_8, 0, 2, 1, 1)

        self.toolButton = QToolButton(self.widget_6)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout_19.addWidget(self.toolButton, 1, 3, 1, 1)

        self.gridLayout.addWidget(self.widget_6, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_3)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.pushButton_11.sizePolicy().hasHeightForWidth())
        self.pushButton_11.setSizePolicy(sizePolicy3)
        self.pushButton_11.setMinimumSize(QSize(60, 0))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_11.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.pushButton_11.setIcon(icon2)
        self.pushButton_11.setIconSize(QSize(18, 18))
        self.pushButton_11.setAutoDefault(False)
        self.pushButton_11.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_11, 0, 1, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_3)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setIcon(icon3)
        self.pushButton_12.setIconSize(QSize(18, 18))
        self.pushButton_12.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_12, 0, 2, 1, 1)

        self.pushButton_13 = QPushButton(self.widget_3)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy3.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy3)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setIcon(icon4)
        self.pushButton_13.setIconSize(QSize(18, 18))
        self.pushButton_13.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)

        self.horizontalLayout.addWidget(self.widget_3)

        self.horizontalSpacer_8 = QSpacerItem(752, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.gridLayout_2.addWidget(self.widget_10, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.widget, 0, 0, 1, 2)

        self.stackedWidget_13 = QStackedWidget(self.widget_2)
        self.stackedWidget_13.setObjectName(u"stackedWidget_13")
        sizePolicy3.setHeightForWidth(self.stackedWidget_13.sizePolicy().hasHeightForWidth())
        self.stackedWidget_13.setSizePolicy(sizePolicy3)
        self.stackedWidget_13.setMinimumSize(QSize(0, 0))
        self.stackedWidget_13.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_13.setStyleSheet(u"background-color: rgb(175, 175, 175);")
        self.stackedWidget_13Page1 = QWidget()
        self.stackedWidget_13Page1.setObjectName(u"stackedWidget_13Page1")
        self.gridLayout_8 = QGridLayout(self.stackedWidget_13Page1)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.tabWidget_2 = QTabWidget(self.stackedWidget_13Page1)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_17 = QGridLayout(self.tab_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBox)

        self.verticalLayout.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.ptn_ok = QPushButton(self.tab_2)
        self.ptn_ok.setObjectName(u"ptn_ok")
        sizePolicy.setHeightForWidth(self.ptn_ok.sizePolicy().hasHeightForWidth())
        self.ptn_ok.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.ptn_ok)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.ptn_cancel = QPushButton(self.tab_2)
        self.ptn_cancel.setObjectName(u"ptn_cancel")
        sizePolicy.setHeightForWidth(self.ptn_cancel.sizePolicy().hasHeightForWidth())
        self.ptn_cancel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.ptn_cancel)

        self.horizontalSpacer_3 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.gridLayout_17.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_2, "")

        self.gridLayout_8.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        self.stackedWidget_13.addWidget(self.stackedWidget_13Page1)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_14 = QGridLayout(self.page_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.tabWidget_3 = QTabWidget(self.page_4)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setStyleSheet(u"background-color: rgb(139, 146, 166);")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget_3.addTab(self.tab_5, "")

        self.gridLayout_14.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.stackedWidget_13.addWidget(self.page_4)

        self.gridLayout_5.addWidget(self.stackedWidget_13, 1, 1, 2, 1)

        self.stackedWidget_3 = QStackedWidget(self.widget_2)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        sizePolicy1.setHeightForWidth(self.stackedWidget_3.sizePolicy().hasHeightForWidth())
        self.stackedWidget_3.setSizePolicy(sizePolicy1)
        self.stackedWidget_3.setMinimumSize(QSize(0, 0))
        self.stackedWidget_3.setMaximumSize(QSize(16777215, 16777215))
        self.stackedWidget_3.setStyleSheet(u"background-color: rgb(113, 113, 113);")
        self.stackedWidget_3.setLineWidth(1)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.gridLayout_9 = QGridLayout(self.page_1)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.widget_p1 = QWidget(self.page_1)
        self.widget_p1.setObjectName(u"widget_p1")
        self.label_p1 = QLabel(self.widget_p1)
        self.label_p1.setObjectName(u"label_p1")
        self.label_p1.setGeometry(QRect(0, 0, 54, 21))
        self.label_p1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p1_3 = QPushButton(self.widget_p1)
        self.pushButton_p1_3.setObjectName(u"pushButton_p1_3")
        self.pushButton_p1_3.setGeometry(QRect(860, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p1_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p1_3.setSizePolicy(sizePolicy)
        self.pushButton_p1_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p1_3.setIcon(icon2)
        self.pushButton_p1_1 = QPushButton(self.widget_p1)
        self.pushButton_p1_1.setObjectName(u"pushButton_p1_1")
        self.pushButton_p1_1.setGeometry(QRect(800, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p1_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p1_1.setSizePolicy(sizePolicy)
        self.pushButton_p1_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p1_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p1_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p1_1.setAutoRepeatDelay(300)
        self.pushButton_p1_1.setAutoRepeatInterval(100)
        self.pushButton_p1_1.setAutoDefault(False)
        self.label_p1_central = MyLabel(self.widget_p1)
        self.label_p1_central.setObjectName(u"label_p1_central")
        self.label_p1_central.setGeometry(QRect(20, 0, 855, 570))
        self.label_p1_central.raise_()
        self.label_p1.raise_()
        self.pushButton_p1_3.raise_()
        self.pushButton_p1_1.raise_()

        self.gridLayout_9.addWidget(self.widget_p1, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_2 = QHBoxLayout(self.page_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_p2 = QWidget(self.page_2)
        self.widget_p2.setObjectName(u"widget_p2")
        self.label_p2 = QLabel(self.widget_p2)
        self.label_p2.setObjectName(u"label_p2")
        self.label_p2.setGeometry(QRect(0, 0, 54, 21))
        self.label_p2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p2_3 = QPushButton(self.widget_p2)
        self.pushButton_p2_3.setObjectName(u"pushButton_p2_3")
        self.pushButton_p2_3.setGeometry(QRect(410, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p2_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p2_3.setSizePolicy(sizePolicy)
        self.pushButton_p2_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p2_3.setIcon(icon2)
        self.pushButton_p2_1 = QPushButton(self.widget_p2)
        self.pushButton_p2_1.setObjectName(u"pushButton_p2_1")
        self.pushButton_p2_1.setGeometry(QRect(350, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p2_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p2_1.setSizePolicy(sizePolicy)
        self.pushButton_p2_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p2_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p2_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p2_1.setAutoRepeatDelay(300)
        self.pushButton_p2_1.setAutoRepeatInterval(100)
        self.pushButton_p2_1.setAutoDefault(False)
        self.label_p2_central = MyLabel(self.widget_p2)
        self.label_p2_central.setObjectName(u"label_p2_central")
        self.label_p2_central.setGeometry(QRect(3, 171, 441, 294))
        self.label_p2_central.raise_()
        self.label_p2.raise_()
        self.pushButton_p2_3.raise_()
        self.pushButton_p2_1.raise_()

        self.horizontalLayout_2.addWidget(self.widget_p2)

        self.widget_p3 = QWidget(self.page_2)
        self.widget_p3.setObjectName(u"widget_p3")
        self.label_p3 = QLabel(self.widget_p3)
        self.label_p3.setObjectName(u"label_p3")
        self.label_p3.setGeometry(QRect(0, 0, 54, 21))
        self.label_p3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p3_3 = QPushButton(self.widget_p3)
        self.pushButton_p3_3.setObjectName(u"pushButton_p3_3")
        self.pushButton_p3_3.setGeometry(QRect(410, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p3_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p3_3.setSizePolicy(sizePolicy)
        self.pushButton_p3_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p3_3.setIcon(icon2)
        self.pushButton_p3_1 = QPushButton(self.widget_p3)
        self.pushButton_p3_1.setObjectName(u"pushButton_p3_1")
        self.pushButton_p3_1.setGeometry(QRect(350, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p3_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p3_1.setSizePolicy(sizePolicy)
        self.pushButton_p3_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p3_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p3_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p3_1.setAutoRepeatDelay(300)
        self.pushButton_p3_1.setAutoRepeatInterval(100)
        self.pushButton_p3_1.setAutoDefault(False)
        self.label_p3_central = MyLabel(self.widget_p3)
        self.label_p3_central.setObjectName(u"label_p3_central")
        self.label_p3_central.setGeometry(QRect(0, 150, 441, 294))
        self.label_p3_central.raise_()
        self.label_p3.raise_()
        self.pushButton_p3_3.raise_()
        self.pushButton_p3_1.raise_()

        self.horizontalLayout_2.addWidget(self.widget_p3)

        self.stackedWidget_3.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.widget_p7 = QWidget(self.page_3)
        self.widget_p7.setObjectName(u"widget_p7")
        self.label_p7 = QLabel(self.widget_p7)
        self.label_p7.setObjectName(u"label_p7")
        self.label_p7.setGeometry(QRect(0, 0, 54, 12))
        self.label_p7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p7_3 = QPushButton(self.widget_p7)
        self.pushButton_p7_3.setObjectName(u"pushButton_p7_3")
        self.pushButton_p7_3.setGeometry(QRect(410, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p7_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p7_3.setSizePolicy(sizePolicy)
        self.pushButton_p7_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p7_3.setIcon(icon2)
        self.pushButton_p7_2 = QPushButton(self.widget_p7)
        self.pushButton_p7_2.setObjectName(u"pushButton_p7_2")
        self.pushButton_p7_2.setGeometry(QRect(370, 0, 40, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p7_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p7_2.setSizePolicy(sizePolicy)
        self.pushButton_p7_2.setMinimumSize(QSize(0, 24))
        self.pushButton_p7_2.setMaximumSize(QSize(40, 24))
        self.pushButton_p7_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_p7_2.setBaseSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setKerning(True)
        self.pushButton_p7_2.setFont(font1)
        self.pushButton_p7_2.setAutoFillBackground(False)
        self.pushButton_p7_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p7_1 = QPushButton(self.widget_p7)
        self.pushButton_p7_1.setObjectName(u"pushButton_p7_1")
        self.pushButton_p7_1.setGeometry(QRect(310, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p7_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p7_1.setSizePolicy(sizePolicy)
        self.pushButton_p7_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p7_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p7_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p7_1.setAutoRepeatDelay(300)
        self.pushButton_p7_1.setAutoRepeatInterval(100)
        self.pushButton_p7_1.setAutoDefault(False)
        self.label_p7_central = MyLabel(self.widget_p7)
        self.label_p7_central.setObjectName(u"label_p7_central")
        self.label_p7_central.setGeometry(QRect(10, 0, 420, 280))
        self.label_p7_central.raise_()
        self.label_p7.raise_()
        self.pushButton_p7_3.raise_()
        self.pushButton_p7_2.raise_()
        self.pushButton_p7_1.raise_()

        self.gridLayout_6.addWidget(self.widget_p7, 1, 1, 1, 1)

        self.widget_p4 = QWidget(self.page_3)
        self.widget_p4.setObjectName(u"widget_p4")
        self.label_p4 = QLabel(self.widget_p4)
        self.label_p4.setObjectName(u"label_p4")
        self.label_p4.setGeometry(QRect(0, 0, 54, 16))
        self.label_p4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p4_3 = QPushButton(self.widget_p4)
        self.pushButton_p4_3.setObjectName(u"pushButton_p4_3")
        self.pushButton_p4_3.setGeometry(QRect(410, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p4_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p4_3.setSizePolicy(sizePolicy)
        self.pushButton_p4_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p4_3.setIcon(icon2)
        self.pushButton_p4_2 = QPushButton(self.widget_p4)
        self.pushButton_p4_2.setObjectName(u"pushButton_p4_2")
        self.pushButton_p4_2.setGeometry(QRect(370, 0, 40, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p4_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p4_2.setSizePolicy(sizePolicy)
        self.pushButton_p4_2.setMinimumSize(QSize(0, 24))
        self.pushButton_p4_2.setMaximumSize(QSize(40, 24))
        self.pushButton_p4_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_p4_2.setBaseSize(QSize(0, 0))
        self.pushButton_p4_2.setFont(font1)
        self.pushButton_p4_2.setAutoFillBackground(False)
        self.pushButton_p4_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p4_1 = QPushButton(self.widget_p4)
        self.pushButton_p4_1.setObjectName(u"pushButton_p4_1")
        self.pushButton_p4_1.setGeometry(QRect(310, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p4_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p4_1.setSizePolicy(sizePolicy)
        self.pushButton_p4_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p4_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p4_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p4_1.setAutoRepeatDelay(300)
        self.pushButton_p4_1.setAutoRepeatInterval(100)
        self.pushButton_p4_1.setAutoDefault(False)
        self.label_p4_central = MyLabel(self.widget_p4)
        self.label_p4_central.setObjectName(u"label_p4_central")
        self.label_p4_central.setGeometry(QRect(10, 0, 420, 280))
        self.label_p4_central.raise_()
        self.label_p4.raise_()
        self.pushButton_p4_3.raise_()
        self.pushButton_p4_2.raise_()
        self.pushButton_p4_1.raise_()

        self.gridLayout_6.addWidget(self.widget_p4, 0, 0, 1, 1)

        self.widget_p5 = QWidget(self.page_3)
        self.widget_p5.setObjectName(u"widget_p5")
        self.label_p5 = QLabel(self.widget_p5)
        self.label_p5.setObjectName(u"label_p5")
        self.label_p5.setGeometry(QRect(0, 0, 54, 16))
        self.label_p5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p5_3 = QPushButton(self.widget_p5)
        self.pushButton_p5_3.setObjectName(u"pushButton_p5_3")
        self.pushButton_p5_3.setGeometry(QRect(410, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p5_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p5_3.setSizePolicy(sizePolicy)
        self.pushButton_p5_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p5_3.setIcon(icon2)
        self.pushButton_p5_2 = QPushButton(self.widget_p5)
        self.pushButton_p5_2.setObjectName(u"pushButton_p5_2")
        self.pushButton_p5_2.setGeometry(QRect(370, 0, 40, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p5_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p5_2.setSizePolicy(sizePolicy)
        self.pushButton_p5_2.setMinimumSize(QSize(0, 24))
        self.pushButton_p5_2.setMaximumSize(QSize(40, 24))
        self.pushButton_p5_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_p5_2.setBaseSize(QSize(0, 0))
        self.pushButton_p5_2.setFont(font1)
        self.pushButton_p5_2.setAutoFillBackground(False)
        self.pushButton_p5_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p5_1 = QPushButton(self.widget_p5)
        self.pushButton_p5_1.setObjectName(u"pushButton_p5_1")
        self.pushButton_p5_1.setGeometry(QRect(310, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p5_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p5_1.setSizePolicy(sizePolicy)
        self.pushButton_p5_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p5_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p5_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p5_1.setAutoRepeatDelay(300)
        self.pushButton_p5_1.setAutoRepeatInterval(100)
        self.pushButton_p5_1.setAutoDefault(False)
        self.label_p5_central = MyLabel(self.widget_p5)
        self.label_p5_central.setObjectName(u"label_p5_central")
        self.label_p5_central.setGeometry(QRect(10, 0, 420, 280))
        self.label_p5_central.raise_()
        self.label_p5.raise_()
        self.pushButton_p5_3.raise_()
        self.pushButton_p5_2.raise_()
        self.pushButton_p5_1.raise_()

        self.gridLayout_6.addWidget(self.widget_p5, 0, 1, 1, 1)

        self.widget_p6 = QWidget(self.page_3)
        self.widget_p6.setObjectName(u"widget_p6")
        self.label_p6 = QLabel(self.widget_p6)
        self.label_p6.setObjectName(u"label_p6")
        self.label_p6.setGeometry(QRect(0, 0, 54, 12))
        self.label_p6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p6_3 = QPushButton(self.widget_p6)
        self.pushButton_p6_3.setObjectName(u"pushButton_p6_3")
        self.pushButton_p6_3.setGeometry(QRect(410, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p6_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p6_3.setSizePolicy(sizePolicy)
        self.pushButton_p6_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p6_3.setIcon(icon2)
        self.pushButton_p6_2 = QPushButton(self.widget_p6)
        self.pushButton_p6_2.setObjectName(u"pushButton_p6_2")
        self.pushButton_p6_2.setGeometry(QRect(370, 0, 40, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p6_2.sizePolicy().hasHeightForWidth())
        self.pushButton_p6_2.setSizePolicy(sizePolicy)
        self.pushButton_p6_2.setMinimumSize(QSize(0, 24))
        self.pushButton_p6_2.setMaximumSize(QSize(40, 24))
        self.pushButton_p6_2.setSizeIncrement(QSize(0, 0))
        self.pushButton_p6_2.setBaseSize(QSize(0, 0))
        self.pushButton_p6_2.setFont(font1)
        self.pushButton_p6_2.setAutoFillBackground(False)
        self.pushButton_p6_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p6_1 = QPushButton(self.widget_p6)
        self.pushButton_p6_1.setObjectName(u"pushButton_p6_1")
        self.pushButton_p6_1.setGeometry(QRect(310, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p6_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p6_1.setSizePolicy(sizePolicy)
        self.pushButton_p6_1.setMinimumSize(QSize(0, 24))
        self.pushButton_p6_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p6_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p6_1.setAutoRepeatDelay(300)
        self.pushButton_p6_1.setAutoRepeatInterval(100)
        self.pushButton_p6_1.setAutoDefault(False)
        self.label_p6_central = MyLabel(self.widget_p6)
        self.label_p6_central.setObjectName(u"label_p6_central")
        self.label_p6_central.setGeometry(QRect(10, 0, 420, 280))
        self.label_p6_central.raise_()
        self.label_p6.raise_()
        self.pushButton_p6_3.raise_()
        self.pushButton_p6_2.raise_()
        self.pushButton_p6_1.raise_()

        self.gridLayout_6.addWidget(self.widget_p6, 1, 0, 1, 1)

        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_3)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_16 = QGridLayout(self.page_5)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.widget_p17 = QWidget(self.page_5)
        self.widget_p17.setObjectName(u"widget_p17")
        self.label_p17 = QLabel(self.widget_p17)
        self.label_p17.setObjectName(u"label_p17")
        self.label_p17.setGeometry(QRect(0, 0, 54, 12))
        self.label_p17.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p17_3 = QPushButton(self.widget_p17)
        self.pushButton_p17_3.setObjectName(u"pushButton_p17_3")
        self.pushButton_p17_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p17_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p17_3.setSizePolicy(sizePolicy)
        self.pushButton_p17_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p17_3.setIcon(icon2)
        self.pushButton_p17_1 = QPushButton(self.widget_p17)
        self.pushButton_p17_1.setObjectName(u"pushButton_p17_1")
        self.pushButton_p17_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p17_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p17_1.setSizePolicy(sizePolicy)
        self.pushButton_p17_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p17_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p17_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p17_1.setAutoRepeatDelay(300)
        self.pushButton_p17_1.setAutoRepeatInterval(100)
        self.pushButton_p17_1.setAutoDefault(False)
        self.label_p17_central = MyLabel(self.widget_p17)
        self.label_p17_central.setObjectName(u"label_p17_central")
        self.label_p17_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p17_central.raise_()
        self.label_p17.raise_()
        self.pushButton_p17_3.raise_()
        self.pushButton_p17_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p17, 2, 2, 1, 1)

        self.widget_p11 = QWidget(self.page_5)
        self.widget_p11.setObjectName(u"widget_p11")
        self.label_p11 = QLabel(self.widget_p11)
        self.label_p11.setObjectName(u"label_p11")
        self.label_p11.setGeometry(QRect(0, 0, 54, 16))
        self.label_p11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p11_3 = QPushButton(self.widget_p11)
        self.pushButton_p11_3.setObjectName(u"pushButton_p11_3")
        self.pushButton_p11_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p11_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_3.setSizePolicy(sizePolicy)
        self.pushButton_p11_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p11_3.setIcon(icon2)
        self.pushButton_p11_1 = QPushButton(self.widget_p11)
        self.pushButton_p11_1.setObjectName(u"pushButton_p11_1")
        self.pushButton_p11_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p11_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p11_1.setSizePolicy(sizePolicy)
        self.pushButton_p11_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p11_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p11_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p11_1.setAutoRepeatDelay(300)
        self.pushButton_p11_1.setAutoRepeatInterval(100)
        self.pushButton_p11_1.setAutoDefault(False)
        self.label_p11_central = MyLabel(self.widget_p11)
        self.label_p11_central.setObjectName(u"label_p11_central")
        self.label_p11_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p11_central.raise_()
        self.label_p11.raise_()
        self.pushButton_p11_3.raise_()
        self.pushButton_p11_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p11, 0, 2, 1, 1)

        self.widget_p10 = QWidget(self.page_5)
        self.widget_p10.setObjectName(u"widget_p10")
        self.label_p10 = QLabel(self.widget_p10)
        self.label_p10.setObjectName(u"label_p10")
        self.label_p10.setGeometry(QRect(0, 0, 54, 16))
        self.label_p10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p10_1 = QPushButton(self.widget_p10)
        self.pushButton_p10_1.setObjectName(u"pushButton_p10_1")
        self.pushButton_p10_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p10_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p10_1.setSizePolicy(sizePolicy)
        self.pushButton_p10_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p10_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p10_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p10_1.setAutoRepeatDelay(300)
        self.pushButton_p10_1.setAutoRepeatInterval(100)
        self.pushButton_p10_1.setAutoDefault(False)
        self.pushButton_p10_3 = QPushButton(self.widget_p10)
        self.pushButton_p10_3.setObjectName(u"pushButton_p10_3")
        self.pushButton_p10_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p10_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p10_3.setSizePolicy(sizePolicy)
        self.pushButton_p10_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p10_3.setIcon(icon2)
        self.label_p10_central = MyLabel(self.widget_p10)
        self.label_p10_central.setObjectName(u"label_p10_central")
        self.label_p10_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p10_central.raise_()
        self.label_p10.raise_()
        self.pushButton_p10_1.raise_()
        self.pushButton_p10_3.raise_()

        self.gridLayout_15.addWidget(self.widget_p10, 0, 1, 1, 1)

        self.widget_p15 = QWidget(self.page_5)
        self.widget_p15.setObjectName(u"widget_p15")
        self.label_p15 = QLabel(self.widget_p15)
        self.label_p15.setObjectName(u"label_p15")
        self.label_p15.setGeometry(QRect(0, 0, 54, 12))
        self.label_p15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p15_3 = QPushButton(self.widget_p15)
        self.pushButton_p15_3.setObjectName(u"pushButton_p15_3")
        self.pushButton_p15_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p15_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p15_3.setSizePolicy(sizePolicy)
        self.pushButton_p15_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p15_3.setIcon(icon2)
        self.pushButton_p15_1 = QPushButton(self.widget_p15)
        self.pushButton_p15_1.setObjectName(u"pushButton_p15_1")
        self.pushButton_p15_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p15_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p15_1.setSizePolicy(sizePolicy)
        self.pushButton_p15_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p15_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p15_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p15_1.setAutoRepeatDelay(300)
        self.pushButton_p15_1.setAutoRepeatInterval(100)
        self.pushButton_p15_1.setAutoDefault(False)
        self.label_p15_central = MyLabel(self.widget_p15)
        self.label_p15_central.setObjectName(u"label_p15_central")
        self.label_p15_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p15_central.raise_()
        self.label_p15.raise_()
        self.pushButton_p15_3.raise_()
        self.pushButton_p15_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p15, 2, 0, 1, 1)

        self.widget_p13 = QWidget(self.page_5)
        self.widget_p13.setObjectName(u"widget_p13")
        self.label_p13 = QLabel(self.widget_p13)
        self.label_p13.setObjectName(u"label_p13")
        self.label_p13.setGeometry(QRect(0, 0, 54, 12))
        self.label_p13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p13_3 = QPushButton(self.widget_p13)
        self.pushButton_p13_3.setObjectName(u"pushButton_p13_3")
        self.pushButton_p13_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p13_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p13_3.setSizePolicy(sizePolicy)
        self.pushButton_p13_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p13_3.setIcon(icon2)
        self.pushButton_p13_1 = QPushButton(self.widget_p13)
        self.pushButton_p13_1.setObjectName(u"pushButton_p13_1")
        self.pushButton_p13_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p13_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p13_1.setSizePolicy(sizePolicy)
        self.pushButton_p13_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p13_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p13_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p13_1.setAutoRepeatDelay(300)
        self.pushButton_p13_1.setAutoRepeatInterval(100)
        self.pushButton_p13_1.setAutoDefault(False)
        self.label_p13_central = MyLabel(self.widget_p13)
        self.label_p13_central.setObjectName(u"label_p13_central")
        self.label_p13_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p13_central.raise_()
        self.label_p13.raise_()
        self.pushButton_p13_3.raise_()
        self.pushButton_p13_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p13, 1, 1, 1, 1)

        self.widget_p14 = QWidget(self.page_5)
        self.widget_p14.setObjectName(u"widget_p14")
        self.label_p14 = QLabel(self.widget_p14)
        self.label_p14.setObjectName(u"label_p14")
        self.label_p14.setGeometry(QRect(0, 0, 54, 12))
        self.label_p14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p14_3 = QPushButton(self.widget_p14)
        self.pushButton_p14_3.setObjectName(u"pushButton_p14_3")
        self.pushButton_p14_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p14_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p14_3.setSizePolicy(sizePolicy)
        self.pushButton_p14_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p14_3.setIcon(icon2)
        self.pushButton_p14_1 = QPushButton(self.widget_p14)
        self.pushButton_p14_1.setObjectName(u"pushButton_p14_1")
        self.pushButton_p14_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p14_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p14_1.setSizePolicy(sizePolicy)
        self.pushButton_p14_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p14_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p14_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p14_1.setAutoRepeatDelay(300)
        self.pushButton_p14_1.setAutoRepeatInterval(100)
        self.pushButton_p14_1.setAutoDefault(False)
        self.label_p14_central = MyLabel(self.widget_p14)
        self.label_p14_central.setObjectName(u"label_p14_central")
        self.label_p14_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p14_central.raise_()
        self.label_p14.raise_()
        self.pushButton_p14_3.raise_()
        self.pushButton_p14_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p14, 1, 2, 1, 1)

        self.widget_p9 = QWidget(self.page_5)
        self.widget_p9.setObjectName(u"widget_p9")
        self.widget_p9.setLayoutDirection(Qt.LeftToRight)
        self.widget_p9.setAutoFillBackground(False)
        self.label_p9 = QLabel(self.widget_p9)
        self.label_p9.setObjectName(u"label_p9")
        self.label_p9.setGeometry(QRect(0, 0, 31, 16))
        sizePolicy1.setHeightForWidth(self.label_p9.sizePolicy().hasHeightForWidth())
        self.label_p9.setSizePolicy(sizePolicy1)
        self.label_p9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                    "background-color: transparent;")
        self.pushButton_p9_1 = QPushButton(self.widget_p9)
        self.pushButton_p9_1.setObjectName(u"pushButton_p9_1")
        self.pushButton_p9_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p9_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p9_1.setSizePolicy(sizePolicy)
        self.pushButton_p9_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p9_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p9_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                           "")
        self.pushButton_p9_1.setAutoRepeatDelay(300)
        self.pushButton_p9_1.setAutoRepeatInterval(100)
        self.pushButton_p9_1.setAutoDefault(False)
        self.pushButton_p9_3 = QPushButton(self.widget_p9)
        self.pushButton_p9_3.setObjectName(u"pushButton_p9_3")
        self.pushButton_p9_3.setGeometry(QRect(260, 0, 30, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p9_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p9_3.setSizePolicy(sizePolicy)
        self.pushButton_p9_3.setMinimumSize(QSize(30, 0))
        self.pushButton_p9_3.setMaximumSize(QSize(30, 16777215))
        self.pushButton_p9_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p9_3.setIcon(icon2)
        self.label_p9_central = MyLabel(self.widget_p9)
        self.label_p9_central.setObjectName(u"label_p9_central")
        self.label_p9_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p9_central.raise_()
        self.label_p9.raise_()
        self.pushButton_p9_1.raise_()
        self.pushButton_p9_3.raise_()

        self.gridLayout_15.addWidget(self.widget_p9, 0, 0, 1, 1)

        self.widget_p16 = QWidget(self.page_5)
        self.widget_p16.setObjectName(u"widget_p16")
        self.label_p16 = QLabel(self.widget_p16)
        self.label_p16.setObjectName(u"label_p16")
        self.label_p16.setGeometry(QRect(0, 0, 54, 12))
        self.label_p16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p16_3 = QPushButton(self.widget_p16)
        self.pushButton_p16_3.setObjectName(u"pushButton_p16_3")
        self.pushButton_p16_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p16_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p16_3.setSizePolicy(sizePolicy)
        self.pushButton_p16_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p16_3.setIcon(icon2)
        self.pushButton_p16_1 = QPushButton(self.widget_p16)
        self.pushButton_p16_1.setObjectName(u"pushButton_p16_1")
        self.pushButton_p16_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p16_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p16_1.setSizePolicy(sizePolicy)
        self.pushButton_p16_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p16_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p16_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p16_1.setAutoRepeatDelay(300)
        self.pushButton_p16_1.setAutoRepeatInterval(100)
        self.pushButton_p16_1.setAutoDefault(False)
        self.label_p16_central = MyLabel(self.widget_p16)
        self.label_p16_central.setObjectName(u"label_p16_central")
        self.label_p16_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p16_central.raise_()
        self.label_p16.raise_()
        self.pushButton_p16_3.raise_()
        self.pushButton_p16_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p16, 2, 1, 1, 1)

        self.widget_p12 = QWidget(self.page_5)
        self.widget_p12.setObjectName(u"widget_p12")
        self.label_p12 = QLabel(self.widget_p12)
        self.label_p12.setObjectName(u"label_p12")
        self.label_p12.setGeometry(QRect(0, 0, 54, 12))
        self.label_p12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                     "background-color: transparent;")
        self.pushButton_p12_3 = QPushButton(self.widget_p12)
        self.pushButton_p12_3.setObjectName(u"pushButton_p12_3")
        self.pushButton_p12_3.setGeometry(QRect(260, 0, 28, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p12_3.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_3.setSizePolicy(sizePolicy)
        self.pushButton_p12_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p12_3.setIcon(icon2)
        self.pushButton_p12_1 = QPushButton(self.widget_p12)
        self.pushButton_p12_1.setObjectName(u"pushButton_p12_1")
        self.pushButton_p12_1.setGeometry(QRect(200, 0, 60, 24))
        sizePolicy.setHeightForWidth(self.pushButton_p12_1.sizePolicy().hasHeightForWidth())
        self.pushButton_p12_1.setSizePolicy(sizePolicy)
        self.pushButton_p12_1.setMinimumSize(QSize(60, 24))
        self.pushButton_p12_1.setMaximumSize(QSize(60, 24))
        self.pushButton_p12_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_p12_1.setAutoRepeatDelay(300)
        self.pushButton_p12_1.setAutoRepeatInterval(100)
        self.pushButton_p12_1.setAutoDefault(False)
        self.label_p12_central = MyLabel(self.widget_p12)
        self.label_p12_central.setObjectName(u"label_p12_central")
        self.label_p12_central.setGeometry(QRect(10, 0, 270, 180))
        self.label_p12_central.raise_()
        self.label_p12.raise_()
        self.pushButton_p12_3.raise_()
        self.pushButton_p12_1.raise_()

        self.gridLayout_15.addWidget(self.widget_p12, 1, 0, 1, 1)

        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.stackedWidget_3.addWidget(self.page_5)

        self.gridLayout_5.addWidget(self.stackedWidget_3, 1, 0, 1, 1)

        self.gridLayout_13.addLayout(self.gridLayout_5, 0, 1, 1, 1)

        self.gridLayout_18.addWidget(self.widget_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_11.setDefault(False)
        self.stackedWidget_13.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(3)
        self.pushButton_p1_1.setDefault(False)
        self.pushButton_p2_1.setDefault(False)
        self.pushButton_p3_1.setDefault(False)
        self.pushButton_p7_1.setDefault(False)
        self.pushButton_p4_1.setDefault(False)
        self.pushButton_p5_1.setDefault(False)
        self.pushButton_p6_1.setDefault(False)
        self.pushButton_p17_1.setDefault(False)
        self.pushButton_p11_1.setDefault(False)
        self.pushButton_p10_1.setDefault(False)
        self.pushButton_p15_1.setDefault(False)
        self.pushButton_p13_1.setDefault(False)
        self.pushButton_p14_1.setDefault(False)
        self.pushButton_p9_1.setDefault(False)
        self.pushButton_p16_1.setDefault(False)
        self.pushButton_p12_1.setDefault(False)

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
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u5217\u8868", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None))
        self.label_321.setText(
            QCoreApplication.translate("MainWindow", u"\u672a\u9009\u62e9\u5de5\u7a0b\u6587\u4ef6", None))
        self.label_311.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u7a0b\u540d\u79f0", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u" \u8fd0\u884c", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u" \u7ed3\u675f", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u" \u6392\u7248", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u76f8\u673a\u6570\u91cf", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u6570\u91cf\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"9", None))

        self.ptn_ok.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.ptn_cancel.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2),
                                    QCoreApplication.translate("MainWindow", u"\u6392\u7248\u8bbe\u5b9a", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5),
                                    QCoreApplication.translate("MainWindow", u"\u53c2\u6570\u8bbe\u5b9a", None))
        self.label_p1.setText(QCoreApplication.translate("MainWindow", u" CCD1", None))
        self.pushButton_p1_3.setText("")
        self.pushButton_p1_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p1_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p2.setText(QCoreApplication.translate("MainWindow", u" CCD1", None))
        self.pushButton_p2_3.setText("")
        self.pushButton_p2_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p2_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p3.setText(QCoreApplication.translate("MainWindow", u" CCD2", None))
        self.pushButton_p3_3.setText("")
        self.pushButton_p3_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p3_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p7.setText(QCoreApplication.translate("MainWindow", u" CCD4", None))
        self.pushButton_p7_3.setText("")
        self.pushButton_p7_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f", None))
        self.pushButton_p7_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p7_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p4.setText(QCoreApplication.translate("MainWindow", u" CCD1", None))
        self.pushButton_p4_3.setText("")
        self.pushButton_p4_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f", None))
        self.pushButton_p4_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p4_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p5.setText(QCoreApplication.translate("MainWindow", u" CCD2", None))
        self.pushButton_p5_3.setText("")
        self.pushButton_p5_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f", None))
        self.pushButton_p5_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p5_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p6.setText(QCoreApplication.translate("MainWindow", u" CCD3", None))
        self.pushButton_p6_3.setText("")
        self.pushButton_p6_2.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f", None))
        self.pushButton_p6_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p6_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p17.setText(QCoreApplication.translate("MainWindow", u" CCD9", None))
        self.pushButton_p17_3.setText("")
        self.pushButton_p17_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p17_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p11.setText(QCoreApplication.translate("MainWindow", u" CCD3", None))
        self.pushButton_p11_3.setText("")
        self.pushButton_p11_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p11_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p10.setText(QCoreApplication.translate("MainWindow", u" CCD2", None))
        self.pushButton_p10_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.pushButton_p10_3.setText("")
        self.label_p10_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p15.setText(QCoreApplication.translate("MainWindow", u" CCD7", None))
        self.pushButton_p15_3.setText("")
        self.pushButton_p15_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p15_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p13.setText(QCoreApplication.translate("MainWindow", u" CCD5", None))
        self.pushButton_p13_3.setText("")
        self.pushButton_p13_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p13_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p14.setText(QCoreApplication.translate("MainWindow", u" CCD6", None))
        self.pushButton_p14_3.setText("")
        self.pushButton_p14_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p14_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p9.setText(QCoreApplication.translate("MainWindow", u" CCD1", None))
        self.pushButton_p9_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.pushButton_p9_3.setText("")
        self.label_p9_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p16.setText(QCoreApplication.translate("MainWindow", u" CCD8", None))
        self.pushButton_p16_3.setText("")
        self.pushButton_p16_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p16_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_p12.setText(QCoreApplication.translate("MainWindow", u" CCD4", None))
        self.pushButton_p12_3.setText("")
        self.pushButton_p12_1.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u7f16\u8bd1", None))
        self.label_p12_central.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))

    # retranslateUi

    def setcss(self):
        '''设置样式'''
        self.widget_4.hide() #提示隐藏

        self.label_311.setText(globalsdynamic.row)
        self.label_321.setText(globalsdynamic.value)

        self.widget_6.setMaximumSize(QSize(200,16777215))
        self.widget_6.setMinimumSize(QSize(200, 0))
        self.label_311.setAlignment(Qt.AlignCenter)  # 设置文本居中
        self.label_321.setAlignment(Qt.AlignCenter)  # 设置文本居中

        # 图像显示窗口内控件
        self.class_page_widget = [[self.widget_p1], [self.widget_p2, self.widget_p3],
                                   [self.widget_p4, self.widget_p5, self.widget_p6, self.widget_p7],
                                   [self.widget_p9, self.widget_p10, self.widget_p11, self.widget_p12, self.widget_p13,self.widget_p14, self.widget_p15, self.widget_p16, self.widget_p17]]
        self.label_central_class = [[self.label_p1_central], [self.label_p2_central, self.label_p3_central],
                                         [self.label_p4_central, self.label_p5_central, self.label_p6_central,self.label_p7_central],
                                         [self.label_p9_central, self.label_p10_central, self.label_p11_central,self.label_p12_central, self.label_p13_central,self.label_p14_central, self.label_p15_central, self.label_p16_central,self.label_p17_central]]
        self.class_page_label = [[self.label_p1], [self.label_p2, self.label_p3],
                                   [self.label_p4, self.label_p5, self.label_p6, self.label_p7],
                                   [self.label_p9, self.label_p10, self.label_p11, self.label_p12, self.label_p13,self.label_p14, self.label_p15, self.label_p16, self.label_p17]]
        self.class_page_btns1 = [[self.pushButton_p1_1],
                               [self.pushButton_p2_1,self.pushButton_p3_1],
                               [self.pushButton_p4_1,self.pushButton_p5_1,self.pushButton_p6_1,self.pushButton_p7_1],
                               [self.pushButton_p9_1,self.pushButton_p10_1,self.pushButton_p11_1,self.pushButton_p12_1,self.pushButton_p13_1,self.pushButton_p14_1,self.pushButton_p15_1,self.pushButton_p16_1,self.pushButton_p17_1]]
        self.class_page_btns3 = [[self.pushButton_p1_3],
                               [self.pushButton_p2_3,self.pushButton_p3_3],
                               [self.pushButton_p4_3,self.pushButton_p5_3,self.pushButton_p6_3,self.pushButton_p7_3],
                               [self.pushButton_p9_3,self.pushButton_p10_3,self.pushButton_p11_3,self.pushButton_p12_3,self.pushButton_p13_3,self.pushButton_p14_3,self.pushButton_p15_3,self.pushButton_p16_3,self.pushButton_p17_3]]

        for i in self.class_page_widget:
            for j in i:
                j.setStyleSheet("background-color: black;")

        # self.pushButton_11.setStyleSheet(u"background-color: rgb(0, 0, 0);")

class Ui_configure(QDialog,):
    '''项目管参数配置窗口ui'''
    # 定义信号
    _signal = QtCore.pyqtSignal(str,str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setcss()
        self.signalSlotConnection()

        self.item_names = get_file_name(Globals.datas_path)  # 存储项目文件目录
        # self.item_names = [i.split('：')[1] for i in self.existing_values]

        if len(self.item_names) >= 1:
            # 设置第1行第2列的单元格为选中状态
            self.tableWidget.setCurrentCell(0, 1)

        self.init_label()


    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.setWindowModality(Qt.ApplicationModal)
        Frame.resize(400, 300)
        icon = QIcon()
        icon.addFile(u":/logo/icon/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Frame.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(Frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 1):
            self.tableWidget.setColumnCount(1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(1)

        self.verticalLayout.addWidget(self.tableWidget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.tab)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.retranslateUi(Frame)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"\u9879\u76ee\u7ba1\u7406", None))
        self.pushButton.setText(QCoreApplication.translate("Frame", u"\u786e\u8ba4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Frame", u"\u9879\u76ee\u6587\u4ef6\u7ba1\u7406", None))
    # retranslateUi


    def signalSlotConnection(self):
        '''设置信号-槽'''
        self.pushButton.clicked.connect(self.onConfirmClick)
        self.tableWidget.cellDoubleClicked.connect(self.onConfirmClick)

    def onConfirmClick(self):
        '''确定按钮按下时执行'''
        selected_item = self.tableWidget.currentItem() # 选中的行
        if selected_item:
            row = selected_item.row()
            column = selected_item.column()
            value = selected_item.text()
            # 发射信号
            self._signal.emit(str(row+1),str(value))
        else:
            self._signal.emit('', '')

    def show_context_menu(self, pos):
        '''右键操作栏'''
        menu = QMenu(self)

        new_action = QAction('新建', self)
        new_action.triggered.connect(lambda: self.show_new_item_dialog('新建'))
        menu.addAction(new_action)

        delete_action = QAction('删除', self)
        delete_action.triggered.connect(self.delete_row)
        menu.addAction(delete_action)

        rename_action = QAction('重命名', self)
        selected_item = self.tableWidget.currentItem()
        if selected_item:
            rename_action.triggered.connect(lambda: self.show_new_item_dialog('重命名', selected_item.text()))
        else:
            rename_action.triggered.connect(lambda: self.show_new_item_dialog('重命名'))
        menu.addAction(rename_action)

        menu.exec_(self.tableWidget.viewport().mapToGlobal(pos))

    def show_new_item_dialog(self,type, default_text=''):
        '''弹出对话框'''
        if type == '重命名' and default_text == '':
            QMessageBox.warning(self, "错误", "未选中项目.")
            return
        dialog = NewItemDialog(self,type,default_text)
        if dialog.exec_() == QDialog.Accepted:
            text = dialog.input_text.text()
            text = text.strip()  # 删除了开头和结尾的空格
            if text:
                # print(text)
                if text in self.item_names:
                    QMessageBox.warning(self, "错误", "已经有同名的项目了.")
                else:
                    if type == '新建':
                        self.add_row(text)
                    elif type == '重命名':
                        self.rename_row(text)
            else:
                QMessageBox.warning(self, "错误", "项目名不能为空.")

    def set_ID(self,count):
        # 设置第一列的值为当前行的索引+1
        item = QTableWidgetItem()
        item.setText(str(count+1))
        item.setBackground(QColor("#b3c7e6"))
        item.setForeground(QColor("#000000"))
        item.setFlags(item.flags() & ~Qt.ItemIsEnabled ) # 不可操作
        self.tableWidget.setItem(count, 0, item)

    def init_label(self):
        for i in self.item_names:
            self.add_row(i,False)

    def add_row(self,text,flag=True):
        '''增加行'''
        try:
            row_count = self.tableWidget.rowCount() # 总行数

            # 新建项目文件
            if flag:
                path_name = path_join(Globals.datas_path,text)
                make_new_folder(path_name)
                self.item_names.append(text)
                write_new_json(path_join(path_name,'data.json'))

            self.tableWidget.insertRow(row_count) # 插入一行

            # 设置第一列的值为当前行的索引
            self.set_ID(row_count)

            # 内容的标志为只读
            for column in range(self.tableWidget.columnCount()):
                # header_item = self.tableWidget.horizontalHeaderItem(column)
                # header_item.setFlags(header_item.flags() & ~Qt.ItemIsEditable)
                item = QTableWidgetItem()
                item.setText(text)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(row_count, 1, item)

            if len(self.item_names) == 1:
                # 设置第1行第2列的单元格为选中状态
                self.tableWidget.setCurrentCell(0, 1)

            # 更新数据库
            data = {'name': text}
            Globals.db_main.create_tables('Project', ['name', 'temppath'])
            Globals.db_main.insert_data('Project', data)

        except Exception as e:
            logging.error(f"【新建项目文件报错：{e}】")
        else:
            if flag:
                QMessageBox.information(self, "提示", f"项目{text}创建成功.")


    def delete_row(self):
        '''删除所选行'''
        try:
            selected_item = self.tableWidget.currentItem() # 选中的行
            row_count = self.tableWidget.rowCount()  # 总行数
            if selected_item:
                row = selected_item.row()
                # 删除项目文件
                text = self.item_names[int(row)]
                path_name = path_join(Globals.datas_path, text)
                if globalsdynamic.data_path == path_name:  # 若删除的项目正在使用
                    QMessageBox.information(self, "提示", f"项目{text}正在使用！")
                    return
                    # globalsdynamic.db_data.close() # 关闭数据库连接，否则无法删除
                    # Globals.db_main.delete_row('Now', "name = 'now'")
                self.tableWidget.removeRow(row)

                delete_folder(path_name)
                self.item_names.pop(row)

                # 更新编号
                for i in range(len(self.item_names)):
                    # 设置第一列的值为当前行的索引
                    self.set_ID(i)

                if len(self.item_names) == 1:
                    # 设置第1行第2列的单元格为选中状态
                    self.tableWidget.setCurrentCell(0, 1)

                # 更新数据库
                Globals.db_main.delete_row_if("Project", f"name = {text}")
                globalsdynamic.update_main_path()


        except Exception as e:
            logging.error(f"【新建项目文件报错：{e}】")
            QMessageBox.information(self, "提示", f"项目{text}删除失败：{e}")
        else:
            QMessageBox.information(self, "提示", f"项目{text}删除成功.")

    def rename_row(self,text):
        '''重命名项目名'''
        try:
            selected_item = self.tableWidget.currentItem()

            if selected_item:
                row = selected_item.row()

                # 重命名项目文件
                oldtext = self.item_names[int(row)]
                path_name = path_join(Globals.datas_path, oldtext)
                new_path_name = path_join(Globals.datas_path, text)
                if globalsdynamic.data_path == path_name: # 若操作的项目正在使用
                #     globalsdynamic.db_data.close() # 关闭数据库连接，否则无法删除
                #     data = {'name': 'now',
                #             'value': text}
                #     Globals.db_main.insert_data('Now', data)
                    QMessageBox.information(self, "提示", f"项目{oldtext}正在使用！")
                    return
                rename_file(path_name, new_path_name)
                self.item_names[row] = text

                item = QTableWidgetItem()
                item.setText(text)
                item.setFlags(item.flags() & ~Qt.ItemIsEditable)
                self.tableWidget.setItem(row, 1, item)

                # 更新数据库
                data = {'name': text}
                Globals.db_main.update_data_row('Project', oldtext, data)
                globalsdynamic.update_main_path()
        except Exception as e:
            logging.error(f"【重命名项目文件报错：{e}】")
            QMessageBox.warning(self, "错误", f"重命名项目文件报错:{e}")
        else:
            QMessageBox.information(self, "提示", f"项目{text}重命名成功.")

    def setcss(self):
        '''设置样式'''
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(['编号', '项目'])
        self.tableWidget.verticalHeader().setVisible(False) # 设置垂直表头为不可见
        header = self.tableWidget.horizontalHeader() # 获取表头部件
        header.setSectionResizeMode(1, QHeaderView.Stretch)  # 设置第一列自动调整宽度
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)  # 设置第二列根据内容调整宽度
        width = header.sectionSize(1) // 2
        header.resizeSection(0, width)  # 设置第一列宽度为第二列宽度的一半
        header.setHighlightSections(False) # # 设置表头的高亮显示为不可选中

        # self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置选择模式为单选
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection) # 设置选择模式为单选
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectItems) # 设置择行为为选择单元格
        self.tableWidget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter) # 设置表格的水平对齐方式为居中对齐
        self.tableWidget.setTextElideMode(Qt.ElideRight) # 设置表格的文本溢出策略为省略号
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel) # 设置表格的水平滚动条策略为自动滚动

        # 设置表格样式
        self.tableWidget.verticalHeader().setStyleSheet("""
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
        self.tableWidget.horizontalHeader().setStyleSheet("""
            QHeaderView::section {
                background-color: #b3c7e6;
                color: #333333;
                padding: 5px;
            }
        """)

        # 设置表格列宽
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setColumnWidth(1, 200)

        # 设置表格字体
        font = QFont('Arial', 10)
        self.tableWidget.setFont(font)

        # 设置行交替颜色
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setStyleSheet("""
            QTableView::item {
                background-color: #ffffff;
            }

            QTableView::item:alternate {
                background-color: #e0e0e0;
            }
        """)
        self.tableWidget.setStyleSheet("QTableWidget::item:selected { background-color: blue; }")

        # 设置右键菜单
        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget.customContextMenuRequested.connect(self.show_context_menu)

