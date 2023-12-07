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

class PyHalcon(halcon):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    """""""""""""""""""""""""""""""""""""""""
                    *窗口显示*
    """""""""""""""""""""""""""""""""""""""""
    def dev_open_window_fit_size (self,row=0, column=0, Width=256, Height=256, father_window=0, mode='visible'):
        """
        打开图形窗口

        :param row: 左上角的行索引。建议:0断言:Row >= 0
        :param column: 左上角的列索引。建议:0断言:Column >= 0
        :param Width: 窗口的宽度。取值建议:256断言:0 < Width <= 32768 || Width == -1
        :param Height: 窗口的高度。取值建议:256断言:0 < Height <= 32768 || Height == -1
        :param father_window: 父窗口的逻辑编号。要指定显示为父，您可以输入'root'或0。取值建议:0断言:FatherWindow >= 0
        :param mode: 窗口模式。取值建议:'visible' 可见
        :return: WindowHandle: 窗口句柄
        """
        return halcon.open_window(row , column , Width, Height, father_window, mode, machine='')
    def dev_set_color(self,window_handle ,color='white'):
        """
        设置输出颜色

        :param window_handle: 窗口句柄
        :param color: 输出颜色名称。价值建议:white
        """
        return halcon.set_color(window_handle ,color)
    def dev_set_draw(self,window_handle ,mode='fill'):
        """
        定义区域填充模式
        如果输出模式为“边距”且线宽大于1，则对象可能不会显示。

        :param window_handle: 窗口句柄
        :param mode: 区域输出的填充模式。建议:fill
        """
        return halcon.set_draw(window_handle ,mode)
    def dev_set_line_width(self, window_handle ,width=1.0):
        """
        定义区域轮廓输出的线宽。
        如果输出模式设置为'margin'(参见set_draw)，线宽很重要。如果线宽大于1，则可能无法始终正确显示区域。

        :param window_handle: 窗口句柄
        :param width: 轮廓模式下区域输出的线宽度。取值建议:1.0断言:Width >= 1.0 && Width <= 2000.0
        :return:
        """
        return halcon.set_line_width(window_handle ,width)
    def dev_set_part(self,window_handle ,row_1=0,column_1=0,row_2=-1,column_2=-1):
        """
        设置图形窗口中要显示的图像部分

        :param window_handle: 窗口句柄
        :param row_1: 所选图像部分左上角的行。建议:0
        :param column_1: 所选图像部分左上角的列。建议:0
        :param row_2: 所选图像部分右下角的行。取值建议:-1断言:Row2 >= Row1 || Row2 == -1 || Row1 == 0 && Row2 == -2
        :param column_2: 所选图像部分右下角的列。取值建议:-1断言:Column2 >= Column1 || Column2 == -1 || Column1 == 0 && Column2 == -2
        :return:
        """
        halcon.set_part(window_handle ,row_1 ,column_1 ,row_2 ,column_2)
    def dev_display(self, object,window_handle ):
        """
        显示图像对象(图像、区域、XLD)。

        :param object: 要显示的图像对象
        :param window_handle: 窗口句柄
        :return:
        """
        return halcon.disp_obj(object,window_handle)
    def get_mbutton(self,window_handle):
        """
        等待，直到按下鼠标按钮

        :param window_handle: 窗口句柄
        :return: Row : 鼠标光标在图像坐标系中的行坐标
        """
        return halcon.get_mbutton(window_handle)
    def write_string(self,window_handle,string='hello'):
        """
        窗口中写字

        :param window_handle: 窗口句柄
        :param string: 输出值的元组(所有类型)。价值建议:hello
        :return:
        """
        halcon.write_string(window_handle,string)
    def dump_window_image(self,window_handle):
        """
        将窗口的内容截图成图像

        :param window_handle: 窗口句柄
        :return: Saved image: 保存图像。
        """
        return halcon.dump_window_image(window_handle)

    """""""""""""""""""""""""""""""""""""""""
                            *图像基本*
    """""""""""""""""""""""""""""""""""""""""
    def read_image(self, file_name):
        """
        读取具有不同文件格式的图像。

        :param file_name: 要读取的图像路径
        :return Read image: 读取图像
        """

        return halcon.read_image(file_name)
    def get_image_size(self,image ):
        """
        返回图像的大小

        :param image: 输入图像
        :return: Width, Height 图像的宽度和高度
        """
        return halcon.get_image_size(image)
    """""""""""""""""""""""""""""""""""""""""
                        *模板匹配*
    """""""""""""""""""""""""""""""""""""""""
    def create_shape_model(self,template,num_levels='auto',angle_start=-30,angle_extent=60,
                           angle_step='auto',scale_min=0.9,scale_max=1.1,scale_step='auto',optimization='auto',metric='use_polarity',contrast='auto',min_contrast='auto'):
        """
        创建形状模型

        :param template: 输入图像，其域将用于创建模型
        :param num_levels: 金字塔级别的最大数量。取值建议:auto
        :param angle_start: 角度范围：开始角度，默认-30
        :param angle_extent: 角度范围：结束角度，默认60
        :param angle_step: 角度步长，默认'auto'
        :param scale_min: 缩放范围：最小缩放，默认0.9
        :param scale_max: 缩放范围：最大缩放，默认1.1
        :param scale_step: 缩放步长(分辨率)。取值建议:auto断言:ScaleStep >= 0
        :param optimization: 优化函数-用于生成模型的一种优化和可选方法。取值建议:auto
        :param metric: 匹配度。取值建议:use_polarity
        :param contrast: 对比度-模板图像中对象对比度的阈值或滞后阈值以及可选的对象部分的最小尺寸。取值建议:auto
        :param min_contrast: 搜索图像中对象的最小对比度。取值建议:auto断言:MinContrast < Contrast
        :return: model_id: 模型句柄
        """
        return halcon.create_scaled_shape_model(template,num_levels ,angle_start ,angle_extent ,angle_step ,scale_min ,scale_max ,scale_step ,optimization ,metric ,contrast,min_contrast)
    def write_shape_model(self,model_id,file_name):
        """
        保存模型

        :param model_id: 模型的句柄
        :param file_name: 文件名
        """
        return halcon.write_shape_model(model_id,file_name)
    def read_shape_model(self,file_name):
        """
        读取模型

        :param file_name: 文件名
        :return: model_id: 模型的句柄
        """
        return halcon.read_shape_model(file_name)
    def find_scaled_shape_model(self,image, model_id ,angle_start=-30, angle_extent=60 ,scale_min=0.9 ,scale_max=1.1 ,
                                min_score=0.5 ,num_matches=1 ,max_overlap=0.5 ,sub_pixel='least_squares' ,num_levels=0,greediness=0.9):
        """
        在图像中寻找各向同性缩放形状模型的最佳匹配

        :param image: 应该在其中找到模型的输入图像。
        :param model_id: 模型的句柄
        :param angle_start:  角度范围：开始角度，默认-30
        :param angle_extent:  角度范围：结束角度，默认60
        :param scale_min: 缩放范围：最小缩放，默认0.9
        :param scale_max: 缩放范围：最大缩放，默认1.1
        :param min_score: 要查找的模型实例的最小分数。取值建议:0.5
        :param num_matches: 要查找的模型实例的数量(或0表示所有匹配)。建议值:1
        :param max_overlap: 要查找的模型实例的最大重叠。取值建议:0.5
        :param sub_pixel: 如果不等于'none'，则亚像素精度。取值建议:least_squares
        :param num_levels: 匹配中使用的金字塔级别的数量(如果$|NumLevels| = 2$，则使用的最低金字塔级别)。建议:0
        :param greediness: 贪婪系数:0~1    0-慢而安全；1-快而可能匹配失败，默认0.9
        :return: Row,Column,Angle,Scale,Score,: 找到的模型实例的行坐标,列坐标，旋转角度，缩放倍数，置信度

        """
        return halcon.find_scaled_shape_model(image, model_id ,angle_start, angle_extent ,scale_min ,scale_max ,min_score ,num_matches ,max_overlap ,sub_pixel ,num_levels ,greediness)
    def clear_shape_model(self,model_id):
        """
        释放形状模型的内存。

        :param model_id: 模型的句柄
        """
        halcon.clear_shape_model(model_id)

if __name__ == '__main__':
    PyHalcon.dev_display('')