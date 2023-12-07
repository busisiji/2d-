# !/usr/bin/env python
# -*- encoding: utf-8 -*-
import copy
import math
import os
from ctypes import cdll

import numpy as np
import cv2
import glob
import time
import sys

from scipy.spatial import distance

from lib.path import get_project_root, path_join, Globals, getPath

thispath = os.path.dirname(os.path.abspath(__file__))
dllpaths = [getPath('core/hAcqDirectFile.dll'),getPath('core/halcon.dll'),getPath('core/halconc.dll'),getPath('core/halconcpp.dll'),getPath('core/hcanvas.dll'),getPath('core/hdevenginecpp.dll')]
for dllpath in dllpaths:
    path = path_join(thispath,dllpath)
    cdll.LoadLibrary(path)

import halcon as ha
project_path = get_project_root()

class Calibration:
    '''
    使用张正友相机标定法进行相机标定
    '''
    def __init__(self):
        self.calibration_images = 'calibration_images/'
        self.savedir = path_join(project_path, 'camera_data')

    def CapturePicture(self):
        '''采集不同角度的棋格图片，至少3张'''
        # 删除calibration_images目标文件夹下所有内容，保留calibration_images文件夹
        for root, dirs, files in os.walk(self.calibration_images, topdown=False):
            # print(root) # 各级文件夹绝对路径
            # print(dirs) # root下一级文件夹名称列表，如 ['文件夹1','文件夹2']
            # print(files)  # root下文件名列表，如 ['文件1','文件2']
            # 第一步：删除文件
            for name in files:
                os.remove(os.path.join(root, name))  # 删除文件
            # 第二步：删除空文件夹
            for name in dirs:
                os.rmdir(os.path.join(root, name))  # 删除一个空目录
        cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        flag = cap.isOpened()
        if not flag:
            print('摄像头有问题！')
            sys.exit()
        index = 1
        while (flag):
            ret, frame = cap.read()
            cv2.imshow("img", frame)
            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):  # 按下s键，进入下面的保存图片操作
                cv2.imwrite(self.calibration_images+ str(index) + ".jpg", frame)
                print("save" + str(index) + ".jpg successfuly!")
                print("-------------------------")
                index += 1
            elif k == ord('q'):  # 按下q键，程序退出
                break
        cap.release() # 释放摄像头
        cv2.destroyAllWindows()# 释放并销毁窗口

    def calibrationCamera(self,x_corner_num=7,y_corner_num=7):
        '''求内参矩阵'''
        objp = np.zeros((x_corner_num * y_corner_num, 3), np.float32)
        # add 2.5 to account for 2.5 cm per square in grid
        objp[:, :2] = np.mgrid[0:y_corner_num, 0:x_corner_num].T.reshape(-1, 2) * 2.5

        # Arrays to store object points and image points from all the images.
        objpoints = []  # 3d point in real world space
        imgpoints = []  # 2d points in image plane.
        images = glob.glob(self.calibration_images+'*.jpg')

        print("getting images")
        for fname in images:
            img = cv2.imread(fname)
            print(fname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # 查找棋盘格角点信息
            ret, corners = cv2.findChessboardCorners(gray, (y_corner_num, x_corner_num), None)
            if ret == True:
                objpoints.append(objp)
                # 精细化角点信息
                imgpoints.append(corners)
                img1 = img

        cv2.destroyAllWindows()

        # 标定，camera_params 是相机内参，distortion_params 是畸变，rvecs,tvecs 分别是旋转矩阵和平移矩阵代表外参
        ret, self.intrinsic_camera_params, self.distortion_params, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        h, w = img1.shape[:2]
        # 使用cv2.getOptimalNewCameraMatrix()函数计算出一个新的相机矩阵和感兴趣区域
        self.new_camera_params, self.roi = cv2.getOptimalNewCameraMatrix(self.intrinsic_camera_params, self.distortion_params, (w, h), 1, (w, h))

        # 保存
        # 相机内参
        np.save(path_join(self.savedir, 'intrinsic_camera_params.npy'), self.intrinsic_camera_params)
        np.save(path_join(self.savedir, 'new_camera_params.npy'), self.new_camera_params)
        # 畸变参数
        np.save(path_join(self.savedir, 'distortion_params.npy'), self.distortion_params)
        # 感兴趣区域
        np.save(path_join(self.savedir, 'roi.npy'), self.roi)

        return ret, self.intrinsic_camera_params, self.distortion_params, rvecs, tvecs

    def calibratioProjection(self,worldPoints=[[424.018, 35.028],[424.303, -12.525],[424.534, -59.973],[386.073, 34.897],[386.635, -12.78],[386.92, -59.916],[348.239, 34.611],[348.723, -13.085],[348.921, -60.124]],
                 imagePoints=[[284.0, 235.0], [395.0, 236.0], [503.0, 238.0], [284.0, 323.0], [395.0, 323.0], [503.0, 325.0], [285.0, 409.0], [395.0, 410.0], [503.0, 410.0]],total_points_used=9):
        '''求转换矩阵'''
        try:
            new_camera_params = np.load(path_join(self.savedir , 'new_camera_params.npy'))
            distortion_params = np.load(path_join(self.savedir , 'distortion_params.npy'))
        except:
            print('请先进行相机内参标定')

        self.worldPoints = np.array([row + [0] for row in worldPoints], dtype=np.float32)
        self.imagePoints = np.array(imagePoints, dtype=np.float32)
        # 通过解PNP问题求解相机的旋转向量(rvec1)和平移向量(tvec1)
        ret, self.rvec1, self.tvec1 = cv2.solvePnP(self.worldPoints, self.imagePoints, distortion_params, new_camera_params)
        # 使用旋转向量通过罗德里格斯公式计算得到旋转矩阵
        self.rotate_params, jac = cv2.Rodrigues(self.rvec1)
        # 将旋转矩阵和旋转向量组合得到外参矩阵，即相机的旋转和平移矩阵
        self.external_camera_params = np.column_stack((self.rotate_params, self.tvec1))
        # 通过新相机矩阵和外参矩阵，可以计算相机的投影矩阵，投影矩阵描述了相机将3D点投影到2D图像上的过程，包括相机的内参和外参
        self.projection_params = self.new_camera_params.dot(self.external_camera_params)

        self.s_arr = np.array([0], dtype=np.float32)
        self.s_describe = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float32)
        for i in range(0, total_points_used):
            XYZ1 = np.array([[self.worldPoints[i, 0], self.worldPoints[i, 1], self.worldPoints[i, 2], 1]], dtype=np.float32)
            XYZ1 = XYZ1.T
            suv1 = self.projection_params.dot(XYZ1)
            s = suv1[2, 0]
            self.s_arr = np.array([s / total_points_used + self.s_arr[0]], dtype=np.float32)
            self.s_describe[i] = s
            # np.save(path_join(self.savedir , 's_arr.npy'), self.s_arr)

        # 保存
        # np.save(path_join(self.savedir , 'rotate_params.npy'), self.rotate_params)
        # np.save(path_join(self.savedir , 'external_camera_params.npy'), self.external_camera_params)
        # np.save(path_join(self.savedir , 'projection_params.npy'), self.projection_params)
        print('rotate_params.npy',self.s_arr,self.rotate_params,self.external_camera_params,self.projection_params)

    def calculate_XYZ(self, u, v):
        # 图像坐标转世界坐标
        try:
            s_arr = np.load(path_join(self.savedir , 's_arr.npy'))
            new_camera_params = np.load(path_join(self.savedir , 'new_camera_params.npy'))
            rotate_params = np.load(path_join(self.savedir , 'rotate_params.npy'))
        except:
            print('请先进行相机内参标定')

        self.scalingfactor = s_arr[0]
        self.inverse_newcam_mtx = np.linalg.inv(new_camera_params)
        self.inverse_R_mtx = np.linalg.inv(self.R_mtx)
        uv_1 = np.array([[u, v, 1]], dtype=np.float32)
        uv_1 = uv_1.T
        suv_1 = self.scalingfactor * uv_1
        xyz_c = self.inverse_newcam_mtx.dot(suv_1)
        xyz_c = xyz_c - self.tvec1
        XYZ = self.inverse_R_mtx.dot(xyz_c)

        return XYZ

    def CalculationError(self,total_points_used=9):
        # 计算误差
        s_mean, s_std = np.mean(self.s_describe), np.std(self.s_describe)
        for i in range(0, total_points_used):
            print("Point " + str(i))
            print("S: " + str(self.s_describe[i]) + " Mean: " + str(s_mean) + " Error: " + str(self.s_describe[i] - s_mean))

