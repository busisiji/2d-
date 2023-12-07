# !/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import threading
import time
from collections import Counter

from PIL import Image
from PyQt5.QtCore import QSizeF, Qt, pyqtSignal, QSize, QPointF, QTimer
from PyQt5.QtGui import QImage, QPen, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QListView, QAbstractItemView, QListWidgetItem, \
    QWidget, QLabel, QVBoxLayout, QCheckBox, QApplication

from core.utils_window import utilsWindow
from core.模板匹配.STMOperateDb import STMOperateDb
from core.模板匹配.ShapTemplateMatching import ShapTemplateMatching
from core.流程树.node.node_node import Node
from lib.data import convert_JSON
from lib.file import save_as_file, make_new_folder, delete_file, clear_folder, delete_images_with_prefix
from lib.path import path_join,Globals, globalsdynamic
from lib.utils import addImageNew, get_new_model_name, parameter_list_to_str, list_de_weight
from core.MyClass import MyListWidget, STMThread, TextLabel
from func_timeout import func_set_timeout, FunctionTimedOut
import func_timeout


class ImageWidget(QWidget):

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.border_color, 2))
        painter.drawRect(self.rect())

class ImageListWidgetItem(QListWidgetItem):
    def __init__(self, name, img_path):
        super().__init__()
        print(name)
        self.img_path = img_path
        # 自定义item中的widget 用来显示自定义的内容
        self.widget = ImageWidget()
        self.nameLabel = TextLabel()
        self.nameLabel.setText(name)
        font = QFont("Arial", 8)  # 设置字体为Arial，大小为12
        self.nameLabel.setFont(font)
        self.nameLabel.setFixedSize(60, 10)
        # 用来显示avator(图像)
        self.avatorLabel = QLabel()
        # 设置图像源 和 图像大小
        # scale_size = QSize(40, 50)
        # self.avatorLabel.setPixmap(QPixmap(img_path).scaled(scale_size))
        addImageNew(self.avatorLabel, self.img_path, 60, 50)
        # 图像自适应窗口大小
        self.avatorLabel.setScaledContents(True)
        # 设置布局用来对nameLabel和avatorLabel进行布局
        self.hbox = QVBoxLayout()
        self.hbox.addWidget(self.avatorLabel)
        self.hbox.addWidget(self.nameLabel)
        self.hbox.addStretch(1)
        # 设置widget的布局
        self.widget.setLayout(self.hbox)
        # 设置自定义的QListWidgetItem的sizeHint，不然无法显示
        self.setSizeHint(self.widget.sizeHint())

    def set_border(self,color=Qt.red):
        self.widget.border_color=color
        self.widget.update()

    def set_image(self, image_path,border_color=Qt.red):
        """设置显示图像"""
        self.img_path = image_path
        self.widget.border_color = border_color
        # scale_size = QSize(40, 50)
        #
        addImageNew(self.avatorLabel, image_path, 60, 50)
        self.setSizeHint(self.widget.sizeHint())
    def set_text(self,name):
        """修改标签名"""
        self.nameLabel.setText(name)

    def text(self):
        return self.img_path

