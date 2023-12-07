import os
import sys
import time
from ctypes import cdll

from lib.path import path_join, Globals, globalsdynamic
from lib.utils import get_new_model_name

#
# thispath = os.path.dirname(os.path.abspath(__file__))
thispath = path_join(Globals.project_path,'core')
dllpaths = ['hAcqDirectFile.dll','halcon.dll','halconcpp.dll','hcanvas.dll','hdevenginecpp.dll']
for dllpath in dllpaths:
    path = path_join(thispath,dllpath)
    cdll.LoadLibrary(path)
# sys.path.append(thispath)

# print(sys.path)
import halcon as ha

class ShapTemplateMatching():
    def __init__(self,
                 tmppath=r'C:\Users\Administrator\Desktop\MKC\untitled1\images\tpl\c0.jpg',
                 imgpath=r'C:\Users\Administrator\Desktop\MKC\untitled1\images\target\sec2.jpg',
                 angle_start=0,
                 angle_extent=360,
                 angle_step='auto',
                 scale_min=0.9,
                 scale_max=1.1,
                 max_overlap=0.8,  # 重叠系数
                 min_score=0.8,  # 最低的匹配分数
                 num_levels=0,  # 搜索时使用的金字塔层数
                 num_matches=1,  # 在图像上找到模板的最大个数
                 greediness=0.9,  # 贪婪系数
                 mask=[None,None,None], # 掩码 pos size type
                 ):
        '''
        基于形状的模板匹配

        :param tmppath: 模板图片路径
        :param imgpath: 目标图片路径
        :param angle_start: 角度范围：开始角度，默认-30
        :param angle_extent: 角度范围：结束角度，默认60
        :param angle_step: 角度步长，默认'auto'
        :param scale_min: 缩放范围：最小缩放，默认0.9
        :param scale_max: 缩放范围：最大缩放，默认1.1
        :param max_overlap: 重叠系数:0~1，默认0.8   0-目标区域不能存在重叠 1-所有找到的目标区域都要返回
        :param min_score: 最低的匹配分数，默认0.8
        :param num_levels: 搜索时使用的金字塔层数，默认0
        :param num_matches: 在图像上找到模板的最大个数，默认1
        :param greediness: 贪婪系数:0~1    0-慢而安全；1-快而可能匹配失败，默认0.9
        :param ShapeModelpath: 保存形状模板的路径
        '''
        self.tmppath = tmppath
        self.imgpath = imgpath
        self.angle_start_deg = angle_start
        self.angle_extent_deg = angle_extent
        self.angle_start_rad = ha.tuple_rad(self.angle_start_deg)[0]
        self.angle_extent_rad = ha.tuple_rad(self.angle_extent_deg)[0]
        self.angle_step = angle_step
        self.scale_min = scale_min
        self.scale_max = scale_max
        self.max_overlap = max_overlap
        self.min_score = min_score
        self.num_levels = num_levels
        self.num_matches = num_matches
        self.greediness = greediness
        self.ShapeModelpath = 'ShapeModel_dot.shm'
        self.mask = mask
        self.EmptyObject = None


    def init_image(self):
        '''预处理'''
        # *阈值化
        Regions = ha.threshold(self.img, 0, 122)
        #*连通区域分块
        ConnectedRegions = ha.connection(Regions)
        #*内部区域填充
        RegionFillUp = ha.fill_up(ConnectedRegions)
        #*区域特征筛选（面积特征）
        SelectedRegions = ha.select_shape(RegionFillUp, 'area', 'and', 14845, 57911.9)
        #*膨胀处理
        RegionDilation = ha.dilation_circle(SelectedRegions, 3.5)
        # #*裁剪目标区域图像
        # ImageReduced = ha.reduce_domain(Image, RegionDilation)
        # return ImageReduced
        pass

    def set_mask_roi(self):
        """创建掩码roi"""
        if not self.mask[1]:
            return self.img
        y = self.mask[0].x()
        y = self.mask[0].x()
        x = self.mask[0].y()
        h = self.mask[1].width()
        w = self.mask[1].height()
        ImageReduced = self.img
        if self.mask[-1] == '矩形':
            reduced = ha.rectangle1_domain(self.img, x, y, x+w, y+h)
            ImageReduced = ha.reduce_domain(self.img, reduced)  # 裁剪图像
            # Domain = ha.get_domain(self.img)
            # RegionDifference1 = ha.difference(Domain,reduced)
            # ImageReduced = ha.paint_region(RegionDifference1, self.img, 1, 'fill')
        elif self.mask[-1] == '圆形':
            circle = ha.gen_circle(x + w / 2, y + h /2, h / 2) # 实心圆
            ImageReduced = ha.reduce_domain(self.img, circle)  # 裁剪图像
            # Domain = ha.get_domain(self.img)
            # RegionDifference1 = ha.difference(Domain, circle)
            # ImageReduced = ha.paint_region(RegionDifference1, self.img, 1, 'fill')
        return ImageReduced


    def set_tmp_roi(self,type_select,path,scale=2):
        """创建模板roi"""
        ImageReduced = ha.read_image(path) if self.tmppath else ''
        if '圆形' == type_select:
            Image = ha.read_image( path) # 读取图像
            [Width], [Height]  = ha.get_image_size(Image)
            circle = ha.gen_circle(Height / 2, Width / 2, Height / 2) # 实心圆
            # 这里取消掉reduce_domain得到搜索图像，而是采用paint_region方式
            ImageReduced = ha.reduce_domain(Image, circle) # 裁剪图像
        elif '圆环' == type_select:
            Image = ha.read_image(path)  # 读取图像
            [Width], [Height] = ha.get_image_size(Image)
            circle = ha.gen_circle(Height / 2, Width / 2, Height / 2 * (scale + 1)  / (2*scale) )  # 实心圆
            RegionDilation = ha.boundary(circle, 'inner')  # 把一个区域缩小到他的边界，即半径缩小一个像素尺寸
            RegionBorder = ha.dilation_circle( RegionDilation,Height / 2 * ((scale-1 )  / (2*scale)) )  # 扩大一个圆形结构基础的一个区域；scale：=圆环尺寸
            ImageReduced = ha.reduce_domain(Image, RegionBorder)  # 裁剪图像

            # # # 窗口显示
            # WindowHandle = ha.open_window(0, 0, Width/2, Height/2, father_window=0, mode='visible', machine='')
            # ha.disp_obj(ImageReduced, WindowHandle)
            # ha.wait_seconds(10)
        return ImageReduced


    def save_template(self,model_name=None,type_select='矩形',scale=2):
        '''生成模板'''
        if not model_name:
            model_name = self.ShapeModelpath
        ImageReduced = self.set_tmp_roi(type_select,self.tmppath,scale)

        # *创建一个轮廓匹配模型基于金字塔的图像
        # ModelImages, ModelRegions = ha.inspect_shape_model(Image,4,30)
        # 准备一个匹配轮廓模型
        # ModelID = ha.create_shape_model(self.img_tmp,'auto',-0.39,0.79,'auto','auto', 'use_polarity','auto','auto') # 生成的匹配图像有移动和旋转
        # print(self.img_tmp, 'auto', self.angle_start_rad, self.angle_extent_rad,self.angle_step,self.scale_min,self.scale_max)
        ModelID = ha.create_scaled_shape_model(ImageReduced, 'auto', self.angle_start_rad, self.angle_extent_rad,self.angle_step,self.scale_min,self.scale_max,'auto', 'auto', 'use_polarity', 'auto', 'auto') #除了移动和旋转还有放大缩小
        # ModelID = ha.create_scaled_shape_model(self.img_tmp, 'auto', ha.tuple_rad(self.angle_start)[0], ha.tuple_rad(self.angle_extent)[0],self.angle_step,self.scale_min,self.scale_max,'auto', 'auto', 'use_polarity', 'auto', 'auto') # //除了移动和旋转还有放大缩小，但这个的放大缩小是可以控制X轴Y轴放大缩小
        # *保存模板
        ha.write_shape_model(ModelID, model_name)
        # # *清除模板
        ha.clear_shape_model(ModelID)

        return model_name
    def matching_template(self,model_name=None):
        '''模板匹配'''
        if not model_name:
            model_name = self.ShapeModelpath

        self.img = ha.read_image(self.imgpath) if os.path.exists(self.imgpath) else ''
        # self.init_image()
        ImageReduced = self.set_mask_roi()


        # 获取模板名
        # *读取形状模板
        self.ShapeModelID = ha.read_shape_model(model_name)

        #
        # *模板匹配
        # *剩下的几个参数是匹配图像的位置状态等参数
        self.Row,self.Column,self.Angle,self.Scale,self.Score = ha.find_scaled_shape_model(ImageReduced, self.ShapeModelID, angle_start = self.angle_start_rad,angle_extent = self.angle_extent_rad,scale_min = self.scale_min,scale_max = self.scale_max,  min_score = self.min_score, num_matches = self.num_matches,
                                max_overlap = self.max_overlap, sub_pixel='least_squares', num_levels = self.num_levels, greediness = self.greediness)
        # print('find_scaled_shape_model',self.Row,self.Column,self.Angle,self.Scale,self.Score)
        self.Model = [0] * len(self.Row)
        return self.Row,self.Column,self.Angle,self.Scale,self.Score,self.Model
    def matching_templates(self,model_names=None):
        '''多模板匹配'''
        if not model_names:
            model_names = [self.ShapeModelpath]

        self.img = ha.read_image(self.imgpath) if os.path.exists(self.imgpath) else ''
        # self.init_image()
        ImageReduced = self.set_mask_roi()

        # 获取模板名
        # *读取形状模板
        self.ShapeModelIDs = [ha.read_shape_model(model_name) for model_name in model_names]

        # # 屏蔽区域
        # Rectangle = ha.gen_rectangle1( 100, 100, 200, 200)
        # self.ShapeModelIDs = [ha.set_shape( 'negative', 0, 0, Rectangle) for model_name in model_names]

        # *模板匹配
        # *剩下的几个参数是匹配图像的位置状态等参数
        result = ha.find_scaled_shape_models(ImageReduced, self.ShapeModelIDs, angle_start = self.angle_start_rad,angle_extent = self.angle_extent_rad,scale_min = self.scale_min,scale_max = self.scale_max,  min_score = self.min_score, num_matches = self.num_matches,
                                max_overlap = self.max_overlap, sub_pixel='least_squares', num_levels = self.num_levels, greediness = self.greediness)
        self.Row, self.Column, self.Angle, self.Scale, self.Score , self.Model= result

        return self.Row,self.Column,self.Angle,self.Scale,self.Score , self.Model

    def show_result_contour_xld(self,time=5):
        '''显示匹配结果，将匹配得到的实例以形状轮廓的形式绘制出来 实心'''
        # *获取图像的宽高
        Width, Height = ha.get_image_size(self.img)
        WindowHandle = ha.open_window(0, 0, Width[0]/2, Height[0]/2, father_window=0, mode='visible', machine='')
        ha.disp_obj(self.img, WindowHandle)
        # *返回一个轮廓模型的轮廓表示
        model_contours = ha.get_shape_model_contours(self.ShapeModelID, 1)
        # 循环遍历匹配结果
        for i in range(len(self.Score)):
            # 获取匹配目标的旋转矩阵
            hom_mat2d_rotate = ha.vector_angle_to_rigid(0, 0, 0, self.Row[i], self.Column[i], self.Angle[i])

            # 添加缩放量生成新的矩阵
            hom_mat2d_scale = ha.hom_mat2d_scale(hom_mat2d_rotate, self.Scale[i], self.Scale[i], self.Row[i], self.Column[i])

            # 对模板轮廓进行矩阵变换
            contours_affine_trans = ha.affine_trans_contour_xld(model_contours, hom_mat2d_scale)

            # 将轮廓转换为区域
            region = ha.gen_region_contour_xld(contours_affine_trans, 'filled')

            # 生成最小外接矩形
            row1, column1, row2, column2 = ha.smallest_rectangle1(region)

            # 框选匹配结果
            ha.set_color(WindowHandle,'green')
            ha.disp_rectangle1(WindowHandle, row1, column1, row2, column2)

            # 勾画匹配结果轮廓
            ha.set_color(WindowHandle,'red')
            ha.disp_obj(contours_affine_trans,WindowHandle)

            ha.wait_seconds(time)
    def show_result(self,time=5):
        '''显示匹配结果，将匹配得到的实例以形状轮廓的形式绘制出来 轮廓'''
        # *获取图像的宽高
        if self.img and self.EmptyObject:
            imgWidth, imgHeight = ha.get_image_size(self.img)
            # 数据库读取
            result = globalsdynamic.db_child.query_data_table('View')
            result = result[0] if result else result
            Width, Height = float(result[1]),float(result[2])
            scaleW = Width / imgWidth[0]
            scaleH = Height / imgHeight[0]

            self.img = ha.zoom_image_size(self.img,Width, Height,'bilinear') # 缩放图片

            WindowHandle = ha.open_window(0, 0, Width, Height, father_window=0, mode='buffer',  machine='')  # visible 可见 buffer 不可见
            # WindowHandle = ha.open_window(0,0, Width, Height, father_window=0, mode='visible', machine='') # visible 可见 buffer 不可见
            ha.set_line_width(WindowHandle,2) # 线条宽度
            ha.disp_obj(self.img, WindowHandle) # 图像
            ha.set_draw(WindowHandle,'margin') # 设置画图填充方式
            # ha.set_color(WindowHandle, 'red')  # 使用红色勾画匹配结果轮廓
            # ha.disp_obj(self.EmptyObject, WindowHandle)  # 模板轮廓

            for i in range(len(self.regions)):
                box = self.boxs[i]
                region = self.regions[i]
                ha.set_color(WindowHandle, 'green')  # 使用绿色矩形框，框选匹配结果
                Row1, Column1, Row2, Column2 = box[0]*scaleW, box[1]*scaleH, box[2]*scaleW, box[3]*scaleH
                print(Row1, Column1, Row2, Column2)
                # ha.disp_rectangle1(WindowHandle, Row1, Column1, Row2, Column2) # 结果框
                # ha.set_color(WindowHandle, 'red')  # 使用红色勾画匹配结果轮廓
                # ha.disp_obj(region, WindowHandle)  # 模板轮廓
                Text = f'{self.Model[i]}=\n中心点:{int(self.Column[i]), int(self.Row[i])}\n角度:{round(self.Angle[i],2)}'
                ha.set_font(WindowHandle, f'Arial-Normal-{int((Row2-Row1)/8)}')
                ha.disp_text(WindowHandle, Text, 'window', Row1, Column1, 'orange red', ['box','shadow'],['false','false'])

            image = ha.dump_window_image(WindowHandle) #图像名，窗口句柄
            ha.write_image(image, globalsdynamic.temp_halcon_path.split('.')[1], 0, globalsdynamic.temp_halcon_path.split('.')[0])
            # ha.wait_seconds(time)
            # 清理关闭窗口
            ha.clear_window(WindowHandle)
            ha.close_window(WindowHandle)

    def get_result(self):
        """
        :return: [Row1（左上y坐标列表），Column1（左上x坐标列表），Row2（右下y坐标列表），Column2（右下x坐标列表）]，结果轮廓
        """
        self.boxs = []
        self.regions = []
        outlines = []
        # *返回一个轮廓模型的轮廓表示
        model_contours = ha.get_shape_model_contours(self.ShapeModelID, 1)
        # 循环遍历匹配结果
        for i in range(len(self.Score)):
            # 获取匹配目标的旋转矩阵
            hom_mat2d_rotate = ha.vector_angle_to_rigid(0, 0, 0, self.Row[i], self.Column[i], self.Angle[i])
            # 添加缩放量生成新的矩阵
            hom_mat2d_scale = ha.hom_mat2d_scale(hom_mat2d_rotate, self.Scale[i], self.Scale[i], self.Row[i],
                                                 self.Column[i])
            # 对模板轮廓进行矩阵变换
            self.contours_affine_trans = ha.affine_trans_contour_xld(model_contours, hom_mat2d_scale)
            self.EmptyObject = self.contours_affine_trans
            # 将轮廓转换为区域
            self.region = ha.gen_region_contour_xld(self.contours_affine_trans, 'filled')
            self.regions.append(self.region)
            # 保存最小外接矩形
            row1, column1, row2, column2 = ha.smallest_rectangle1(self.region) # Row1（左上y坐标），Column1（左上x坐标），Row2（右下y坐标），Column2（右下x坐标）
            self.boxs.append((min(row1), min(column1), max(row2), max(column2)))
            # 保存结果轮廓
            outlines.append(self.contours_affine_trans)
        return self.boxs,outlines
    def get_results(self):
        """
        :return: [Row1（左上y坐标列表），Column1（左上x坐标列表），Row2（右下y坐标列表），Column2（右下x坐标列表）]，结果轮廓
        """
        self.boxs = []
        self.regions = []
        outlines = []
        self.EmptyObject = ha.gen_empty_obj() # 生成一个空集对象
        # 循环遍历匹配结果
        # for s in range(len(self.ShapeModelIDs)):
        for i in range(len(self.Score)):
            # *返回一个轮廓模型的轮廓表示
            model_contour = ha.get_shape_model_contours(self.ShapeModelIDs[self.Model[i]], 1)
            # 获取匹配目标的旋转矩阵
            hom_mat2d_rotate = ha.vector_angle_to_rigid(0, 0, 0, self.Row[i], self.Column[i], self.Angle[i])
            # 添加缩放量生成新的矩阵
            hom_mat2d_scale = ha.hom_mat2d_scale(hom_mat2d_rotate, self.Scale[i], self.Scale[i], self.Row[i],
                                                 self.Column[i])
            # 对模板轮廓进行矩阵变换
            self.contours_affine_trans = ha.affine_trans_contour_xld(model_contour, hom_mat2d_scale)
            # # 连接轮廓
            self.EmptyObject = ha.concat_obj(self.EmptyObject, self.contours_affine_trans)

            # 将轮廓转换为区域
            self.region = ha.gen_region_contour_xld(self.contours_affine_trans, 'filled')
            self.regions.append(self.region)
            # 保存最小外接矩形
            row1, column1, row2, column2 = ha.smallest_rectangle1(self.region) # Row1（左上y坐标），Column1（左上x坐标），Row2（右下y坐标），Column2（右下x坐标）
            self.boxs.append((min(row1), min(column1), max(row2), max(column2)))
            # 保存结果轮廓
            outlines.append(self.contours_affine_trans)
        return self.boxs,outlines


def main(shaptemplatematching):
    model_name = get_new_model_name()
    shaptemplatematching.save_template(model_name)
    shaptemplatematching.matching_template(model_name)
    result = shaptemplatematching.get_result()
    return result
    # shaptemplatematching.show_result(10)

if __name__ == "__main__":
    print('path', globalsdynamic.temp_path, path_join(Globals.temporarily_path, 'tmp_path.jpg' ))
    shaptemplatematching = ShapTemplateMatching(tmppath=path_join(Globals.temporarily_path, 'tmp_path.jpg' ),
                                                imgpath=globalsdynamic.temp_path,
                                                min_score=0.35,
                                                max_overlap = 0.8,
                                                angle_start=0,
                                                angle_extent=360,
                                                scale_min=0.7,
                                                scale_max=1.3,
                                                num_matches=5)
    shaptemplatematching.save_template()
    shaptemplatematching.matching_template()
    shaptemplatematching.get_result()
    shaptemplatematching.show_result(10)
    # ha.classify_image_class_mlp()
    # ha.copy_obj()