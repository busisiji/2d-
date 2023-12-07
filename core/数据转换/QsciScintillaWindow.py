import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from func_timeout import func_set_timeout

from core.PopUpWindow import QsciParameterDialog
from core.utils_window import utilsWindow
from core.数据转换.QsciOperateDb import QsciOperateDb
from core.流程树.node.node_node import Node
from lib.path import Globals, globalsdynamic
from core.MyClass import MyTableWidget
from core.CodeCompilerClass import  codeCompilerVBS


class Stream(QObject):
    """Redirects console output to text widget."""
    newText = pyqtSignal(str)

    def write(self, text):
        self.newText.emit(str(text))

class QsciTableWidget(MyTableWidget):
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

    def getparameterName(self):
        if self.objectName() == 'tableWidget_4':
            self.parameterName = 'input'
        elif self.objectName() == 'tableWidget_5':
            self.parameterName = 'output'
        return self.parameterName

    def delete_row(self):
        """删除行"""
        currentRow = self.currentRow() # 当前选中行数
        item = self.item(currentRow, 1)
        text = item.text() if item else []
        self._signaldelete.emit([text],self.parameterName) # 删除预设参数
        super().delete_row(db_name=None) # 放在前面会先先删掉选中行
        self.updata_table_data_db()
        if not self.rowCount():
            self.insertRow(0)  # 插入一行

    def clear_row(self, noClearDb = False):
        """清空行"""
        super().clear_row(db_name=None)
        if not noClearDb:
            self._signalclear.emit(self.parameterName)
            self.updata_table_data_db()
            if not self.rowCount():
                self.insertRow(0)  # 插入一行

    def show_parameter_dialog(self, row):
        """双击增加一行"""
        # 创建参数子窗口并显示
        dialog = QsciParameterDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            # 如果点击了确定按钮，则将参数设置为编辑框中的内容
            parameter = dialog.get_parameter()
            find_row = self.find_same_name(parameter[1], 1)
            if not find_row or row == find_row:
                # 表格增加行
                self.set_row_data(row, parameter)
                # 增加预设参数
                self._signaladdAction.emit(self.parameterName, row, parameter[1])
                # 更新数据库
                self.updata_table_data_db()
            else:
                QMessageBox.information(self, "错误", "名称不能重复！")

    def get_save_data(self):
        """表格数据保持到seld.save_data中"""
        self.save_data = {'types': [], 'texts': [], 'icons': []}
        self.save_data['id'] = Globals.node_index
        self.save_data['title'] = '数据转换'
        # 两个表格的参数一起写入通用行数据库
        if self.getparameterName() == 'input':
            self.get_table_data(self)
            self.get_table_data(self.parent().window().ChildVision.tableWidget_5)
        elif self.getparameterName() == 'output':
            self.get_table_data(self.parent().window().ChildVision.tableWidget_4)
            self.get_table_data(self)
    def get_table_data(self, tableWidget):
        """获取表格数据"""
        for row in range(tableWidget.rowCount()):
            for column in range(tableWidget.columnCount()):
                item = tableWidget.item(row, column)
                if not item:
                    continue
                if column == 0:
                    self.save_data['types'].append(item.text())  # 获取每一行的数据
                elif column == 1:
                    self.save_data['texts'].append(item.text())  # 获取每一行的数据
            if not tableWidget.item(row, 0) and not tableWidget.item(row, 1):
                continue
            if tableWidget.getparameterName() == 'input':
                self.save_data['icons'].append(1)
            elif tableWidget.getparameterName() == 'output':
                self.save_data['icons'].append(0)

    def updata_table_data_db(self):
        """参数表格更新数据"""
        # 获取新图元
        self.get_save_data()
        tree = self.parent().window().ChildVision.nodeEditWind
        new_node = Node(tree.scene, self.save_data['title'], self.save_data['types'], self.save_data['texts'],
                        self.save_data['icons'], isNew=False)

        # 更新流程树
        tree.scene.updataNode(Globals.node_index-1,new_node)
        # 流程树数据库保存
        globalsdynamic.db_child.insert_data('Node', self.save_data,'id')

        # 数据转换数据库新增数据
        self.data = {}
        self.data['id'] = Globals.node_index
        if self.getparameterName() == 'input':
            self.data['inputType'] = self.get_column_data(0)
            self.data['inputName'] = self.get_column_data(1)
        elif self.getparameterName() == 'output':
            self.data['outputType'] = self.get_column_data(0)
            self.data['outputName'] = self.get_column_data(1)
        QsciOperateDb.add_data(self.data)

    def setcss(self, table):
        super().setcss(table)
        self.setSelectionBehavior(QTableWidget.SelectRows)  # 设置选择行为为选择整行
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 将表格变为禁止编辑

