import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pylab as plt

"""图像预处理"""


# 缩放
# 灰度化
# 二值化-otsu,自定义，自适应
# 均值滤波
# 中值滤波
# 自定义滤波
# 高斯/双倍滤波
# 开/闭运算
# 图片展示

class ImagePreprocessing:
    def __init__(self, img):
        self.img = img

    ##缩放
    def resizefigure(self, reshape=(0, 0)):
        new_img1 = cv2.resize(self.img, reshape, interpolation=cv2.INTER_AREA)
        self.img = new_img1
        return new_img1

    ##灰度化
    def gray(self):
        grayImage = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img = grayImage
        return grayImage

    ##均值滤波
    def blur_img(self):
        # （1, 15）是垂直方向模糊，（15， 1）是水平方向模糊
        dst = cv2.blur(self.img, (1, 15))
        self.img = dst
        return dst

    ##中值滤波
    def median_blur_img(self):
        dst = cv2.medianBlur(self.img, 5)
        self.img = dst
        return dst

    # 自定义滤波
    def custom_blur_img(self):
        # 36是防止数值溢出
        kernel = np.ones((6, 6), np.float32) / 36
        dst = cv2.filter2D(self.img, -1, kernel)
        self.img = dst
        return dst

    # 高斯滤波
    def gauss_blur_img(self):
        img_gauss_blur = cv2.GaussianBlur(self.img, (3, 3), 0)
        self.img = img_gauss_blur
        return img_gauss_blur

    # 双边滤波
    def bilateral_blur_img(self):
        img_bliteral_blur = cv2.bilateralFilter(self.img, 9, 20, 45)
        self.img = img_bliteral_blur
        return img_bliteral_blur

    # 开/闭运算
    def open_close(self, open=True):
        kernel = np.ones((3, 3), dtype=np.uint8)
        if open:
            dst = cv2.morphologyEx(self.img, cv2.MORPH_OPEN, kernel)
        else:
            dst = cv2.morphologyEx(self.img, cv2.MORPH_CLOSE, kernel)
        self.img = dst
        return dst

    # otsu二值化
    def otsu_th(self):
        # ret2, th2 = cv2.threshold(self.img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # 先使用一个 5x5 的高斯核除去噪音，然后再使用 Otsu 二值化
        blur = cv2.GaussianBlur(self.img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # print(ret2)
        self.img = th3
        return th3

    # 自适应二值化
    def adap_th(self):
        adaptive_threshold_img = cv2.adaptiveThreshold(self.img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                                       35, 3)
        self.img = adaptive_threshold_img
        return adaptive_threshold_img

    # 自定义二值化
    def self_th(self):
        ret, thresh1 = cv2.threshold(self.img, 180, 255, cv2.THRESH_BINARY)
        self.img = thresh1
        return thresh1

    ##图片展示
    def show(self):
        cv2.imshow('new_img', self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    # orc_img_path = "./data"
    #
    # img_paths = os.listdir('../1.jpg')
    # for img_path in img_paths:=
        img = cv2.imread('..' + "/" + '1.jpg')
        print(img.shape)

        fp = ImagePreprocessing(img)
        fp.show()
        if img.shape[1] < 200:
            fp.resizefigure(reshape=(460, 460))
        # fp.custom_blur_img()
        # fp.median_blur_img()
        # fp.gauss_blur_img()
        # fp.adap_th()
        # fp.gauss_blur_img()

        graimg = fp.gray()
        # fp.adap_th()
        # fp.self_th()
        # plt.hist(graimg.ravel(), 256, [0, 256])
        # plt.show()
        fp.open_close(open=True)
        fp.show()

        # break