import sys

from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from func_timeout import func_set_timeout

from core.MyClass import MyTableWidget
from core.utils_window import utilsWindow
from core.数据合并.PooleOperateDb import PooleOperateDb
from core.流程树.node.node_node import Node
from core.自定义输出.OutputOperateDb import OutputOperateDb
from lib.data import convert_JSON, Merge
from lib.path import globalsdynamic, Globals

class OutputParameterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        """参数输入窗口"""
        self.parent = parent
        self.setWindowTitle("自定义输出参数")

        # 创建参数标签和文本框
        self.parameter_label1 = QLabel("类型：")
        # 创建 QComboBox 控件
        self.combo_box1 = QComboBox()

        for type in Globals.types[:-1]:
            self.combo_box1.addItem(type)

        # 添加控件
        self.label = QLabel('组成参数的数据数量：')
        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(1)
        self.spin_box.setMaximum(100)
        self.spin_box.setValue(1)

        # 创建确定按钮和取消按钮
        self.ok_button = QPushButton("确定")
        self.cancel_button = QPushButton("取消")
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)

        # 创建布局并添加控件
        layout = QVBoxLayout()
        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(self.parameter_label1)
        h_layout_1.addWidget(self.combo_box1)
        h_layout_1.addWidget(self.label)
        h_layout_1.addWidget(self.spin_box)
        self.line_edit_widget = QWidget()
        self.line_edit_layout = QGridLayout(self.line_edit_widget)
        self.line_edit_scroll = QScrollArea()
        self.line_edit_scroll.setWidgetResizable(True)
        self.line_edit_scroll.setWidget(self.line_edit_widget)
        layout.addLayout(h_layout_1)
        layout.addWidget(self.line_edit_scroll)
        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(self.ok_button)
        h_layout_2.addWidget(self.cancel_button)
        layout.addLayout(h_layout_2)
        self.setLayout(layout)
        # 初始化line edit控件
        self.labels = []
        self.line_edits = []

        # 限制数据类型
        # 根据parameter_label1的文本设置验证器
        self.validator = None  # 声明验证器变量

        self.init()

        # 更改spin_box的信号连接
        self.combo_box1.currentIndexChanged.connect(self.update_validator)
        self.spin_box.editingFinished.connect(self.update_line_edits)

    def init(self):
        """初始化"""
        self.update_line_edits()  # 初始化line edit控件
        self.update_validator()  # 初始化验证器

    def init_dialog_data(self,type,parameter):
        """初始化窗口数据"""
        if type:
            self.combo_box1.setCurrentText(type)
            self.update_validator()
        if parameter:
            parameters = parameter.split('|')
            self.spin_box.setValue(len(parameters))
            if self.update_line_edits():
                for i in range(len(parameters)):
                    line_edit = self.line_edits[i]
                    text = parameters[i]
                    line_edit.setText(text)

    def clear_str_lineedit(self):
        """清空所有带字符的LineEdit的内容"""
        pos = 0
        for line_edit in self.line_edits:
            text = line_edit.text()
            if not self.validator.validate(text, pos)[0] == QIntValidator.Acceptable:
                line_edit.clear()

    def update_validator(self):
        """初始化验证器"""
        # 根据parameter_label1的文本设置验证器
        if self.combo_box1.currentText() == '数值' or self.combo_box1.currentText() == '点':
            self.validator = QDoubleValidator() # 只允许输入数字
            self.clear_str_lineedit()
        else:
            self.validator = None  # 默认情况下允许任何输入
        # 设置验证器
        for line_edit in self.line_edits:
            line_edit.setValidator(self.validator)

    def update_line_edits(self):
        """更新line edit控件数量"""
        num_line_edits = self.spin_box.value()
        if self.combo_box1.currentText() == '点' and num_line_edits%2!=0:
            QMessageBox.information(self, "错误", "点类型必须两两结合，组成参数的数据数量必须为偶数！")
            return False
        while len(self.line_edits) < num_line_edits:
            num = len(self.line_edits)
            label = QLabel()
            label.setText(f'第{num + 1}个数据：')
            line_edit = QLineEdit()
            self.labels.append(label)
            self.line_edits.append(line_edit)
            self.line_edit_layout.addWidget(label, num, 0, 1, 1)
            self.line_edit_layout.addWidget(line_edit,num,1,1,1)
        while len(self.line_edits) > num_line_edits:
            label = self.labels.pop()
            line_edit = self.line_edits.pop()
            self.line_edit_layout.removeWidget(label)
            self.line_edit_layout.removeWidget(line_edit)
            label.deleteLater()
            line_edit.deleteLater()
        # 设置验证器
        for line_edit in self.line_edits:
            line_edit.setValidator(self.validator)
        return True