def findRound(image_path='F:/2d-/images/target/jiu.png',score=0.5, size=8068 ):
    """
    查找图像中的圆

    @param image_path: 图像路径
    @param score: 圆的最低相似度
    @return: 圆中心坐标 x,y
    """
    image = ha.read_image(image_path)  # 读取图片
    width, height = ha.get_image_size(image)  # 获取图片大小
    if ha.count_channels(image)[0] == 3:  # 通道数
        gray_image = ha.rgb1_to_gray(image)  # 转换为灰度图像
    else:
        gray_image = image
    binary_image = ha.threshold(gray_image, 128.0, 255.0)  # 灰度图像阈值分割
    regions = ha.connection(binary_image)  # 连通组件分析
    selected_regions = ha.select_shape(regions, 'circularity', 'and', score, 1.0)  # 根据形状特征选择区域 circularity：与圆的相似度
    selected_regions = ha.select_shape(selected_regions, 'area', 'and', size, 10081)
    sorted_regions = ha.sort_region(selected_regions, 'character', 'True', 'row')  # 排序
    areas, Rows, Columns = ha.area_center(sorted_regions)  # 计算中心坐标
    return Rows, Columns

def CalculationError(calibration_matrix,world_points,image_points):

    predicted_world_points =  copy.deepcopy(world_points)
    # 将这四个世界坐标点通过转换矩阵转换到图像坐标系中
    for i in range(len(image_points)):
        [predicted_world_points[i][0]],[predicted_world_points[i][1]] = ImagetoWorld(image_points[i][0],image_points[i][1], calibration_matrix)
    # 计算预测的图像坐标与实际图像坐标之间的欧氏距离误差
    world_points = np.array(world_points, dtype=np.float32)
    predicted_world_points = np.array(predicted_world_points, dtype=np.float32)
    euclidean_distances = distance.cdist(world_points, predicted_world_points, 'euclidean')

    return euclidean_distances


