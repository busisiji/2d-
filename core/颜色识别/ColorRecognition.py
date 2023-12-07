# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from ctypes import cdll

from lib.path import get_project_root, path_join, Globals, getPath, globalsdynamic

thispath = os.path.dirname(os.path.abspath(__file__))
dllpaths = [getPath('core/hAcqDirectFile.dll'),getPath('core/halcon.dll'),getPath('core/halconc.dll'),getPath('core/halconcpp.dll'),getPath('core/hcanvas.dll'),getPath('core/hdevenginecpp.dll')]
for dllpath in dllpaths:
    path = path_join(thispath,dllpath)
    cdll.LoadLibrary(path)

import halcon

class ColorRecognition:
    def __init__(self,
                 color = ['yellow', 'pink', 'blue', 'orange'],
                 Modelpath = globalsdynamic.mlpmodle_path, # 多层感知机网络存储路径
                 Classes=halcon.gen_empty_obj() # 创建一个空区域对象，用于保存训练样本
                 ):
        self.color = color
        self.Modelpath = Modelpath
        self.Classes = Classes

    def addclass_circle(self,Row, Column, r):
        """训练样板加入圆形"""
        Image = halcon.read_image(globalsdynamic.temp_path) # 必须加，不加面积为0
        # 行列相反
        # Rectangle = halcon.gen_circle(Row, Column, r)
        Rectangle = halcon.gen_circle(Column,Row, r)
        self.Classes = halcon.concat_obj(self.Classes, Rectangle)
        if not halcon.area_center(Rectangle)[0]:
            return False
        return True
    def addclass_rectangle(self,Row1, Column1, Row2, Column2):
        """训练样板加入矩形"""
        if Row1 <= Row2 and Column1 <= Column2 and Row2 - Row1 > 0 and Column2 - Column1 > 0:
            pass
        else:
            print("不满足生成矩形的条件")
            return
        Image = halcon.read_image(globalsdynamic.temp_path)  # 必须加，不加面积为0
        # 行列相反
        # Rectangle = halcon.gen_rectangle1(round(Row1,2), round(Column1,2), round(Row2,2), round(Column2,2))
        Rectangle = halcon.gen_rectangle1(round(Column1,2), round(Row1,2), round(Column2,2), round(Row2,2))
        if not halcon.area_center(Rectangle)[0][0]:
            return False
        self.Classes = halcon.concat_obj(self.Classes, Rectangle)
        return True

    def addclass_draw(self,imgpath = '../../images/color/Sample.Sec0.jpg'):
        """采集样本"""
        Image = halcon.read_image(imgpath)
        Width, Height = halcon.get_image_size(Image)
        WindowHandle = halcon.open_window(0, 0, Width, Height, father_window=0, mode='visible', machine='')
        halcon.disp_obj(Image,WindowHandle)
        halcon.set_draw(WindowHandle,'margin')
        halcon.set_color(WindowHandle,'black')

        # 1 生成训练样本（指定颜色类别）
        for i in range(1,len(self.color)+1):
            halcon.disp_obj(Image, WindowHandle)
            halcon.disp_obj(self.Classes, WindowHandle)
            halcon.disp_text(WindowHandle, ['在' + self.color[i - 1] + '区域画一个矩形', '点击鼠标右键确认'],
                             'window', 24, 12, 'black', [], [])
            # 画矩形
            Row1, Column1, Row2, Column2 = halcon.draw_rectangle1(WindowHandle)
            self.addclass_rectangle(Row1, Column1, Row2, Column2)
            # # 画圆
            # Row,Column,r = halcon.draw_circle(WindowHandle)
            # self.addclass_circle(Row, Column, r)
        return Image

    def train(self,imgpath,max_iterations=200,WeightTolerance=1,ErrorTolerance=0.01):
        """
        MLP模型训练

        :param imgpath: 图像路径
        :param max_iterations: 迭代次数
        :param:WeightTolerance 权重容差
        :param:ErrorTolerance 误差容差
        """

        # *创建 / 添加样本 / 训练分类器
        try:
            Image = halcon.read_image(imgpath)
            # 1 创建并设置多层感知机网络参数
            MLPHandle = halcon.create_class_mlp(3, 10, len(halcon.area_center(self.Classes)[0]), 'softmax', 'normalization', 10, 42)
            # 2 把训练样本添加到网络中
            halcon.add_samples_image_class_mlp(Image, self.Classes,MLPHandle)
            # 3 训练多层感知机网络
            # Error, ErrorLog = halcon.train_class_mlp(MLPHandle, max_iterations, 1, 0.01)
            Error, ErrorLog = halcon.train_class_mlp(MLPHandle, int(max_iterations), WeightTolerance, ErrorTolerance)
            # 4 保存多层感知机网络
            halcon.write_class_mlp(MLPHandle, self.Modelpath)
            # classify(self.Modelpath,WindowHandle,color)
            # 5 清除MLP分类器，清楚内存
            halcon.clear_class_mlp(MLPHandle)
            print('训练完成')
            return None
        except Exception as e:
            return e

    def classify(self,imgpath = '../../images/color/Sample.Sec1.jpg'):
        """颜色分类"""
        ImageTest = halcon.read_image(imgpath)
        if not os.path.exists(self.Modelpath):
            return None

        # 1 读取多层感知机网络
        MLPHandle = halcon.read_class_mlp(self.Modelpath)
        # halcon.disp_obj(ImageTest,WindowHandle)
        # 2 创建分类器
        ClassRegions = halcon.classify_image_class_mlp(ImageTest, MLPHandle, 0.5)
        if not ClassRegions:
            return None
        # 3 识别面积最大的为最有可能的类别
        area_center = halcon.area_center(ClassRegions)
        area_max_index = area_center[0].index(max(area_center[0]))
        result = self.color[area_max_index]
        center = area_center[1][area_max_index],area_center[2][area_max_index]
        return result,center

    def read_image(self,imgpath):
        return halcon.read_image(imgpath)

    def classifys(self,imgs):
        MLPHandle = halcon.read_class_mlp(self.Modelpath)
        ClassRegions = halcon.classify_image_class_mlp(imgs, MLPHandle, 0.5)
        return ClassRegions

    def recognize(self,imgpath = '../../images/color/Sample.Sec1.jpg'):
        """颜色识别"""
        MLPHandle = halcon.read_class_mlp(self.Modelpath)
        ImageTest = halcon.read_image(imgpath)
        ClassRegions = halcon.classify_image_class_mlp(ImageTest, MLPHandle, 0.5)
        scale_min = 0.7
        scale_max = 1.3
        result = []
        # halcon.set_color(WindowHandle,'white')
        for feature in range(1,5):
            ObjectsSelected = halcon.copy_obj(ClassRegions, feature, 1)
            ConnectedRegions = halcon.connection(ObjectsSelected)
            # SelectedRegions = halcon.select_shape(ConnectedRegions, 'area', 'and', halcon.area_center(Classes)[0][feature-1]*scale_min, halcon.area_center(Classes)[0][feature-1]*scale_max)
            SelectedRegions = halcon.select_shape(ConnectedRegions, 'area', 'and',1490.83, 5000)
            Number = halcon.count_obj(SelectedRegions)
            # halcon.disp_text(WindowHandle, ['the number of ' + color[feature - 1] + ':' + str(Number)], 'window', 50 + feature * 50, 50,
            #              'black', [],[])
        # halcon.wait_seconds(30)
            print(self.color[feature - 1] + ':' + str(Number))
            result.append(self.color[feature - 1] + ':' + str(Number))
        halcon.clear_class_mlp(MLPHandle)
        return result

