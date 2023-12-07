import logging
from PyQt5.QtCore import Qt, QTimer, QVariant, QSize, QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from core.init_window import init_Modbus, init_visionWindow
from core.utils_window import utilsWindow
from core.网络通讯.ModbusOperateDb import ModbusOperateDb
from core.网络通讯.ModbusWindow import ModbusWindow
from lib.camera import Camera
from lib.file import *
from lib.image import ImagePro, rotate_image
from lib.path import path_join, Globals, globalsdynamic
from lib.utils import  setCurrentIndex, addImageNew
from core.MyClass import CameraThread

# 相机类
camera = Camera()
# 图像类
image = ImagePro()

class ImageCaptureWindow(utilsWindow):
    '''图像采集界面'''
    def __init__(self,MainWindow):
        self.MainWindow = MainWindow
        self.ChildVision = MainWindow.ChildVision
        self.camera_list = [ ] # 相机列表 [名称 ip]
        self.data = {'name':globalsdynamic.child, 'temppath': ''}
        self.keys = ['name','temppath','parameters']
        self.filename = False # 模板文件原来路径
        self.timer = None
        self.isView = False # 是否预览中
        # self.tmp_path = path_join(Globals.temporarily_path, 'temp.'+Globalsjson.temp_suffix) # 临时样板图片存储路径
        self.local_img_path = path_join(Globals.temporarily_path, 'local')# 本地采集的样板图片临时存储目录
        self.camera_img_path = path_join(Globals.temporarily_path, 'camera')  # 摄像头采集的样板图片临时存储目录
        self.preprocessing_list = [
            '平均值滤波',
            '中间值滤波',
            '高斯滤波',
            '双边滤波',
            '图像锐化',
            '图像平滑',
            '边缘增强',
            '开/闭运算',
            '二值化',
        ]
        self.signalSlotConnection()

        clear_folder_if_exceeded_numbe(self.local_img_path)
        clear_folder_if_exceeded_numbe(self.camera_img_path)

        self.ChildVision.tabWidget_4.removeTab(2) # 删除图像滤波界面

    def setcss(self):
        self.camera_trigger()
        self.ChildVision.radioButton.setChecked(True)
        self.ChildVision.radioButton_2.setChecked(False)
        self.ChildVision.stackedWidget_3.setCurrentIndex(0)

    def signalSlotConnection(self):
        # 图像采集共用
        self.signal = [self.ChildVision.pushButton_3,self.ChildVision.pushButton_5,self.ChildVision.pushButton_28,self.ChildVision.pushButton_6,
                       self.ChildVision.toolButton_2,self.ChildVision.pushButton_45,self.ChildVision.pushButton_46,self.ChildVision.pushButton_44,self.ChildVision.pushButton_31,
                       self.ChildVision.radioButton.toggled,self.ChildVision.radioButton_2.toggled,self.ChildVision.listWidget_2.customContextMenuRequested,
                       self.ChildVision.listWidget_2.itemClicked,self.ChildVision.comboBox_3.activated,self.ChildVision.comboBox_7.currentIndexChanged,
                       self.ChildVision.comboBox_14.currentIndexChanged,self.ChildVision.comboBox.currentIndexChanged,
                       self.ChildVision.spinBox_21.returnPressed]
        super().signalSlotConnection()

        self.ChildVision.radioButton.toggled.connect(lambda checked: setCurrentIndex(self.ChildVision, 0))
        self.ChildVision.radioButton_2.toggled.connect(lambda checked: setCurrentIndex(self.ChildVision, 1))
        self.ChildVision.pushButton_3.clicked.connect(
            lambda: self.set_img_fluctuate(-1))
        self.ChildVision.pushButton_5.clicked.connect(
            lambda: self.set_img_fluctuate( 1))
        self.ChildVision.pushButton_28.clicked.connect(self.window_close)
        self.ChildVision.pushButton_6.clicked.connect(self.set_currentItem_template)

        self.ChildVision.listWidget_2.context_menu(self.ChildVision.label_2)
        self.ChildVision.listWidget_2.customContextMenuRequested.connect(self.ChildVision.listWidget_2.show_menu)

        # 本地图像采集
        self.ChildVision.toolButton_2.clicked.connect(self.Open_Folder)
        self.ChildVision.listWidget_2.itemClicked.connect(self.set_img)

        # 相机图像采集
        self.ChildVision.pushButton_45.clicked.connect(self.camera_join)
        self.ChildVision.pushButton_46.clicked.connect(self.camera_capture_image)
        self.ChildVision.pushButton_44.clicked.connect(self.camera_close)
        self.ChildVision.comboBox_3.activated.connect(self.camera_run)
        self.ChildVision.comboBox_7.currentIndexChanged.connect(self.camera_choice_name)
        self.ChildVision.comboBox_14.currentIndexChanged.connect(self.camera_trigger)
        # 图像滤波
        self.ChildVision.comboBox.currentIndexChanged.connect(self.InstructionSelection)

        self.ChildVision.pushButton_31.clicked.connect(self.set_modbus)

        self.ChildVision.toolButton_15.clicked.connect(self.view)

        # 信号
        # self.ChildVision.spinBox_21.returnPressed.connect(self.camera_get_images_time)

    def run(self, module_input=None):
        """流程树运行"""
        image_array = self.camera_get_image(True)
        return [globalsdynamic.temp_path],[]

    def view(self):
        if not camera.g_bExit:
            if not self.isView and not self.MainWindow.ChildVisionCode.isRun:
                # 清理识别框
                self.ChildVision.View.clearShowBox()
                # # 清理文本
                self.ChildVision.View.clearShowBoxText()
                self.set_run()
            else:
                self.set_stop()
        else:
            QMessageBox.information(self.MainWindow, "提示", f"相机未连接！")

    def set_run(self):
        """开始预览"""
        self.isView = True
        icon = QIcon()
        icon.addFile(u":/相机/icon/闭眼睛.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ChildVision.toolButton_15.setIcon(icon)
        self.ChildVision.action_2.setIcon(icon)
        self.ChildVision.toolButton_15.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.ChildVision.toolButton_15.setStyleSheet(
            "background-color: rgb(255,165,0);\n"f"border-radius: 10px; border:\n"" 3px groove gray;border-style: outset;")

        self.viewTime = QTimer()
        self.viewTime.timeout.connect(lambda: self.camera_get_image(True))
        self.viewTime.start(10)

    def set_stop(self):
        """停止预览"""
        try:
            self.viewTime.stop()
        except:
            pass
        icon = QIcon()
        icon.addFile(u":/相机/icon/预览.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ChildVision.toolButton_15.setIcon(icon)
        self.ChildVision.action_2.setIcon(icon)
        self.ChildVision.toolButton_15.setText(QCoreApplication.translate("MainWindow", u"\u9884\u89c8", None))
        self.ChildVision.toolButton_15.setStyleSheet(
            "background-color: rgb(58, 111, 50);\n"f"border-radius: 10px; border:\n"" 3px groove gray;border-style: outset;")
        self.isView = False

    def InstructionSelection(self):
        currentText = self.ChildVision.comboBox.currentText()
        if currentText in self.preprocessing_list:
            index = self.preprocessing_list.index(currentText)
            # self.ChildVision.stackedWidget_14.setCurrentIndex(index)
            self.ChildVision.stackedWidget_14.show()

    def ifFun(self,value_1):
        """条件判断"""
        symbol = self.ChildVision.comboBox_37.currentText()
        value_2 = self.ChildVision.comboBox_42.currentText()
        if symbol != '=' and not value_2.isdigit():
            QMessageBox.information(self.MainWindow, "错误", f"非数值无法做为等式以为的比较值！")
            return
        if symbol == '=':
            return 'OK' if value_1 == value_2 else 'NG'
        elif symbol == '>':
            return 'OK' if value_1 > value_2 else 'NG'
        elif symbol == '<':
            return 'OK' if value_1 < value_2 else 'NG'
        elif symbol == '>=':
            return 'OK' if value_1 >= value_2 else 'NG'
        elif symbol == '<=':
            return 'OK' if value_1 <= value_2 else 'NG'

    def set_show_window(self):
        """切换显示的窗口"""
        self.ChildVision.radioButton.setChecked(True)  # 设置为选中状态
        self.ChildVision.radioButton_2.setChecked(False)  # 设置为未选中状态
        self.ChildVision.stackedWidget_3.setCurrentIndex(0)

    def get_listWidget(self):
        # listWidgets = [self.ChildVision.listWidget_2, self.ChildVision.listWidget]
        # labels = [self.ChildVision.label_2, self.ChildVision.label_6]
        type = self.ChildVision.stackedWidget_3.currentIndex()
        listWidgets = [self.ChildVision.listWidget_2]
        labels = [self.ChildVision.label_2]
        type = 0
        return listWidgets[type],labels[type],type

    def Open_Folder(self):
        '''采集图像 本地'''
        listWidget = self.ChildVision.listWidget_2
        path,_ = QFileDialog.getOpenFileName(self.MainWindow, "选取文件", "./")
        if _:
            img_list = self.ChildVision.listWidget_2.get_listwidget_item_names()
            if not _:
                return
            self.ChildVision.lineEdit.setText(path)
            addImageNew(self.ChildVision.label_2, path, 374, 200)
            if path not in img_list:
                # 添加某选项
                listWidget.addItem(path)
            else:
                QMessageBox.information(self.MainWindow, "提示", "已经有同名的样板了！")
            listWidget.set_currentItem_matching_text(path)

            # 保存本地采集的图像
            save_as_file(path, path_join(self.local_img_path, path.split('/')[-1]))


    def set_img(self,item):
        '''切换图像'''
        listWidget,label,type = self.get_listWidget()
        path = path_join(self.local_img_path,item.text().split('/')[-1])
        addImageNew(label, path, 374, 200)
        # 设置为选中项
        listWidget.setCurrentItem(item)
        if type == 0:
            self.ChildVision.lineEdit.setText(path)

    def set_img_fluctuate(self,num):
        '''上下切换图像'''
        listwidget,_,_ = self.get_listWidget()
        index = listwidget.currentRow() + num
        if index < 0 or index >= listwidget.count():
            return
        self.set_img(listwidget.item(index))

    def camera_trigger(self):
        """相机触发方式改变"""
        nConnectionNum = self.ChildVision.comboBox_14.currentIndex()
        if nConnectionNum == 0: # 手动触发
            self.ChildVision.stackedWidget_8.hide()
            if not camera.g_bExit:
                self.close_get_images()
                # camera.set_Value(param_type="float_value", node_name="TriggerMode",node_value=))
        elif nConnectionNum == 1: # 定时触发
            self.ChildVision.stackedWidget_8.setCurrentIndex(1)
            self.ChildVision.stackedWidget_8.show()
            # if not camera.g_bExit:
            #     self.camera_get_images_time()
        elif nConnectionNum == 2: # 外部触发
            self.ChildVision.stackedWidget_8.setCurrentIndex(0)
            self.ChildVision.stackedWidget_8.show()

    def set_modbus(self):
        # self.ChildVision.ChildModbus = ModbusWindow(self.MainWindow)
        # ModbusOperateDb.insert_data()
        # init_Modbus(self.ChildVision.ChildModbus)
        self.ChildVision.comboBox_33.setItemData(1, QVariant(0), Qt.UserRole-1) # 禁用写
        self.ChildVision.stackedWidget.setCurrentIndex(5)
    def close_modbus(self):
        self.ChildVision.comboBox_33.setItemData(1, QVariant(1 | 32), Qt.UserRole - 1) # 启用

    def camera_choice_name(self):
        '''相机名称随相机ip变化'''
        nConnectionNum = self.ChildVision.comboBox_7.currentIndex()
        self.ChildVision.comboBox_18.setCurrentIndex(nConnectionNum)
    def camera_choice_ip(self):
        '''相机ip随相机名称变化'''
        nConnectionNum = self.ChildVision.comboBox_18.currentIndex()
        self.ChildVision.comboBox_7.setCurrentIndex(nConnectionNum)

    def camera_run(self):
        '''选择相机品牌后显示相机列表'''
        if int(self.ChildVision.comboBox_3.currentIndex()) == 1:
            # 1.选择相机
            self.camera_list = camera.camera_init()
            if self.camera_list:
                self.ChildVision.comboBox_18.clear()
                self.ChildVision.comboBox_7.clear()
                for name, ip in self.camera_list:
                    self.ChildVision.comboBox_18.addItem(name)
                    self.ChildVision.comboBox_7.addItem(ip)
            else:
                QMessageBox.information(self.MainWindow, "提示", "找不到相机！.")
                return

    def get_parameters(self):
        """获取相机属性"""
        parameters = {}
        parameters['frequency'] = self.ChildVision.

    def camera_join(self):
        '''连接相机'''
        nConnectionNum = self.ChildVision.comboBox_7.currentIndex()
        if nConnectionNum < 0:
            QMessageBox.warning(self.MainWindow, "错误", "请选择相机ip.")
            return
        self.MainWindow.setCursor(Qt.WaitCursor) # 鼠标改为等待样式
        camera.nConnectionNum = int(self.ChildVision.comboBox_7.currentIndex())
        # 4.启动设备和相机
        if camera.g_bExit:
            # 防闪退
            self.camera_thread = CameraThread(camera,self.get_parameters())
            self.camera_thread.progressRun.connect(self.camera_join_result)
            self.camera_thread.start()
        else:
            self.MainWindow.setCursor(Qt.ArrowCursor)  # 鼠标改为默认样式
            QMessageBox.information(self.MainWindow, "提示", "相机已连接.")
    def camera_join_result(self,e):
        """根据相机初始化结果做不同事件"""
        if e:
            self.ChildVision.label_42.open_light()  # 信号灯亮
            self.MainWindow.setCursor(Qt.ArrowCursor)  # 鼠标改为默认样式
            QMessageBox.information(self.MainWindow, "提示", "相机连接成功.")
        else:
            logging.error(f"【相机连接失败：{e}】")
            self.MainWindow.setCursor(Qt.ArrowCursor)  # 鼠标改为默认样式
            QMessageBox.warning(self.MainWindow, "错误", "相机连接失败.")

    def camera_get_image(self,isSaveTemp=False):
        """图像获取"""
        try:
            if not camera.g_bExit:
                #获取下一帧的图像
                image_array = camera.get_image()
                image_array = rotate_image(image_array, self.ChildVision.comboBox_17.currentIndex())
                if isSaveTemp:
                    if not globalsdynamic.temp_path:
                        globalsdynamic.temp_path = path_join(globalsdynamic.data_path, 'temp.jpg')
                        # globalsdynamic.temp_suffix = 'jpg'  # 样板图像的后缀
                    image.saveimg_tofile(globalsdynamic.temp_path, image_array) # 保存运行时图像 自动

                    # self.ChildVision.View.showImgpath(globalsdynamic.temp_path)
                    self.filename = globalsdynamic.temp_path
                    self.set_template()
                return image_array
        except Exception as e:
            self.close_get_images()
            # logging.error(f"【图像获取失败：{e}】")
            QMessageBox.warning(self.MainWindow, "错误", f"图像获取失败:{e}")

    def camera_get_images_time(self):
        """连续获取图像 相机"""
        if not camera.g_bExit:
            self.close_get_images()
            time = self.ChildVision.spinBox_21.text()
            if not time:
                return
            time = int(time)
            self.timer = QTimer()
            self.timer.timeout.connect(self.camera_get_image)
            self.timer.start(time)  # 每隔time秒触发一次定时器

    def camera_get_images_io(self):
        """外部触发获取图像 相机"""
        if not camera.g_bExit:
            self.camera_get_image()

    def close_get_images(self):
        """停止定时"""
        if self.timer:
            self.timer.stop()

    def camera_capture_image(self):
        '''采集图像 相机'''
        try:
            if not camera.g_bExit:
                self.ChildVision.View.clear()
                image_array = self.camera_get_image()
                # flipped_image = image.image_process(image_array)
                # 临时图像保存
                image_path = image.saveimg_tofolder(self.camera_img_path, image_array)
                # self.ChildVision.View.showImgpath(image_path) # 展示图像
                self.ChildVision.listWidget_2.addItem(image_path) # 采集的图像添加在展示列表中
                self.ChildVision.listWidget_2.set_currentItem_matching_text(image_path)

                # 设为模板
                self.set_currentItem_template()

            else:
                QMessageBox.information(self.MainWindow, "提示", "相机未连接.")
        except Exception as e:
            self.close_get_images()
            logging.error(f"【图像获取失败：{e}】")
            QMessageBox.warning(self.MainWindow, "错误", f"图像获取失败:{e}")

    def camera_close(self):
        '''断开连接'''
        try:
            if camera.g_bExit:
                # QMessageBox.warning(self.MainWindow, "提示", "相机未连接.")
                return
            else:
                camera.close()
                self.close_get_images()
        except Exception as e:
            logging.error(f"【相机断开连接失败：{e}】")
            QMessageBox.warning(self.MainWindow, "错误", f"相机断开连接失败：{e}")
        else:
            self.ChildVision.label_42.close_light()  # 信号灯暗
            QMessageBox.information(self.MainWindow, "提示", "相机断开连接成功.")

    def set_currentItem_template(self):
        '''将展示的图像设置为模板'''
        listWidget,_,_ = self.get_listWidget()
        currentItem = listWidget.currentItem()
        if not currentItem:
            QMessageBox.warning(self.MainWindow, "错误", "请先选择一张图片.")
            return
        self.filename = currentItem.text()
        self.set_template()

    def set_template(self):
        '''将图像设置为模板'''
        globalsdynamic.temp_suffix = self.filename.split('.')[-1]  # 更新全局变量 模板文件后缀
        if not os.path.exists(self.filename):
            QMessageBox.warning(self.MainWindow, "错误", "请先采集一张图片.")
            return
        addImageNew(self.ChildVision.parentlabel, self.filename)  # 参数窗口显示模板图片
        self.ChildVision.View.showImgpath(self.filename)  # 显示模板图片
        self.save_data()  #

    def get_parameters(self):
        return [self.ChildVision.comboBox_3.currentText(),self.ChildVision.comboBox_7.currentText(),self.ChildVision.comboBox_18.currentText(),
                self.ChildVision.comboBox_14.currentText(),self.ChildVision.comboBox_34.currentText(),self.ChildVision.comboBox_42.currentText(),
                self.ChildVision.comboBox_44.currentText(),self.ChildVision.spinBox_21.value(),self.ChildVision.comboBox_17.currentText()]

    def save_data(self):
        '''保存数据'''
        self.data['temppath'] = path_join(globalsdynamic.data_path, 'temp.' + globalsdynamic.temp_suffix)  # 更新样板图片路径
        if 'temp.' not in self.data['temppath']:
            del self.data['temppath']
        self.data['name'] = globalsdynamic.child
        self.data['parameters'] = self.get_parameters()

        # 数据库写入
        globalsdynamic.db_main.insert_data('ImageCapture', self.data)
        globalsdynamic.db_child.update_data_if("Node","parameters",[globalsdynamic.temp_path],f'id = "1"')

        globalsdynamic.update_main_path()  # 全局变量更新
        save_as_file(self.filename, globalsdynamic.temp_path)

    def window_close(self):
        self.save_data()
        # init_visionWindow(self.ChildVision)
        super().window_close()