def getTransformationMatrix(Columns=None,Rows=None,X=None,Y=None):
    """
    求相机和机械臂的转换矩阵

    param X: 机械臂x坐标
    param Y: 机械臂y坐标
    param Columns: 图像x坐标
    param Rows: 图像y坐标
    """
    # 调试用
    # worldPoints = [[424.018, 35.028], [424.303, -12.525], [424.534, -59.973], [386.073, 34.897]]
    # imagePoints = [[284.0, 235.0], [395.0, 236.0], [503.0, 238.0], [284.0, 323.0]]
    # X,Y = [i[0] for i in worldPoints], [i[1] for i in worldPoints]
    # Columns, Rows = [i[0] for i in imagePoints], [i[1] for i in imagePoints]

    worldPoints, imagePoints = [],[]
    for i in range(len(Columns)):
        imagePoints.append([Columns[i],Rows[i]])
    for i in range(len(X)):
        worldPoints.append([X[i],Y[i]])
    HomMat2D = ha.vector_to_hom_mat2d(Columns, Rows, X, Y)  # 计算仿射变换矩阵
    average_distance = CalculationError(HomMat2D,worldPoints,imagePoints)
    # 计算矩阵中所有元素的平均值
    average_error = np.mean(average_distance)
    return HomMat2D,average_error


def ImagetoWorld(Column,Row,hom_mat2d):
    """
    图像坐标转世界坐标

    param Column: 图像x坐标
    param Row: 图像y坐标
    param hom_mat2d: 转换矩阵
    return: 世界坐标
    """
    xy = ha.affine_trans_point_2d(hom_mat2d, Column, Row)
    # print(xy)
    return xy

