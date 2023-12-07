import sqlite3
import threading
import time

from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtWidgets import QMessageBox
from func_timeout import FunctionTimedOut

from core.MyClass import LoadingProgress
from core.图像设备.ImageCaptureWindow import ImageCaptureWindow, camera
from core.坐标标定.CameraCalibrationWindow import CameraCalibrationWindow
from core.数据转换.QsciScintillaWindow import QsciScintillaWindow
from core.模板匹配.ShapTemplateMatchingWindow import ShapTemplateMatchingWindow
from core.网络通讯.ModbusWindow import ModbusWindow
from core.颜色识别.ColorRecognitionWindow import ColorRecognitionWindow
from lib.path import globalsdynamic, Globals
from core.init_window import *


# class RunFlow(QThread):
class RunFlow():
    def __init__(self,MainWindow):
        super().__init__()
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision
        self.isRun = False
        self.timer = QTimer()

        self.scene = self.ChildVision.nodeEditWind.scene

    def run(self):
        """开始运行"""
        try:
            self.start_time = time.time()
            # self.ChildVision.toolButton_14.setEnabled(False)  # 运行按钮暂时不可用
            # 关闭参数窗口
            # self.ChildVision.stackedWidget.close()
            # # self.ChildVision.stackedWidget.hide()
            # self.ChildVision.widget_11.show()

            # # 多线程操作数据库
            # globalsdynamic.db_child.conn = sqlite3.connect(globalsdynamic.db_data_path, check_same_thread=False)
            # globalsdynamic.db_child.cursor = globalsdynamic.db_child.conn.cursor()
            if self.ChildVision.stackedWidget.isVisible() and Globals.node_index <= len(self.ChildVision.Childs):
                self.ChildVision.Childs[Globals.node_index-1].window_close()  # 保存退出当前参数窗口

            nConnectionNum = self.ChildVision.comboBox_14.currentIndex()
            if nConnectionNum == 0 or camera.g_bExit:  # 手动触发
                # self.loadingWindow = LoadingProgress()
                self.run_fun()
                self.MainWindow.ChildVisionCode.set_stop()
                # self.loadingWindow.close()
            elif nConnectionNum == 1 :  # 定时触发
                self.timer.timeout.connect(self.time_run)
                self.timer.start(1)  # 每隔time秒触发一次定时器
            elif nConnectionNum == 2:  # 外部触发
                # if
                self.run_fun()
        finally:
            globalsdynamic.update_temp()

    def stop(self):
        """停止运行"""
        self.timer.stop()
        self.MainWindow.ChildVisionCode.set_stop()

    def time_run(self):
        """定时运行"""
        print('====================',self.MainWindow.ChildVisionCode.isRun)
        if camera.g_bExit:
            self.timer.stop()
        if not self.isRun :
            self.run_fun()

    def get_module_input(self,start_node_index,start_socket_index,node_results=None):
        """获取模块输入参数"""
        if not node_results:
            node_results = globalsdynamic.db_child.query_data_table("Node")
        input_parameter = node_results[int(start_node_index)][Globals.nodekeys.index('parameters') + 1] if int(
            start_node_index) < len(node_results) else []  # 连接输入参数的图元的输入输出参数
        if not input_parameter:
            module_input=[]
        else:
            input_parameter = eval(input_parameter)
            module_input=input_parameter[int(start_socket_index)]
        return module_input

    def run_fun(self):

        if not globalsdynamic.temp_path:
            QMessageBox.warning(self.MainWindow, "错误", f"请先设置图像模板!")
            return
        node_results = globalsdynamic.db_child.query_data_table("Node")
        edge_results = globalsdynamic.db_child.query_data_table("Edge")
        if not node_results or not edge_results:  # 没有图元或连接线直接结束
            print('没有图元或连接线直接结束')
            return

        self.isRun = True # 是否运行中
        isFirst = True # 是否第一次显示框

        # 清空参数列
        globalsdynamic.db_child.clear_column("Node", 'parameters')
        # 设置参数字典 输入图元:输出图元，输入节点，输出节点
        parameters = {}
        for edge_result in edge_results:
            start_node_index, end_node_index, start_socket_index, end_socket_index = edge_result[1:]  # 连接点
            parameters[end_node_index,end_socket_index] = start_node_index, start_socket_index # 输入参数 只传入最后一条连接的值
        try:
            for i in range(len(node_results)):
                print(f'___________________________________第{i}个模块_______________________________________')
                start_time = time.time()
                # # 输入参数没有连接线的模块跳过
                # if i > 0 and str(i) not in [edge[2] for edge in edge_results]:
                #     continue
                Globals.node_index = i + 1  # 更新当前模块索引
                self.node = self.scene.nodes[i]  # 图元
                name = node_results[i][1]  # 模块名
                module = self.ChildVision.Childs[i]  # 模块
                module_input = []
                init_parameters(self.ChildVision, i)  # 参数初始化

                # 遍历输入参数连接点,获取输入参数
                for input_index in range(self.node.input_num):
                    start_node_index, start_socket_index = parameters[str(i),str(input_index)] if (str(i),str(input_index)) in parameters else (None,None)

                    if not start_node_index or not start_socket_index:
                        # module_input.append(None)
                        continue

                    module_input.append(self.get_module_input(start_node_index,start_socket_index,node_results))

                    boxs = node_results[int(start_node_index)][Globals.nodekeys.index('boxs') + 1] if int(
                        start_node_index) < len(node_results) else []  # 连接输入参数的图元的输出框
                    if not boxs:
                        boxs = []
                    else:
                        boxs = eval(boxs)
                # 没有输入参数跳过
                if name != '图像设备' and name != '自定义输出' and len(module_input)-module_input.count("")-module_input.count([])-module_input.count(None)==0:
                    # 有连接线没输入参数报错
                    if len(module_input) > 0:
                        self.ChildVision.nodeEditWind.scene.nodes[i].grNode.setResult('NG', int((time.time() - start_time) * 1000))
                    continue

                print('++++++++',module_input,i)
                module.isolated = False  # 是否单独运行
                try:
                    if name == '模板匹配':
                        if isFirst:
                            self.ChildVision.View.clearShowBox()
                            # # 清理文本
                            self.ChildVision.View.clearShowBoxText()
                            isFirst = False
                        # # 模块运行
                        self.module_output, boxs = module.run(module_input,boxs)
                    elif name == '颜色识别':
                        self.module_output, boxs = module.run(module_input, boxs,last_name=node_results[i-1][1])
                    else:
                        # # 模块运行
                        self.module_output,boxs = module.run(module_input)
                except FunctionTimedOut as e:
                    # 超时报错
                    # text = self.node.updata_tip()
                    self.ChildVision.nodeEditWind.scene.nodes[i].grNode.setResult('NG',int((time.time()-start_time)*1000))
                    continue
                except Exception as e:
                    # 异常报错
                    self.ChildVision.nodeEditWind.scene.nodes[i].grNode.setResult('NG', int((time.time() - start_time) * 1000))
                    continue

                globalsdynamic.db_child.update_data_if("Node","parameters",self.module_output,f'id = "{i+1}"')
                globalsdynamic.db_child.update_data_if("Node", "boxs",boxs, f'id = "{i + 1}"')
                node_results = globalsdynamic.db_child.query_data_table("Node")
                # 结果显示
                self.node.updata_tip(self.module_output)
                self.ChildVision.nodeEditWind.scene.nodes[i].grNode.setResult('OK',int((time.time()-start_time)*1000))



        except Exception as e:
            print(e)
                # QMessageBox.warning(self.MainWindow, "错误", f"运行失败{e}")
        finally:
            self.isRun = False
            module.isolated = True  # 是否单独运行
            globalsdynamic.update_temp()
            print('____________________|', time.time()-self.start_time)






