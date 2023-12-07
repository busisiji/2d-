import io
from datetime import datetime
import os
import time
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image, ImageTk,ImageQt
import tkinter as tk

from lib.path import path_join

from PyQt5.QtCore import *
from PyQt5.QtGui import *

def imageToPixmap(pil_image):
    """Image转QPixmap格式"""
    # 转化为QImage
    qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height,pil_image.width*3, QImage.Format_RGB888)
    # 转化为QPixmap
    qpixmap = QPixmap.fromImage(qimage)
    return qpixmap


def piltoPixmap(pil_img):
    """PIL格式转QPixmap格式"""
    # print("PIL格式转QPixmap格式")
    # pixmap = ImageQt.toqpixmap(pil_img)
    # return pixmap
    # 初始化QPixmap对象, 第一个图像宽， 第二个图像高
    result = QPixmap(pil_img.size[0], pil_img.size[1])
    bytesIO = io.BytesIO()
    try:
        pil_img.save(bytesIO, format='BMP')
    except:
        pil_img.save(bytesIO, format='PNG')
    result.loadFromData(bytesIO.getvalue())
    return result

def pixmaptoPil(pixmap):
    """QPixmap格式转PIL格式"""
    print("QPixmap格式转PIL格式")
    img_obj = ImageQt.fromqpixmap(pixmap)
    return img_obj

def piltoQimage(pil_image):
    # 将PIL图像转换为QImage
    return QImage(pil_image.tobytes(), pil_image.width, pil_image.height,pil_image.width*3, QImage.Format_RGB888)

def qimagetoPil(qimage):
    """将QImage对象转换为PIL对象"""
    buffer = QBuffer()
    qimage.save(buffer, 'BMP')
    pil_image = Image.open(io.BytesIO(buffer.data()))
    return pil_image

def rotate_image(img, index):
    """
    旋转图片并保存

    :param img: 图片路径 / NumPy数组类型的图片
    :param index: 0 正常 1~3 旋转 4 翻转 5 镜像
    :return:
    """
    if index == 4:
        return flip_image(img)
    elif index == 5:
        return mirror_image(img)
    else:
        angles = [0,90,180,270]
        if isinstance(img, str):
            # 加载图片
            pixmap = QPixmap(img)
            # 创建旋转变换矩阵
            transform = QTransform().rotate(angles[index])
            # 应用变换矩阵到图片
            rotated_pixmap = pixmap.transformed(transform)
            # 保存旋转后的图片
            rotated_pixmap.save(img)
        else:
            if index != 0:
                # img = img.reshape((540, 720, 3))  # 根据自己分辨率进行转化
                img = np.rot90(img, k=index, axes=(0, 1))
            # flipped_image = Image.fromarray(img)
            return img
def flip_image(img):
    if isinstance(img, str):
        # 打开图片
        image = Image.open(img)
        # 上下翻转图片
        flipped_image = image.transpose(Image.FLIP_TOP_BOTTOM)
        # 保存翻转后的图片
        flipped_image.save(img)
    else:
        # 垂直翻转
        flipped_img = np.flipud(img)
        # 将翻转后的数组转换为图片
        # flipped_img = Image.fromarray(flipped_img)
        return flipped_img

def mirror_image(img):
    """左右镜像图像并保存"""
    if isinstance(img, str):
        # 打开图片
        image = Image.open(img)
        # 左右镜像图片
        mirrored_image = image.transpose(Image.FLIP_LEFT_RIGHT)
        # 保存镜像后的图片
        mirrored_image.save(img)
    else:
        # 水平镜像
        # img = img.reshape((540, 720, 3))
        flipped_img = np.fliplr(img)
        # 将镜像后的数组转换为图片
        # flipped_img = Image.fromarray(flipped_img)
        return flipped_img


def crop_quadrilateral(image, point1, point2, point3, point4):
    """
    截取四边形
    """
    # Create a transparent mask with the same size as the image
    mask = QImage(image.size(), QImage.Format_ARGB32_Premultiplied)
    mask.fill(Qt.transparent)

    # Create a QPainter object and set the drawing device to the mask
    painter = QPainter(mask)

    # Create a QBrush object and set the color to white
    brush = QBrush(QColor(255, 255, 255))

    # Set the QPainter's drawing device to the mask and set the drawing mode to CompositionMode_Source
    painter.setCompositionMode(QPainter.CompositionMode_Source)

    # Draw a quadrilateral mask
    painter.setBrush(brush)
    painter.setPen(Qt.NoPen)
    path = QPainterPath()
    path.moveTo(point1[0], point1[1])  # Define the vertices of the quadrilateral
    path.lineTo(point2[0], point2[1])
    path.lineTo(point3[0], point3[1])
    path.lineTo(point4[0], point4[1])
    path.closeSubpath()
    painter.drawPath(path)

    # Set the QPainter's drawing device to the image and set the drawing mode to CompositionMode_DestinationIn
    painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)

    # Apply the mask to the image
    painter.drawImage(0, 0, image)

    # End the drawing
    painter.end()

    # Return the cropped image
    cropped_image = image.copy()
    cropped_image.setAlphaChannel(mask)
    return cropped_image

