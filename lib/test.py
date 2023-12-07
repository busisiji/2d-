# -- coding: utf-8 --
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import *
import numpy as np

# from CameraControl_header import MV_CC_DEVICE_INFO_LIST
# from mainWindow import Ui_MainWindow  # 导入创建的GUI类
import sys
import threading
import msvcrt
from ctypes import *

sys.path.append("./MvImport")
from MvCameraControl_class import *
from Ui_MainWindow import *
from CameraParams_header import *


class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):
    sendAddDeviceName = pyqtSignal()  # 定义一个添加设备列表的信号。
    deviceList = MV_CC_DEVICE_INFO_LIST()
    g_bExit = False
    # ch:创建相机实例 | en:Creat Camera Object
    cam = MvCamera()

    def connect_and_emit_sendAddDeviceName(self):
        # Connect the sendAddDeviceName signal to a slot.
        self.sendAddDeviceName.connect(self.SelectDevice)
        # Emit the signal.
        self.sendAddDeviceName.emit()

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        self.connect_and_emit_sendAddDeviceName()
        self.butopenCam.clicked.connect(lambda: self.openCam(self.camSelect.currentData()))
        self.butcloseCam.clicked.connect(self.closeCam)

        # setting main window geometry
        desktop_geometry = QtWidgets.QApplication.desktop()  # 获取屏幕大小
        main_window_width = desktop_geometry.width()  # 屏幕的宽
        main_window_height = desktop_geometry.height()  # 屏幕的高
        rect = self.geometry()  # 获取窗口界面大小
        window_width = rect.width()  # 窗口界面的宽
        window_height = rect.height()  # 窗口界面的高
        x = (main_window_width - window_width) // 2  # 计算窗口左上角点横坐标
        y = (main_window_height - window_height) // 2  # 计算窗口左上角点纵坐标
        self.setGeometry(x, y, window_width, window_height)  # 设置窗口界面在屏幕上的位置
        # 无边框以及背景透明一般不会在主窗口中用到，一般使用在子窗口中，例如在子窗口中显示gif提示载入信息等等

    # self.setWindowFlags(Qt.FramelessWindowHint)
    # self.setAttribute(Qt.WA_TranslucentBackground)

    # 打开摄像头。
    def openCam(self, camid):
        self.g_bExit = False
        # ch:选择设备并创建句柄 | en:Select device and create handle
        stDeviceList = cast(self.deviceList.pDeviceInfo[int(camid)], POINTER(MV_CC_DEVICE_INFO)).contents
        ret = self.cam.MV_CC_CreateHandle(stDeviceList)
        if ret != 0:
            print("create handle fail! ret[0x%x]" % ret)
            sys.exit()
        # ch:打开设备 | en:Open device

        ret = self.cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != 0:
            print("open device fail! ret[0x%x]" % ret)
            sys.exit()

        # ch:探测网络最佳包大小(只对GigE相机有效) | en:Detection network optimal package size(It only works for the GigE camera)
        if stDeviceList.nTLayerType == MV_GIGE_DEVICE:
            nPacketSize = self.cam.MV_CC_GetOptimalPacketSize()
            if int(nPacketSize) > 0:
                ret = self.cam.MV_CC_SetIntValue("GevSCPSPacketSize", nPacketSize)
                if ret != 0:
                    print("Warning: Set Packet Size fail! ret[0x%x]" % ret)
            else:
                print("Warning: Get Packet Size fail! ret[0x%x]" % nPacketSize)

        # ch:设置触发模式为off | en:Set trigger mode as off
        ret = self.cam.MV_CC_SetEnumValue("TriggerMode", MV_TRIGGER_MODE_OFF)
        if ret != 0:
            print("set trigger mode fail! ret[0x%x]" % ret)
            sys.exit()
            # ch:获取数据包大小 | en:Get payload size
        stParam = MVCC_INTVALUE()
        memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

        ret = self.cam.MV_CC_GetIntValue("PayloadSize", stParam)
        if ret != 0:
            print("get payload size fail! ret[0x%x]" % ret)
            sys.exit()
        nPayloadSize = stParam.nCurValue

        # ch:开始取流 | en:Start grab image
        ret = self.cam.MV_CC_StartGrabbing()
        if ret != 0:
            print("start grabbing fail! ret[0x%x]" % ret)
            sys.exit()

        data_buf = (c_ubyte * nPayloadSize)()

        try:
            hThreadHandle = threading.Thread(target=self.work_thread, args=(self.cam, data_buf, nPayloadSize))
            hThreadHandle.start()
        except:
            print("error: unable to start thread")

    # 关闭相机
    def closeCam(self):
        self.g_bExit = True
        # ch:停止取流 | en:Stop grab image
        ret = self.cam.MV_CC_StopGrabbing()
        if ret != 0:
            print("stop grabbing fail! ret[0x%x]" % ret)
            sys.exit()

        # ch:关闭设备 | Close device
        ret = self.cam.MV_CC_CloseDevice()
        if ret != 0:
            print("close deivce fail! ret[0x%x]" % ret)

        # ch:销毁句柄 | Destroy handle
        ret = self.cam.MV_CC_DestroyHandle()
        if ret != 0:
            print("destroy handle fail! ret[0x%x]" % ret)

    def work_thread(self, cam=0, pData=0, nDataSize=0):
        stFrameInfo = MV_FRAME_OUT_INFO_EX()
        memset(byref(stFrameInfo), 0, sizeof(stFrameInfo))
        while True:
            QIm = np.asarray(pData)  # 将c_ubyte_Array转化成ndarray得到（3686400，）
            QIm = QIm.reshape((540, 720, 3))  # 根据自己分辨率进行转化
            # print(temp)
            # print(temp.shape)
            # QIm = cv2.cvtColor(QIm, cv2.COLOR_BGR2RGB)  # 这一步获取到的颜色不对，因为默认是BRG，要转化成RGB，颜色才正常
            pyrD1 = cv2.pyrDown(QIm)  # 向下取样
            pyrD2 = cv2.pyrDown(pyrD1)  # 向下取样
            image_height, image_width, image_depth = pyrD2.shape  # 读取图像高宽深度
            pyrD3 = QImage(pyrD2, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
            self.label.setPixmap(QPixmap.fromImage(pyrD3))
            # cv2.namedWindow("result", cv2.WINDOW_AUTOSIZE)
            # cv2.imshow("result", temp)
            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break

            ret = cam.MV_CC_GetOneFrameTimeout(pData, nDataSize, stFrameInfo, 1000)
            if ret == 0:
                print("get one frame: Width[%d], Height[%d], nFrameNum[%d]" % (
                    stFrameInfo.nWidth, stFrameInfo.nHeight, stFrameInfo.nFrameNum))
            else:
                print("no data[0x%x]" % ret)
            if self.g_bExit == True:
                del pData
                break

    # 获得所有相机的列表存入cmbSelectDevice中
    def SelectDevice(self):
        '''选择所有能用的相机到列表中，
             gige相机需要配合 sdk 得到。
        '''
        # 得到相机列表

        tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE
        # ch:枚举设备 | en:Enum device
        ret = MvCamera.MV_CC_EnumDevices(tlayerType, self.deviceList)
        if ret != 0:
            print("enum devices fail! ret[0x%x]" % ret)
            sys.exit()
        if self.deviceList.nDeviceNum == 0:
            print("find no device!")
            sys.exit()

        print("Find %d devices!" % self.deviceList.nDeviceNum)
        for i in range(0, self.deviceList.nDeviceNum):
            mvcc_dev_info = cast(self.deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
            if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE:
                print("\ngige device: [%d]" % i)
                strModeName = ""
                for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName:
                    strModeName = strModeName + chr(per)
                print("device model name: %s" % strModeName)
                self.camSelect.addItem(strModeName, i)  # 写入设备列表。

    def pushbutton_function(self):
        # do some things
        Img = cv2.imread('JP1.JPG')  # 通过opencv读入一张图片
        image_height, image_width, image_depth = Img.shape  # 读取图像高宽深度
        QIm = cv2.cvtColor(Img, cv2.COLOR_BGR2RGB)
        QIm = QImage(QIm.data, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
        self.label.setPixmap(QPixmap.fromImage(QIm))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())