class QsciScintillaWindow(utilsWindow):
    '''数据转换界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision

        self.isolated = True

        self.signalSlotConnection()
    def signalSlotConnection(self):
        self.signal = [self.ChildVision.pushButton_48,self.ChildVision.pushButton_14,self.ChildVision.pushButton_47,
                       self.ChildVision.tableWidget_4._signaldelete,self.ChildVision.tableWidget_5._signaldelete,
                       self.ChildVision.tableWidget_4._signalclear,self.ChildVision.tableWidget_5._signalclear,
                       self.ChildVision.tableWidget_4._signaladdAction, self.ChildVision.tableWidget_5._signaladdAction
                       ]
        super().signalSlotConnection()

        self.ChildVision.pushButton_48.clicked.connect(self.code_svae) # 保存数据
        self.ChildVision.pushButton_14.clicked.connect(self.code_run) # 运行代码
        self.ChildVision.tableWidget_4._signaldelete.connect(self.ChildVision.widget_31.deleteMenuAction)
        self.ChildVision.tableWidget_5._signaldelete.connect(self.ChildVision.widget_31.deleteMenuAction)
        self.ChildVision.tableWidget_4._signaldelete.connect(self.ChildVision.widget_34.deleteMenuAction)
        self.ChildVision.tableWidget_5._signaldelete.connect(self.ChildVision.widget_34.deleteMenuAction)
        self.ChildVision.tableWidget_4._signalclear.connect(self.ChildVision.widget_31.clearMenuAction)
        self.ChildVision.tableWidget_5._signalclear.connect(self.ChildVision.widget_31.clearMenuAction)
        self.ChildVision.tableWidget_4._signalclear.connect(self.ChildVision.widget_34.clearMenuAction)
        self.ChildVision.tableWidget_5._signalclear.connect(self.ChildVision.widget_34.clearMenuAction)
        self.ChildVision.tableWidget_4._signaladdAction.connect(self.ChildVision.widget_31.setMenuAction)
        self.ChildVision.tableWidget_5._signaladdAction.connect(self.ChildVision.widget_31.setMenuAction)
        self.ChildVision.tableWidget_4._signaladdAction.connect(self.ChildVision.widget_34.setMenuAction)
        self.ChildVision.tableWidget_5._signaladdAction.connect(self.ChildVision.widget_34.setMenuAction)
        self.ChildVision.pushButton_47.clicked.connect(self.window_close)

    @func_set_timeout(Globals.timeout)  # 设定函数超执行时间_
    def run(self, module_input):
        datas = self.get_input_datas(module_input)
        result = self.code_run(datas)
        return result,[]

    def get_input_datas(self,module_input):
        """获取输入参数"""
        module_input = [input if input else '' for input in module_input]
        datas = {}
        inputs = self.ChildVision.tableWidget_4.get_column_data(1)
        for i in range(len(inputs)):
            input = inputs[i]
            datas[input] = module_input[i] if i < len(module_input) else ''
        return datas

    def get_output_datas(self,datas):
        """增加输出参数"""
        outputs = self.ChildVision.tableWidget_5.get_column_data(1)
        for output in outputs:
            datas[output] = ''
        return datas

    def code_run(self,datas={}):
        """代码运行"""

        texts = []
        inputs = self.ChildVision.tableWidget_4.get_column_data(1)
        for i in range(len(inputs)):
            texts.append(self.get_input(i))
        if not datas:
            datas = self.get_input_datas(texts)
        datas = self.get_output_datas(datas)
        if self.ChildVision.tabWidget_10.currentIndex() == 0:
            result = self.ChildVision.widget_31.btn_action(datas)
        else:
            result = self.ChildVision.widget_34.btn_action(datas)
            result = texts + result
        # if self.isolated:
        #     node = self.ChildVision.nodeEditWind.scene.nodes[Globals.node_index]
        #     node.updata_tip(result)
        return result

    def code_svae(self):
        """代码保存"""
        self.ChildVision.widget_31.confirm_btn_action()
        self.ChildVision.widget_34.confirm_btn_action()

    def save_data(self):
        """数据库保存"""
        data = {'type':self.ChildVision.tabWidget_10.currentIndex()}
        QsciOperateDb.add_data(data)

    def window_close(self):
        '''关闭窗口'''
        self.save_data()
        super().window_close()
        # sys.stdout = sys.__stdout__



if __name__ == '__main__':
    app = QApplication(sys.argv)
    # myGUI = codeCompilerPy()
    myGUI = codeCompilerVBS()
    sys.exit(app.exec_())