def get_scale(img_path):
    img = halcon.read_image(img_path)
    imgWidth, imgHeight = halcon.get_image_size(img)
    # 数据库读取
    result = globalsdynamic.db_child.query_data_table('View')
    result = result[0] if result else result
    Width, Height = float(result[1]), float(result[2])
    scaleW = Width / imgWidth[0]
    scaleH = Width / imgHeight[0]
    return img,scaleW,scaleH

def add_text(text_boxs,img,windowWidth,windowHeight):
    '''图像绘制文本'''
    WindowHandle = halcon.open_window(0,0,windowWidth,windowHeight, father_window=0, mode='buffer', machine='') # visible 可见 buffer 不可见
    for text, Row, Column, Width, Height in text_boxs:
        halcon.disp_obj(img, WindowHandle) # 图像
        halcon.set_font(WindowHandle, f'Arial-Normal-{int(Width/8)}')
        halcon.disp_text(WindowHandle, text, 'window', Row, Column, 'orange red', ['box','shadow'],['false','false'])
        img = halcon.dump_window_image(WindowHandle) #图像名，窗口句柄
    halcon.write_image(img, globalsdynamic.temp_halcon_path.split('.')[1], 0, globalsdynamic.temp_halcon_path.split('.')[0])
        # ha.wait_seconds

    halcon.clear_window(WindowHandle)
    halcon.close_window(WindowHandle)

if __name__ == '__main__':
    color = ['yellow', 'pink', 'blue', 'orange']
    # classify()
    colorRecognition = ColorRecognition(color)
    colorRecognition.addclass_draw()