class ImageListWidget(MyListWidget):
    signal = pyqtSignal(list)
    signal_init = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # # 设置每个item size
        # self.setGridSize(QSize(220, 190))
        # 设置横向list
        self.setFlow(QListView.LeftToRight)
        # 设置换行
        self.setWrapping(True)
        # 窗口size 变化后重新计算列数
        self.setResizeMode(QListView.Adjust)
        # 设置选择模式
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.setIconSize(QSize(200, 150))


    def set_one_accpt(self,item):
        '''设置只有一个图片激活'''
        for i in self.get_listwidget_items():
            if i != item:
                i.isUse = False
                i.set_border(Qt.white)
            else:
                item.isUse = True
                item.set_border(Qt.red)
                self.setCurrentItem(item)

    def get_accptitem(self):
        '''获取激活选取'''
        for i in self.get_listwidget_items():
            if i.isUse:
                return i
        return None
    def del_accptitem(self):
        '''删除激活选项'''
        # 更新数据库
        currentRow = self.currentRow()

        # 删除图像
        delete_images_with_prefix(path_join(globalsdynamic.data_path, path_join('template',str(Globals.node_index))),str(Globals.node_index) + '_' + str(
            self.currentRow()))

        item = self.get_accptitem()
        self.takeItem(self.row(item)) #删除激活选项

        STMOperateDb.delete_module(currentRow)

        if self.count() <= 0:
            self.label.clear()
            self.label.setText('图像展示')
            # 新增空白模板
            self.signal_init.emit()
            return

        self.set_one_accpt(self.currentItem())
        path = self.currentItem().text()
        addImageNew(self.label, path, 374, 200)

    def del_allitems(self):
        '''清空选项'''
        # self.clear()
        super().del_allitems()
        STMOperateDb.delete_allmodule()
        # 清空图像文件夹
        clear_folder(path_join(globalsdynamic.data_path,  path_join('template',str(Globals.node_index)) ))
        # 新增空白模板
        self.signal_init.emit()


    def load_images(self, path=None,name=None):
        # 设置每个item size
        if not path:
            path = Globals.black_image_path
            # 检查文件是否存在，如果不存在则创建
            if not os.path.exists(path):
                # 创建一个50x50的全黑图片
                image = Image.new("RGB", (60, 50), (0, 0, 0))
                # 保存图片
                image.save(path)
        # 去重
        names = self.get_label_names()
        # if name in names:
        #     name = str(int(name)+len(names))
        if not name:
            name = str(len(names)+1)
        img_item = ImageListWidgetItem(name, path)
        # img_item.set_image(path)

        self.addItem(img_item)
        self.setItemWidget(img_item, img_item.widget)
        self.set_one_accpt(img_item)

        # # 刷新界面
        # QApplication.processEvents()
        # self.repaint()
        return path

    def get_label_names(self):
        """获取标签名称列表"""
        names = []
        for item in self.get_listwidget_items():
            names.append(item.nameLabel.text())
        return names
    def get_image_paths(self):
        """获取图像路径列表"""
        names = []
        for item in self.get_listwidget_items():
            names.append(item.text())
        return names

    def set_label_names(self,names):
        """设置标签名称"""
        items = self.get_listwidget_items()
        for i in range(len(items)):
            item = items[i]
            if i < len(names):
                item.nameLabel.setText(names[i])
        return names

