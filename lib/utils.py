import os
import time

from PIL import Image, ImageQt
from PyQt5.QtGui import QImage, QPixmap, QImageReader
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QMenu, QGridLayout, QSpacerItem, QSizePolicy, QAction
from PyQt5.QtCore import Qt, QSize, QBuffer, QByteArray, QPoint

from lib.file import make_new_folder
from lib.image import imageToPixmap
from lib.path import Globals, path_join, globalsdynamic


# 列表去重
def removal_list(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return  unique_list

def setLabelCentral(label,parentWidth=False,parentHeight=False,scale=1.5):
    '''设置控件在父窗口中居中且按父窗口大小比例缩放控件大小'''
    if not parentWidth:
        parentWidth = label.parentWidget().width()
    if not parentHeight:
        parentHeight = label.parentWidget().height()
    if parentWidth >= parentHeight * scale:
        expectedWidth = int(parentHeight * scale)
        expectedHeight = parentHeight
        # self.switch_layout(self.ChildrenReom.label_central, self.ChildrenReom.widget_2, 'H')
        label.setGeometry(int((parentWidth - expectedWidth) / 2), 0,expectedWidth, expectedHeight)
    else:
        expectedWidth = parentWidth
        expectedHeight = int(parentWidth / scale)
        # self.switch_layout(self.ChildrenReom.label_central, self.ChildrenReom.widget_2, 'V')
        label.setGeometry(0, int((parentHeight - expectedHeight) / 2),expectedWidth, expectedHeight)
    # print('labelwidth,labelheight',label.width(),label.height())

def switch_layout(control,widget,new_layout):
    '''
    :param control: 窗口中的控件
    :param widget: 窗口
    :param new_layout: 新的布局 V或者H
    :return: 修改布局
    '''
    # 创建一个垂直布局
    if new_layout == 'V':
        vertical_layout  = QVBoxLayout(widget)
    elif new_layout == 'H':
        vertical_layout  = QHBoxLayout(widget)

    # 将标签和按钮添加到垂直布局中
    vertical_layout .addWidget(control)

    # 设置主窗口的布局为新布局
    widget.setLayout(vertical_layout)


def KeepAspectScale(frameWidth, frameHeight, windowWidth, windowHeight):
    '''
    保持宽高比的情况下，将图片尺寸缩放到窗口中

    :param frameWidth: 图片宽度
    :param frameHeight: 图片高度
    :param windowWidth: 窗口宽度
    :param windowHeight: 窗口高度
    :return: 缩放后的图片尺寸，缩放依据（宽或高），缩放比例
    '''
    PlaybackSize = [0, 0]
    scaleBy = "width"

    if frameWidth / frameHeight >= windowWidth / windowHeight:
        # 按宽度缩放
        PlaybackSize[0] = float(windowWidth)
        PlaybackSize[1] = frameHeight * windowWidth / frameWidth
    else:
        # 按高度缩放
        scaleBy = "height"
        PlaybackSize[1] = float(windowHeight)
        PlaybackSize[0] = frameWidth * windowHeight / frameHeight

    return PlaybackSize, scaleBy

def resizeGL(window):
    '''设置图像显示窗口内控件大小位置'''
    window.comboBox_type = int(window.comboBox.currentIndex())
    for i in range(len(window.class_page_widget[window.comboBox_type])):
        setLabelCentral(window.label_central_class[window.comboBox_type][i])

        window.class_page_label[window.comboBox_type][i].move(10, 10)
        window.class_page_btns1[window.comboBox_type][i].move(
            window.class_page_widget[window.comboBox_type][i].width() - 90, 0)
        window.class_page_btns3[window.comboBox_type][i].move(
            window.class_page_widget[window.comboBox_type][i].width() - 90 + window.class_page_btns1[window.comboBox_type][
                i].width(), 0)

def setCurrentIndex(ChildVision, index):
    '''切换窗口重置控件大小位置'''
    ChildVision.stackedWidget_3.setCurrentIndex(index)
    # resizeGL(ChildVision, 'child_window2')


def addImageBetween(label,img_path):
    '''标签中间放置图片'''
    # if w and h:
    #     label.setFixedSize(w,h)
    # reader = QImageReader(img_path)
    # image = QImage(img_path)
    # print(image.width(),image.height(),label.width(),label.height())
    # scaledSize, scaleBy = KeepAspectScale(image.width(),image.height(),label.width(),label.height())
    # reader.setScaledSize(QSize(scaledSize[0], scaledSize[1]))
    # image = reader.read()
    # pixmap = QPixmap.fromImage(image)
    # label.setPixmap(pixmap)
    # label.setScaledContents(True)  # 允许标签缩放以适应窗口大小
    image = QPixmap(img_path)
    # scaledSize, scaleBy = KeepAspectScale(image.width(), image.height(), label.parentWidget().width(), label.parentWidget().width())
    # label.setPixmap(image.scaled(QSize(scaledSize[0],scaledSize[1]))) # 设置图片尺寸
    label.setPixmap(image)
    label.setScaledContents(True)  # 允许标签缩放以适应窗口大小

    label.setGeometry((label.parentWidget().width() - label.width()) // 2, (label.parentWidget().height() - label.height()) // 2, label.width(), label.height()) # 水平居中

    setLabelCentral(label)

def addImageNew(label, img_path, w=False, h=False):
    '''将图像添加到一个标签中 填充黑色保持尺寸一致'''
    if w and h:
        label.setFixedSize(w,h)
    if not os.path.exists(img_path):
        print("图片路径不存在:",img_path)
        return
    image = Image.open(img_path)
    scaledSize, scaleBy = KeepAspectScale(image.width, image.height, label.width(),
                                          label.height())

    image = image.resize((int(scaledSize[0]), int(scaledSize[1])))
    # 创建一个新的图片，尺寸与Label组件一致，并填充黑色
    new_image = Image.new("RGB", (label.width(), label.height()), "black")
    new_image.convert()
    # 将原始图片粘贴到新图片中心位置
    x_offset = int((label.width() - image.width) / 2)
    y_offset = int((label.height() - image.height) / 2)
    new_image.paste(image, (x_offset, y_offset))

    pixmap = imageToPixmap(new_image)
    label.setPixmap(pixmap)
    return [x_offset,x_offset+image.width],[y_offset,y_offset+image.height]


def QpixmaptoQImageReader(qimage):
    """Qpixmap转QImageReader类型"""
    # 将QImage数据存储到内存缓冲区中
    buffer = QBuffer()
    buffer.open(QBuffer.ReadWrite)
    qimage.save(buffer, "BMP")  # 这里可以指定您想要的图像格式，如PNG、JPEG等
    buffer.seek(0)

    # 从内存缓冲区中创建QByteArray对象
    image_data = QByteArray(buffer.data())

    # 创建QImageReader对象并从QByteArray中读取图像数据
    image_reader = QImageReader()
    image_reader.setDevice(image_data)
    return image_reader

def isSignalConnected( obj, name= 'clicked()'):
    """判断信号是否连接
    :param obj:        对象
    :param name:       信号名，如 clicked()
    """
    index = obj.metaObject().indexOfMethod(name)
    if index > -1:
        method = obj.metaObject().method(index)
        if method:
            return obj.isSignalConnected(method)
    return False

def get_new_model_name():
    """获取模型名"""
    folder_path = path_join(globalsdynamic.data_path,'model/'+str(Globals.node_index))
    make_new_folder(folder_path)
    model_name = path_join(folder_path, 'ShapeModel_dot' + str(
        time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())) + '.shm')  # 颜色识别模型存储路径

    return model_name

def parameter_list_to_str(parameter):
    """列表参数转字符串'x|x'参数"""
    try:
        parameter = [str(p) for p in parameter]
        result = '|'.join(parameter)
        return result
    except:
        return ''
def parameter_str_to_list(parameter,isNum=False):
    """字符串'x|x'参数转列表参数"""
    try:
        result = parameter.split('|')
        if isNum:
            result = [float(x) for x in result]
        return result
    except:
        return []

def list_de_weight(original_list):
    """遍历列表 查找所有重名元素修改为不同名元素"""
    # 创建一个空字典用于存储元素出现的次数
    element_count = {}

    # 遍历列表，将重名元素修改为不同名元素
    new_list = []
    for element in original_list:
        if element in element_count:
            element_count[element] += 1
            new_element = element + str(element_count[element])
            new_list.append(new_element)
        else:
            element_count[element] = 0
            new_list.append(element)

    return new_list

def ch_to_str(name):
    """将中文变量名转换为_开头的数字变量名"""
    try:
        b = name.encode('utf-8') + b'\x01'
        return 'var' + str(int.from_bytes(b, 'little'))
    except Exception as e:
        return 'var' + str(int(time.time()*pow(10,6)))