def crop_circle(image):
    '''截取圆形图像'''
    # 创建一个与图像大小相同的透明图像
    mask = QImage(image.size(), QImage.Format_ARGB32_Premultiplied)
    mask.fill(Qt.transparent)

    # 创建一个 QPainter 对象，并设置绘制设备为 mask
    painter = QPainter(mask)

    # 创建一个 QBrush 对象，并设置颜色为白色
    brush = QBrush(QColor(255, 255, 255))

    # 设置 QPainter 的绘制设备为 mask，并设置绘制模式为 CompositionMode_Source
    painter.setCompositionMode(QPainter.CompositionMode_Source)

    # 绘制一个圆形掩码
    painter.setBrush(brush)
    painter.setPen(Qt.NoPen)
    painter.drawEllipse(mask.rect())

    # 设置 QPainter 的绘制设备为 image，并设置绘制模式为 CompositionMode_DestinationIn
    painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)

    # 在图像上应用掩码
    painter.drawImage(0, 0, image)

    # 结束绘制
    painter.end()

    # 返回截取的圆形图像
    cropped_image = image.copy()
    cropped_image.setAlphaChannel(mask)

    return cropped_image

def crop_ring( image, scale):
    '''截取圆环图像'''
    # 创建一个与图像大小相同的透明图像
    mask = QImage(image.size(), QImage.Format_ARGB32_Premultiplied)
    mask.fill(Qt.transparent)

    # 创建一个 QPainter 对象，并设置绘制设备为 mask
    painter = QPainter(mask)

    # 创建一个 QBrush 对象，并设置颜色为白色
    brush = QBrush(QColor(255, 255, 255))

    # 设置 QPainter 的绘制设备为 mask，并设置绘制模式为 CompositionMode_Source
    painter.setCompositionMode(QPainter.CompositionMode_Source)

    # 绘制一个外圆形掩码
    outer_radius = min(image.width(), image.height()) / 2
    outer_rect = QRectF(image.width() / 2 - outer_radius, image.height() / 2 - outer_radius, outer_radius * 2,
                        outer_radius * 2)
    painter.setBrush(brush)
    painter.setPen(Qt.NoPen)
    painter.drawEllipse(outer_rect)

    # 绘制一个内圆形掩码
    inner_radius = outer_radius / scale
    inner_rect = QRectF(image.width() / 2 - inner_radius, image.height() / 2 - inner_radius, inner_radius * 2,
                        inner_radius * 2)
    painter.setBrush(Qt.transparent)
    painter.drawEllipse(inner_rect)

    # 设置 QPainter 的绘制设备为 image，并设置绘制模式为 CompositionMode_DestinationIn
    painter.setCompositionMode(QPainter.CompositionMode_DestinationIn)

    # 在图像上应用掩码
    painter.drawImage(0, 0, image)

    # 结束绘制
    painter.end()

    # 返回截取的圆环图像
    cropped_image = image.copy()
    cropped_image.setAlphaChannel(mask)

    return cropped_image

class ImagePro():
    '''图像'''
    def init_Image(self):
        # 创建窗口
        self.window = tk.Tk()
        self.window.title("Image with Text")
        self.window.geometry("800x600")

        # 创建画布
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

        # 设置文字内容和字体
        self.font = ImageFont.truetype('font/simsun.ttc', size=50)
        # 设置文字颜色
        self.text_color = (255, 0, 0)  # 红色
        # 设置文字位置
        self.text_position = (50, 50)

        # # 打开图片对象
        # image = Image.open('back/1.bmp')
        # self.addtext('未开始',image)

    def image_process(self,image_data):
        # 1.图像数据预处理
        temp = np.asarray(image_data)
        # temp = temp.reshape((540, 720, 3))
        return temp

    # 图片添加文字
    def addtext(self,text, data_img):
        # # 打开图片对象
        image = Image.fromarray(data_img)
        # 创建绘图对象
        draw = ImageDraw.Draw(image)
        # 在图片上添加文字
        draw.text(self.text_position, text, font=self.font, fill=self.text_color)
        # 显示图片
        photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo
        # 更新窗口
        self.window.update()
        # 暂停1秒钟
        # time.sleep(1)

    # 保存图像文件
    def saveimg_tofile(self, file_path, data_img):
        # 检查文件夹是否存在，如果不存在则创建
        # if not os.path.exists(file_path):
        #     os.makedirs(file_path)
        # 将图像数据转为图像
        image = Image.fromarray(data_img)
        image.save(file_path)
        return file_path

    def saveimg_tofolder(self, folder_path, data_img):
        # 检查文件夹是否存在，如果不存在则创建
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        else:
            pass
        # # 将RGB图像转换为BGR图像
        # data_img = cv2.cvtColor(data_img, cv2.COLOR_RGB2BGR)
        # 将图像数据转为图像
        image = Image.fromarray(data_img)
        # 获取当前系统时间
        # current_time = datetime.datetime.now()
        # # 格式化时间字符串
        time_string = datetime.now().strftime('%Y-%m-%d-%H-%M-%S.%f')
        # 保存图像文件
        image.save(path_join(folder_path, str(time_string) + '.bmp'))
        # img.save(folder_path + '/' + str(time_string) + '.bmp')
        return path_join(folder_path, str(time_string) + '.bmp')