class ShapTemplateMatchingWindow(utilsWindow):
    '''模板匹配界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision
        self.nodeIndex = str(Globals.node_index)
        # self.template_path = path_join(Globals.temporarily_path, 'tmp_path.' + globalsdynamic.temp_suffix)  # 当前模板的路径
        self.template_path = ''
        self.template_img_path = path_join(globalsdynamic.data_path, path_join('template',str(Globals.node_index)) )  # 保存的模板文件临时存储目录
        self.type_select = '矩形'
        self.type_mask = self.ChildVision.comboBox_9.currentText()
        self.signal = None
        self.output_list = [self.ChildVision.checkBox_25, self.ChildVision.checkBox_24, self.ChildVision.checkBox_17,
                            self.ChildVision.checkBox_21, self.ChildVision.checkBox_16, self.ChildVision.checkBox_15,
                            self.ChildVision.checkBox_34,self.ChildVision.checkBox_33,self.ChildVision.checkBox_13,
                            self.ChildVision.checkBox_19, self.ChildVision.checkBox_22,self.ChildVision.checkBox_26]
        self.mask = [None,None,None]
        self.isolated = True # 是否单独运行
        self.boxs = []

        self.signalSlotConnection()

    def setcss(self):

        self.setSpinbox(self.ChildVision.spinBox_2, 40, 10, 100, 1)  # 置信度
        self.setSpinbox(self.ChildVision.spinBox_7, 0, 0, 100, 1)  # 最大目标数
        self.setSpinbox(self.ChildVision.spinBox_3, 0, -360, 360, 1)  # 初始角度
        self.setSpinbox(self.ChildVision.spinBox_5, 360, -360, 360, 1)  # 结束角度
        self.setSpinbox(self.ChildVision.spinBox_8, 70, -100, 200, 1)  # 最小缩放
        self.setSpinbox(self.ChildVision.spinBox_13, 130, -100, 200, 1)  # 最大缩放
        self.setSpinbox(self.ChildVision.spinBox_4, 0, 0, 16, 1)  # 金字塔层数
        self.setSpinbox(self.ChildVision.spinBox_6, 'auto', 0, 180, 1)  # 角度步长
        self.setSpinbox(self.ChildVision.spinBox_9, 80, 0, 100, 1)  # 重叠系数
        self.setSpinbox(self.ChildVision.spinBox_10, 90, 0, 100, 1)  # 贪婪系数
        self.setSpinbox(self.ChildVision.spinBox_11, 50, 0, 100, 10)  # 圆相似度
        self.setSpinbox(self.ChildVision.spinBox_12, 100, 0, 200, 10)
        self.setSpinbox(self.ChildVision.spinBox_19, 200, 10, 500, 10)  # 迭代次数

        for output in self.output_list:
            output.setChecked(True)  # 默认勾选

        self.ChildVision.tabWidget_5.setCurrentIndex(0)
        self.changedComboBox11()

        self.ChildVision.pushButton_12.hide()

    def signalSlotConnection(self):
        self.signal = [self.ChildVision.pushButton_27,self.ChildVision.pushButton_29,self.ChildVision.pushButton_11,
                       self.ChildVision.pushButton_32,self.ChildVision.pushButton_26,self.ChildVision.toolButton_3,
                       self.ChildVision.pushButton_34,self.ChildVision.pushButton_35,self.ChildVision.pushButton_36,
                       self.ChildVision.pushButton_30,self.ChildVision.listWidget_3.itemClicked,self.ChildVision.listWidget_3.signal_init
                       ]
        super().signalSlotConnection()
        # if Globals.isSignalSlotConnection['模板匹配']:
        #     return
        self.ChildVision.comboBox_11.currentIndexChanged.connect(self.changedComboBox11)
        # 模板
        self.ChildVision.pushButton_27.clicked.connect(self.template_select) # 采集区域
        self.ChildVision.pushButton_29.clicked.connect(self.template_gather) # 采集模板
        self.ChildVision.pushButton_11.clicked.connect(self.template_learn) # 目标学习
        self.ChildVision.pushButton_32.clicked.connect(self.template_recognize) # 识别测试
        self.ChildVision.pushButton_26.clicked.connect(self.set_mask) # 搜索区域
        self.ChildVision.toolButton_3.clicked.connect(self.Open_Folder) # 采集模板 本地
        self.ChildVision.listWidget_3.context_menu(self.ChildVision.label_10) # 右键菜单
        self.ChildVision.pushButton_34.clicked.connect(lambda : self.template_add(None)) # 新增模板
        self.ChildVision.pushButton_35.clicked.connect(self.ChildVision.listWidget_3.del_accptitem) # 删除模板
        self.ChildVision.pushButton_36.clicked.connect(self.ChildVision.listWidget_3.del_allitems) # 清空模板
        self.ChildVision.listWidget_3.itemClicked.connect(self.set_save_img)
        self.ChildVision.listWidget_3.signal_init.connect(self.template_add)

        self.ChildVision.pushButton_30.clicked.connect(self.window_close)

        # Globals.isSignalSlotConnection['模板匹配'] = True

    @func_set_timeout(Globals.timeout)  # 设定函数超执行时间_
    def run(self,module_input,boxs):
        """流程树运行"""
         # 初始化参数
        self.boxs = []
        if module_input and module_input[-1] and ('temp_halcon.' in module_input[-1] or 'temp.' in module_input[-1]):
            img_path = module_input[-1]
            globalsdynamic.temp_path = img_path
        else:
            raise Exception("没有输入图像！")
            # return [globalsdynamic.temp_path]+self.get_result_ng()+[globalsdynamic.temp_path],[]
        # 读取数据库
        result = STMOperateDb.get_row()
        if result:
            if result[STMOperateDb.get_key_index('parameters')]:
                parameters = convert_JSON(result[STMOperateDb.get_key_index('parameters')])
                self.ChildVision.comboBox_8.setCurrentIndex(int(parameters[0]))
                self.ChildVision.spinBox_7.setValue(int(parameters[1]))
                self.ChildVision.spinBox_2.setValue(int(parameters[2]))
                self.ChildVision.spinBox_3.setValue(int(parameters[3]))
                self.ChildVision.spinBox_5.setValue(int(parameters[4]))
                self.ChildVision.spinBox_8.setValue(int(parameters[5]))
                self.ChildVision.spinBox_13.setValue(int(parameters[6]))
                self.ChildVision.spinBox_9.setValue(int(parameters[7]))
                self.ChildVision.spinBox_6.setValue(int(parameters[8]))
                self.ChildVision.spinBox_4.setValue(int(parameters[9]))
                self.ChildVision.spinBox_10.setValue(int(parameters[10]))
                self.ChildVision.comboBox_11.setCurrentIndex(int(parameters[11]))
                self.ChildVision.comboBox_30.setCurrentText(parameters[12])
                self.ChildVision.spinBox_15.setValue(int(parameters[13]))

        # 输出参数
        globalsdynamic.temp_halcon_path = globalsdynamic.temp_path  # 取消第二图像
        result = self.template_recognize()
        if result:
            result = [globalsdynamic.temp_path] + result + [globalsdynamic.temp_halcon_path]
        else:
            result = [globalsdynamic.temp_path] + self.get_result_ng()+ [globalsdynamic.temp_halcon_path]

        boxs = boxs + [box[1::-1] + box[3:1:-1] for box in self.results[0]]
        # boxs = boxs + self.boxs
        return result,boxs

    def changedComboBox11(self):
        text = self.ChildVision.comboBox_11.currentIndex()
        if text == 0:
            self.ChildVision.stackedWidget_10.setCurrentIndex(1)
        else:
            self.ChildVision.stackedWidget_10.setCurrentIndex(0)

    def set_spinBox15(self):
        modelNames = STMOperateDb.get_column('modelName')
        num = 0
        if modelNames:
            num = len(modelNames)
        if num <= 0:
            num = 0
        self.setSpinbox(self.ChildVision.spinBox_15, num, 1, num, 1)  # 迭代次数

    def set_comboBox30(self):
        self.ChildVision.comboBox_30.clear()
        modelNames = STMOperateDb.get_column('modelName')
        if not modelNames:
            return
        for modelName in modelNames:
            # self.ChildVision.comboBox_30.addItem(modelName.split('\\')[-1])
            self.ChildVision.comboBox_30.addItem(modelName)
    def updata_output_sockets(self):
        """更新输出节点"""
        output_checked_list = [ ]
        for output in self.output_list:
            if output.isChecked():
                output_checked_list.append(output.text())

        save_data = {}
        save_data['id'] = Globals.node_index
        save_data['title'] = '模板匹配'
        save_data['types'] = ['图像']+[output.split('，')[1] for output in output_checked_list]
        save_data['texts'] = ['输入图像']+[output.split('，')[0] for output in output_checked_list]
        save_data['icons'] = [1]+[0]*len(output_checked_list)

        tree = self.ChildVision.nodeEditWind
        new_node = Node(tree.scene, save_data['title'], save_data['types'], save_data['texts'],
                        save_data['icons'], isNew=False)

        # 更新流程树
        tree.scene.updataNode(Globals.node_index - 1, new_node)
        # 流程树数据库保存
        globalsdynamic.db_child.insert_data('Node', save_data, 'id')

    def set_mask(self):
        '''新建掩码'''
        self.type_mask = self.ChildVision.comboBox_9.currentText()
        self.ChildVision.View.addNewMask(id="SelectionBox",type=self.type_mask)

    def template_select(self):
        '''新建选取框'''
        self.template_result_noshow()
        self.type_select = self.ChildVision.comboBox_10.currentText()
        self.ChildVision.View.addNewSelection(id="SelectionBox",type=self.type_select)

    def template_add(self,path=None,name=None):
        '''增加模版'''
        self.ChildVision.listWidget_3.load_images(path,name)
        # QTimer.singleShot(10, lambda : self.ChildVision.listWidget_3.load_images(path))
    def template_show(self,path):
        '''显示模板'''
        addImageNew(self.ChildVision.label_10, path, 300, 200)
    def template_save(self,image):
        '''保存采集的模板'''
        get_accptitem = self.ChildVision.listWidget_3.get_accptitem()
        self.template_img_path = path_join(globalsdynamic.data_path,  path_join('template',str(Globals.node_index)))  # 保存的模板文件临时存储目录
        self.template_path = str(Globals.node_index)+'_'+str(self.ChildVision.listWidget_3.currentRow()) + '.' + globalsdynamic.temp_suffix
        self.template_path = path_join(self.template_img_path,self.template_path)
        if get_accptitem:
            make_new_folder(self.template_img_path) # 创建模板文件夹
            image.save(self.template_path) # 保存模板文件
            self.template_show(self.template_path)  # 显示模板文件
            # image.save(tmp_path)  # 模板文件另存在临时路径中

            get_accptitem.set_image(self.template_path)

            # # # 写入数据库
            # STMOperateDb.add_module(self.ChildVision.listWidget_3.currentRow(),self.template_path)
        else:
            QMessageBox.warning(self.MainWindow, "错误", "请先点击新增模板！")
            return

    def test_data(self):
        '''测试参数是否设置有误'''
        if self.ChildVision.spinBox_3.value() > self.ChildVision.spinBox_5.value():
            QMessageBox.warning(self.MainWindow, "错误", "请选择正确的角度范围！")
            return False
        if self.ChildVision.spinBox_8.value() > self.ChildVision.spinBox_13.value():
            QMessageBox.warning(self.MainWindow, "错误", "请选择正确的涨缩范围！")
            return False
        return True

    def template_gather(self):
        '''采集模板'''
        # self.template_result_noshow()

        # self.template_path = path_join(Globals.temporarily_path, 'tmp_path.' + globalsdynamic.temp_suffix)  # 临时模板的路径
        image = self.ChildVision.View.getSelectionImg(self.type_select)
        if image is None:
            QMessageBox.information(self.MainWindow, "提示", "请先创建采集区域！")
            return None
        self.template_save(image)

        # 数据库保存模板形状
        scale = self.ChildVision.View.getSelectionScale('圆环') if self.type_select == '圆环' else 1
        type_selects = STMOperateDb.get_column('type_selects')
        if not type_selects:
            type_selects = {}
        type_selects[self.ChildVision.listWidget_3.currentRow()] = [self.type_select,scale]
        data = {'type_selects':type_selects}
        STMOperateDb.add_data(data)

    def Open_Folder(self):
        '''采集模板 本地'''
        path,_ = QFileDialog.getOpenFileName(self.MainWindow, "选取文件", "./")
        if not _:
            return
        self.ChildVision.lineEdit_2.setText(path)

        self.template_save(QImage(path))

        # 数据库保存模板形状
        scale =  1
        type_selects = STMOperateDb.get_column('type_selects')
        if not type_selects:
            type_selects = {}
        type_selects[self.ChildVision.listWidget_3.currentRow()] = [self.type_select, scale]
        data = {'type_selects': type_selects}
        STMOperateDb.add_data(data)

    def set_save_img(self,item):
        '''切换保存的图像'''
        self.ChildVision.listWidget_3.set_one_accpt(item)
        tmp_path = item.text()
        if tmp_path != Globals.black_image_path:
            self.template_save(QImage(tmp_path))


    def template_init(self,tmp_path=None,img_path=None):
        if not img_path:
            img_path = globalsdynamic.temp_path
        self.shaptemplatematching = ShapTemplateMatching(
            imgpath=img_path,
            tmppath=tmp_path,
            # imgpath=Globalsjson.temp_path,
            min_score=float(self.ChildVision.spinBox_2.value()) / 100.0,
            num_matches=int(self.ChildVision.spinBox_7.value()),
            max_overlap=float(self.ChildVision.spinBox_9.value()) / 100.0,
            angle_start=int(self.ChildVision.spinBox_3.value()),
            angle_extent=int(self.ChildVision.spinBox_5.value()),
            scale_min=float(self.ChildVision.spinBox_8.value()) / 100.0,
            scale_max=float(self.ChildVision.spinBox_13.value()) / 100.0,
            num_levels=int(self.ChildVision.spinBox_4.value()),
            greediness=float(self.ChildVision.spinBox_10.value()) / 100.0,
            mask = self.mask
        )

    def template_learn(self):
        """目标学习"""
        try:
            model_names = {}

            if not self.test_data():
                return None
            if not self.ChildVision.listWidget_3.count():
                QMessageBox.warning(self.MainWindow, "错误", "请先点击新增模板！")
                return None

            self.ChildVision.pushButton_11.setEnabled(False)

            self.template_delete_model()  # 删除旧模型
            # 多模板训练
            result = STMOperateDb.get_row()
            names = self.ChildVision.listWidget_3.get_label_names()
            tmp_paths = self.ChildVision.listWidget_3.get_image_paths()
            if not result or not result[6] or not names or not tmp_paths:
                return
            type_selects = convert_JSON(result[6])
            for i in range(len(tmp_paths)):
                tmp_path = tmp_paths[i]
                name = names[i]
                type_select = type_selects[str(i)][0] if type_selects and str(i) in type_selects else '矩形'
                model_name = get_new_model_name()
                model_name = model_name.replace(".shm", f"_{i}.shm")
                # 训练很快不需要多线程
                # # 训练模型
                # self.worker_thread = STMThread(self, tmp_path, model_name, type_select)
                # self.worker_thread.progressTrain.connect(lambda: self.MainWindow.awaitWindow.update_progress(
                #     int(100 / len(self.ChildVision.listWidget_3.get_listwidget_items()))))
                # self.worker_thread.start()
                if tmp_path and os.path.exists(tmp_path) and not 'black_image.jpg' in tmp_path:
                    self.template_init(tmp_path)
                    self.shaptemplatematching.save_template(model_name, type_select[0], type_select[1])  # 保存新模型
                else:
                    continue
                # # 写入数据库
                model_names[name] = model_name
                # STMOperateDb.add_module(i, names[i],name='matching_paths',add=False)
            # 模型写入数据库
            data = {}
            data['modelName'] = model_names
            STMOperateDb.add_data(data)
            self.set_spinBox15()
            self.set_comboBox30()

            QMessageBox.warning(self.MainWindow, "提示", "目标学习完毕！")
        except Exception as e:
            QMessageBox.warning(self.MainWindow, "错误", f"目标学习失败:{e}！")
        finally:
            self.ChildVision.pushButton_11.setEnabled(True)

    def template_result_noshow(self):
        """模板匹配识别结果显示结束"""
        # # halcon
        # if self.ChildVision.View.temp_path and 'temp_halcon' in self.ChildVision.View.temp_path:
        #     self.ChildVision.View.displayImg(QImage(globalsdynamic.temp_path),globalsdynamic.temp_path)
        # view
        self.ChildVision.View.clear()

    def template_result_show(self,result,pos):
        '''显示模板匹配识别结果'''
        boxs, outlines = result
        rectangle = []
        # 显示识别结果
        modelName = STMOperateDb.get_column('modelName')
        if not modelName:
            raise
            return
        names = list(modelName)
        for i in range(len(boxs)):
            text = f'{names[int(self.Model[i])]}=中心点:{round(self.Column[i]), round(self.Row[i])}角度:{round(self.Angle[i],2)}'
            x1, y1, x2, y2 = self.ChildVision.View.turnNewShowBox(boxs[i],pos,i)
            # self.boxs.append([x1, y1, x2, y2])
            self.ChildVision.View.addNewShowBox(x1,y1,x2,y2,text)
            rectangle.append([x1, y1, x2, y2])
        return rectangle

    def template_recognize(self):
        '''识别测试'''
        try:
            if not self.test_data():
                return None

            self.model_names = {}
            # 获取掩码图片
            # 裁剪后的图片路径，在item中图像左上角为（0，0） ,  # 图像左上角为（0，0），在item中的大小，比例，掩码类别
            cropped_image, self.item_pos ,self.img_pos, size,scale, type= self.ChildVision.View.getMaskImg(self.type_mask)
            # cropped_image.save(globalsdynamic.img_halcon_path)  # 保存识别图片
            if size:
                self.mask = [self.img_pos, size*scale, type]
            else:
                self.mask = [None,None,None]

            # 图片另存为
            # save_as_file(globalsdynamic.temp_path, globalsdynamic.temp_halcon_path)  # 保存第二图像 识别图片

            # 读取数据库
            result = STMOperateDb.get_row()
            if not result:
                return

            self.ChildVision.pushButton_32.setEnabled(False)
            # self.ChildVision.View.clear()

            self.model_names = result[3]
            if not self.model_names and self.isolated:
                QMessageBox.warning(self.MainWindow, "错误", "请先点击目标学习！")
            self.model_names = list(self.model_names.values()) if self.model_names else []

            if self.isolated:
                self.template_result_noshow()
                # 单独运行
                # self.template_recognize_thread()
                self.template_recognize_run()
                self.template_result_show(self.results, self.img_pos) if result else []
            else:
                # 流程运行
                recognize_result = self.template_recognize_run()
                rectangle = self.template_result_show(self.results, self.img_pos) if result else []
                return recognize_result

        except Exception as e:
            print(e)
            raise  # 重新引发异常
        finally:
            self.ChildVision.pushButton_32.setEnabled(True)

    def template_recognize_run(self):
        """识别模板"""
        self.template_init(img_path=globalsdynamic.temp_halcon_path)
        self.results = [[], []]
        if self.model_names:
            if self.ChildVision.comboBox_11.currentIndex() == 0:  # 单模板匹配
                model_name = self.model_names[self.ChildVision.comboBox_30.currentIndex()]
                self.Row, self.Column, self.Angle, self.Scale, self.Score,self.Model = (
                    self.shaptemplatematching.matching_template(model_name))
                self.results = self.shaptemplatematching.get_result()

            else:  # 多模板匹配
                model_num = int(self.ChildVision.spinBox_15.text())
                if not model_num:
                    print('+++??????????????')
                self.Row, self.Column, self.Angle, self.Scale, self.Score, self.Model = (
                    self.shaptemplatematching.matching_templates(
                        self.model_names[:model_num]))
                self.results = self.shaptemplatematching.get_results()

            # self.shaptemplatematching.show_result()
            # self.ChildVision.View.displayImg(QImage(globalsdynamic.temp_halcon_path), globalsdynamic.temp_halcon_path)
            self.ChildVision.pushButton_32.setEnabled(True)

            # 输出参数
            self.Row = [round(output,2) for output in self.Row if isinstance(output,float)]
            self.Column = [round(output, 2) for output in self.Column if isinstance(output, float)]
            self.Angle = [round(output, 2) for output in self.Angle if isinstance(output, float)]
            self.Scale = [round(output, 2) for output in self.Scale if isinstance(output, float)]
            self.Score = [round(output, 2) for output in self.Score if isinstance(output, float)]
            result = []
            num = sum(1 for item in self.Model if item or item == 0)
            counter = Counter(self.Model)
            self.model,self.point,self.point_x,self.point_y,self.angle,self.score = '','','','','',''
            # self.Point = list(zip(self.Column, self.Row))
            self.modelNames = STMOperateDb.get_column('modelName')
            self.modelNames = list(self.modelNames)
            self.Name = [self.modelNames[i] for i in self.Model]

            if self.Column:
                # 参数格式调整
                for i in range(len(self.model_names)):
                    self.model = self.model + str(counter[i])
                    if i < len(self.model_names) - 1:
                        self.model = self.model + '|'
                self.point_x = parameter_list_to_str(self.Column)
                self.point_y = parameter_list_to_str(self.Row)
                self.angle = parameter_list_to_str(self.Angle)
                self.score = parameter_list_to_str(self.Score)
                self.name = parameter_list_to_str(self.Name)
                self.label_name = parameter_list_to_str(self.ChildVision.listWidget_3.get_label_names())
                for i in range(len(self.Column)):
                    self.point = self.point + str(self.Column[i]) + '|' + str(self.Row[i])
                    if i < len(self.Column) - 1:
                        self.point = self.point + '|'

                # 检出中心
                if self.output_list[0].isChecked():
                    result.append(self.point)
                # 检出中心X
                if self.output_list[1].isChecked():
                    # result.append(self.Column)
                    result.append(self.point_x)
                # 检出中心Y
                if self.output_list[2].isChecked():
                    # result.append(self.Row)
                    result.append(self.point_y)
                # 检出角度
                if self.output_list[3].isChecked():
                    # result.append(self.Angle)
                    result.append(self.angle)
                # 检出数量
                if self.output_list[4].isChecked():
                    # result.append(len(self.Model))
                    result.append(num)
                    # result.append(self.model)
                # 检出模板数
                if self.output_list[5].isChecked():
                    # result.append(len(self.Model))
                    result.append(self.model)
                # 检出模板名
                if self.output_list[6].isChecked():
                    # result.append(num)
                    result.append(self.name)
                # 识别模板名
                if self.output_list[7].isChecked():
                    if self.ChildVision.comboBox_11.currentIndex() == 0:
                        result.append(self.ChildVision.comboBox_30.currentText())
                    else:
                        names = self.modelNames[:self.ChildVision.spinBox_15.value()]
                        result.append(parameter_list_to_str(names))
                    # result.append(len(self.Model)-num)
                # 学习模板名
                if self.output_list[8].isChecked():
                    result.append(self.label_name)
                # 得分
                if self.output_list[9].isChecked():
                    # result.append(self.Score)
                    result.append(self.score)
                # 结果
                if self.output_list[10].isChecked():
                    result.append('OK')
            else:
                result = self.get_result_ng()
            return result

    def get_result_ng(self):
        """无识别结果"""
        output_list = self.output_list
        if self.output_list[9].isChecked():
            output_list = self.output_list[:-1]
        outputs = [output for output in output_list if output.isChecked()]
        isCheckeds = [1 if output.isChecked() else 0 for output in output_list]
        result = [''] * len(outputs)
        if self.output_list[8].isChecked():
            result[-1] = 'NG'
        if self.output_list[4].isChecked():
            result[4-isCheckeds[:4].count(0)] = 0
        if self.output_list[5].isChecked():
            result[5-isCheckeds[:5].count(0)] = 0

        # result = []
        # for output in self.output_list:
        #     if not output.isChecked():
        #         continue
        #     type = output.currentText().split('，')[-1]
        #     if type == '数值':
        #         result.append(0)
        #     elif type == '字符':
        #         result.append(0)
        return result

    def template_recognize_thread(self):
        # 识别 等待窗口
        self.MainWindow.awaitWindow.show_progress()
        self.worker_thread = STMThread(self)
        self.worker_thread.progressTrain.connect(lambda: self.MainWindow.awaitWindow.complete_progress('成功'))
        self.worker_thread.start()

    def template_delete_model(self):
        """删除模型"""
        folder_path = path_join(globalsdynamic.data_path, 'model/' + str(Globals.node_index))
        if os.path.exists(folder_path):
            clear_folder(folder_path)

    def save_template(self):
        """保存模板"""
        data = {}
        data['template_paths'] = self.ChildVision.listWidget_3.get_image_paths()
        data['template_names'] = self.ChildVision.listWidget_3.get_label_names()
        STMOperateDb.add_data(data)

    def save_mask(self):
        """保存掩码"""
        cropped_image, item_pos,pos, size, scale,type  = self.ChildVision.View.getMaskImg(self.ChildVision.comboBox_9.currentText())
        curViewSize = self.ChildVision.View.curViewSize
        playbackPos = self.ChildVision.View.playbackItem.pos()
        if size:
            data = {}
            data['name'] = globalsdynamic.child
            # mask 0：左上角点（item坐标系中图像左上角为(0,0)的点） 1：掩码大小 2：图像左上角点（item坐标系中填充图形左上角为(0,0)） 3：item窗口大小 4：掩码类型
            data['mask'] = [(item_pos.x(),item_pos.y()), (size.width() ,size.height()) ,(playbackPos.x(),playbackPos.y()), (curViewSize.width(),curViewSize.height()),type]
            globalsdynamic.db_main.insert_data('ImageCapture', data)
            # mask = {'mask': [(item_pos.x(),item_pos.y()), (size.width() ,size.height()) , scale,type]}
            # STMOperateDb.add_data(mask)

    def save_parameters(self):
        """保存参数"""
        parameters = {"parameters": [self.ChildVision.comboBox_8.currentIndex(),self.ChildVision.spinBox_7.value(),self.ChildVision.spinBox_2.value(),
                                     self.ChildVision.spinBox_3.value(),self.ChildVision.spinBox_5.value(),self.ChildVision.spinBox_8.value(),
                                     self.ChildVision.spinBox_13.value(),self.ChildVision.spinBox_9.value(),self.ChildVision.spinBox_6.value(),
                                     self.ChildVision.spinBox_4.value(),self.ChildVision.spinBox_10.value(),self.ChildVision.comboBox_11.currentIndex()
                                     ,self.ChildVision.comboBox_30.currentText(),self.ChildVision.spinBox_15.value(),self.template_path]}
        STMOperateDb.add_data(parameters)

    def save_output_sockets(self):
        """保存输入输出参数"""
        save_data = {"output": []}
        for output in self.output_list:
            save_data["output"].append(output.isChecked())
        result = STMOperateDb.get_row()
        if not result:
            return
        output = result[STMOperateDb.get_key_index('output')]
        # 输出参数改变，图元也改变
        if output and convert_JSON(output) != save_data["output"] or not convert_JSON(output) :
            STMOperateDb.add_data(save_data)
            self.updata_output_sockets()
    def window_close(self):
        self.save_template()
        self.save_mask()
        self.save_parameters()
        self.save_output_sockets()
        super().window_close()