if __name__ == '__main__':
    # getTransformationMatrix()
    # Px = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    # Py = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    # Qx = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0]
    # Qy = [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0]
    # HomMat2D = ha.vector_to_hom_mat2d(Px, Py, Qx, Qy)
    # print(HomMat2D)
    # ha.disp_rectangle1()

    import halcon

    # halcon.dev_set_draw('margin')
    # ImageRootName = '../../mytest/test2.png'
    # Regions = ['黄色', '粉色', '蓝色', '背景']
    # Highlight = ['goldenrod', 'magenta', 'cyan']
    #
    # # 创建一个空区域对象，用于保存训练样本
    # Classes = halcon.gen_empty_obj()
    #
    # # 下面这个循环里一个是用彩色图片训练网络，一个用模拟的灰度图片训练网络。
    # # 从最后的结果来看，用彩色的图片训练的网络能更好的完成任务；而用模拟的
    # # 灰度图片训练的网络分类效果不是很好。这说明颜色特征还是非常有用的。
    # for Mode in range(2):
    #     # halcon.dev_set_color('black')
    #     Image = halcon.read_image(ImageRootName)
    #     Width, Height = halcon.get_image_size(Image)
    #     WindowHandle = halcon.open_window(0, 0, Width, Height, father_window=0, mode='visible', machine='')
    #     if Mode == 1:
    #         # pass
    #     #     # 模拟灰色图像
    #         GrayImage = halcon.rgb1_to_gray(Image)
    #         Image = halcon.compose3(GrayImage, GrayImage, GrayImage)
    #         halcon.disp_obj(Image, WindowHandle)
    #     if Mode == 0:
    #         # ***
    #         # 1 生成训练样本（指定颜色类别）
    #         # ***
    #         for i in range(1, 5):
    #             halcon.disp_obj(Image, WindowHandle)
    #             halcon.disp_obj(Classes, WindowHandle)
    #             halcon.disp_text(WindowHandle, ['在' + Regions[i - 1] + '区域画一个矩形', '点击鼠标右键确认'],
    #                                 'window', 24, 12, 'black',[],[])
    #             # 注意：画矩形的时候，不要把背景信息包括进去了；否则，检测效果会不好的
    #             Row1, Column1, Row2, Column2 = halcon.draw_rectangle1(WindowHandle)
    #             Rectangle = halcon.gen_rectangle1(Row1, Column1, Row2, Column2)
    #             Classes = halcon.concat_obj(Rectangle, Classes)
    #
    #     # ***
    #     # 训练多层感知机网络
    #     # ***
    #
    #     # 2.1 创建并设置多层感知机网络参数
    #     MLPHandle = halcon.create_class_mlp(3, 10, 4, 'softmax', 'normalization', 3, 42)
    #     # MLPHandle = halcon.create_class_mlp(20, 10, 5, 'softmax', 'normalization', 3, 42)
    #     if halcon.tuple_is_valid_handle(MLPHandle):
    #         print("MLP 模型加载成功！")
    #     else:
    #         print("MLP 模型加载失败！")
    #     print(Classes)
    #     # 2.2 把训练样本添加到网络中
    #     halcon.add_samples_image_class_mlp(Image, Classes, MLPHandle)
    #     halcon.set_tposition(WindowHandle, 100, 12)
    #     halcon.write_string(WindowHandle, 'Training...')
    #
    #     # 2.3 训练多层感知机网络
    #     Error, ErrorLog = halcon.train_class_mlp(MLPHandle, 400, 0.5, 0.01)
    #
    #     for img in range(1,4):
    #         Image = halcon.read_image(ImageRootName)
    #         if Mode == 1:
    #             GrayImage = halcon.rgb1_to_gray(Image)
    #             Image = halcon.compose3(GrayImage, GrayImage, GrayImage)
    #
    #         # ***
    #         # 在随后的图片中使用多层感知机分类物品
    #         # ***
    #
    #         ClassRegions = halcon.classify_image_class_mlp(Image, MLPHandle, 0.5)
    #
    #         halcon.disp_obj(Image, WindowHandle)
    #         halcon.disp_text(WindowHandle, '查看每一种颜色的棋子是否有四个...', 'window', 24, 12, 'black',[],[])
    #         halcon.set_line_width(WindowHandle, 2)
    #         for figure in range(1,4):
    #             ObjectsSelected = halcon.copy_obj(ClassRegions, figure, 1)
    #             ConnectedRegions = halcon.connection(ObjectsSelected)
    #             SelectedRegions = halcon.select_shape(ConnectedRegions, 'area', 'and', 400, 99999)
    #             Number = halcon.count_obj(SelectedRegions)
    #             # halcon.set_color(WindowHandle,Highlight[figure - 1])
    #             # halcon.disp_obj(SelectedRegions, WindowHandle)
    #             OutString = Regions[figure - 1] + ': ' + str(Number) + '   '
    #             halcon.set_color(WindowHandle,'green')
    #             halcon.disp_text(WindowHandle,OutString, 'window', 24 + 30 * figure, 12, 'black', [],[])
    #             if Number == 4:
    #                 halcon.disp_text(WindowHandle, 'Not OK', 'window', 24 + 30 * figure, 70, 'black', [],[])
    #             else:
    #                 halcon.disp_text(WindowHandle, 'OK', 'window', 24 + 30 * figure, 70, 'green', [],[])
    #     #   halcon.disp_continue_message('WindowHandle', 'black', 'true')
    #     #     halcon.stop()
    #         break
    #
    #
    # # halcon.set_line_width(WindowHandle,3)
    # # halcon.set_draw(WindowHandle,'fill')
    # # halcon.clear_window()
    # halcon.wait_seconds(30)
    Row1 = 400.0
    Row2 = 1200.0
    # Column1 = 299.6869565217391
    # Column2 = 899.0608695652174
    Column1 = Row1
    Column2 = Row2
    Rectangle = halcon.gen_rectangle1(Row1, Column1, Row2, Column2)
    print(Rectangle)