class OutputtableWidget(MyTableWidget):
    _signaldelete = pyqtSignal(list,str)
    _signalclear = pyqtSignal(str)
    _signaladdAction = pyqtSignal(str,int,str)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """参数表格"""
        # 监听 QTableWidget 控件的双击信号
        self.cellDoubleClicked.connect(self.show_parameter_dialog)
        if self.rowCount() == 0:
            self.insertRow(0)  # 插入一行

    def init_table_data(self):
        """初始化表格数据"""
        self.clear()
        result = OutputOperateDb.get_row()
        if not result:
            return
        types = convert_JSON(result[1]) if result[1] else []
        parameters = convert_JSON(result[2]) if result[2] else []
        for row in range(len(types)):
            type = types[row]
            parameter = parameters[row]
            # 表格增加行
            self.set_row_data(row, [type, parameter])

        return parameters

    def delete_row(self):
        """删除行"""
        super().delete_row(db_name=None) # 放在前面会先先删掉选中行
        if not self.rowCount():
            self.insertRow(0)  # 插入一行
        self.updata_table_data_db()

    def clear_row(self):
        """清空行"""
        super().clear_row(db_name=None)
        if not self.rowCount():
            self.insertRow(0)  # 插入一行
        self.updata_table_data_db()

    def show_parameter_dialog(self, row):
        """双击增加一行"""
        # 创建参数子窗口并显示
        self.dialog = OutputParameterDialog(self)


        type = self.item(row, 0).text() if self.item(row, 0) else None
        parameter = self.item(row, 1).text() if self.item(row, 1) else None
        if type or parameter:
            self.dialog.init_dialog_data(type,parameter)

        self.parameter = ''
        if self.dialog.exec_() == QDialog.Accepted:
            for line_edit in self.dialog.line_edits:
                if line_edit.text():
                    self.parameter = self.parameter + line_edit.text() + '|'
            self.parameter = self.parameter.strip('|')
            # 表格增加行
            self.set_row_data(row, [self.dialog.combo_box1.currentText(),self.parameter])
            # 更新数据库
            self.updata_table_data_db()

    def get_table_data(self):
        """获取表格数据"""
        self.table_data = {'types':[],'texts':[]}
        for row in range(self.rowCount()):
            for column in range(self.columnCount()):
                item = self.item(row, column)
                if not item:
                    continue
                if column == 0:
                    self.table_data['types'].append(item.text())  # 获取每一行的数据
                elif column == 1:
                    self.table_data['texts'].append(item.text())  # 获取每一行的数据
            if not self.item(row, 0) and not self.item(row, 1):
                continue
        return self.table_data
    def updata_table_data_db(self):
        """参数表格更新数据"""
        OutputOperateDb.add_data(self.get_table_data())

    def setcss(self, table):
        super().setcss(table)
        self.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选择行为为选择整行
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 将表格变为禁止编辑

class OutputWindow(utilsWindow):
    '''数据转换界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision

        self.signalSlotConnection()

    def signalSlotConnection(self):
        self.signal = [self.ChildVision.pushButton_19,
                       ]
        super().signalSlotConnection()

        self.ChildVision.pushButton_19.clicked.connect(self.window_close)

    @func_set_timeout(Globals.timeout)  # 设定函数超执行时间_
    def run(self, module_input):
        table_data = self.ChildVision.tableWidget_2.get_table_data()
        return table_data['texts'],[]

    def updata_node_data(self):
        """参数表格更新数据"""
        table_data = self.ChildVision.tableWidget_2.get_table_data()
        if not table_data:
            return
        self.node_data = {
            'id': Globals.node_index,
            'title': '自定义输出',
            'types': table_data['types'],
            'texts': [],
            'icons': []
        }


        for i in range(len(self.node_data['types'])):
            self.node_data['texts'].append(self.node_data['types'][i])
            self.node_data['icons'].append(0)

        # 获取新图元
        tree = self.ChildVision.nodeEditWind
        new_node = Node(tree.scene,self.node_data['title'], self.node_data['types'], self.node_data['texts'], self.node_data['icons'], isNew=False)

        # 更新流程树
        tree.scene.updataNode(Globals.node_index-1,new_node)
        new_node.updata_tip(table_data['texts'])
        # 流程树数据库保存
        globalsdynamic.db_child.insert_data('Node', self.node_data,'id')

    def updata_tip(self,node=None,text=[]):
        if not node:
            node = self.ChildVision.nodeEditWind.scene.nodes[Globals.node_index-1]
        node.updata_tip(text)

    def save_data(self):
        """保存数据库"""
        data = {
            'type': self.ChildVision.comboBox_31.currentText(),
            'num':  self.ChildVision.spinBox_16.value()
        }
        PooleOperateDb.add_data(data)

    def window_close(self):
        self.updata_node_data()
        # self.save_data()
        super().window_close()