import sys
import os

import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap

# basedir = os.path.abspath(os.path.dirname(__file__))

basedir1 = os.path.abspath(os.path.join(os.path.dirname("__file__"),"lib"))
basedir2 = os.path.abspath(os.path.join(os.path.dirname("__file__"),"lib","MvImport"))
sys.path.append(basedir1)
sys.path.append(basedir2)
from MvImport.MvCameraControl_class import *

class Camera:
    '''相机'''
    def __init__(self):
        self.g_bExit = True  # 相机是否关闭

    def camera_init(self):
        '''选择相机'''
        camera_list = []
        SDKVersion = MvCamera.MV_CC_GetSDKVersion()
        print("SDKVersion[0x%x]" % SDKVersion)

        self.deviceList = MV_CC_DEVICE_INFO_LIST()
        tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE

        # ch:枚举设备 | en:Enum device
        ret = MvCamera.MV_CC_EnumDevices(tlayerType, self.deviceList)
        if ret != 0:
            print("enum devices fail! ret[0x%x]" % ret)
            # sys.exit()
            return

        if self.deviceList.nDeviceNum == 0:
            print("find no device!")
            # sys.exit()
            return
        print("Find %d devices!" % self.deviceList.nDeviceNum)

        for i in range(0, self.deviceList.nDeviceNum):
            mvcc_dev_info = cast(self.deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
            if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE:
                print("\ngige device: [%d]" % i)
                strModeName = ""
                for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName:
                    strModeName = strModeName + chr(per)
                print("device model name: %s" % strModeName)

                nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
                nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
                nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
                nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
                print("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))
                camera_list.append([strModeName,str(nip1)+'.'+str(nip2)+'.'+str(nip3)+'.'+str(nip4)+'.']) # 相机名称 相机ip
            elif mvcc_dev_info.nTLayerType == MV_USB_DEVICE:
                print("\nu3v device: [%d]" % i)
                strModeName = ""
                for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chModelName:
                    if per == 0:
                        break
                    strModeName = strModeName + chr(per)
                print("device model name: %s" % strModeName)

                strSerialNumber = ""
                for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chSerialNumber:
                    if per == 0:
                        break
                    strSerialNumber = strSerialNumber + chr(per)
                print("user serial number: %s" % strSerialNumber)
        return camera_list


    def run(self,parameters=None):
        '''启动相机'''
        self.g_bExit = False
        # ch:创建相机实例 | en:Creat Camera Object
        self.cam = MvCamera()

        # ch:选择设备并创建句柄| en:Select device and create handle
        stDeviceList = cast(self.deviceList.pDeviceInfo[int(self.nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents

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

        # 关闭自动曝光时间
        ret = self.cam.MV_CC_SetEnumValue("ExposureAuto", MV_EXPOSURE_AUTO_MODE_OFF)
        if ret != 0:
            raise Exception("set ExposureAuto fail! ret[0x%x]" % ret)
        # 自动增益  连续模式
        ret = self.cam.MV_CC_SetEnumValue("GainAuto", MV_GAIN_MODE_CONTINUOUS)
        if ret != 0:
            raise Exception("set GainAuto fail! ret[0x%x]" % ret)
        # 增益值 范围 0 - 23.98dB
        # ret = camera.MV_CC_SetFloatValue("Gain",3)
        # if ret != 0:
        #     raise Exception("set Gain fail! ret[0x%x]" % ret)
        # 设置采集帧率 范围：0.1 - 100000
        ret = self.cam.MV_CC_SetFloatValue("AcquisitionFrameRate", float(50.00))
        if ret != 0:
            raise Exception("Set AcquisitionFrameRate fail! ter[0x%x]" % ret)
        # 设置曝光时间 范围 15 - 9999448
        ret = self.cam.MV_CC_SetFloatValue("ExposureTime", float(800.00))
        if ret != 0:
            raise Exception("Set ExposureTime fail! ter[0x%x]" % ret)
        # 设置自动白平衡
        ret = self.cam.MV_CC_SetEnumValue("BalanceWhiteAuto", 1)
        if ret != 0:
            raise Exception("Set BalanceWhiteAuto fail! ret[0x%x]" % ret)
        # 设置亮度 范围 0 - 255
        ret = self.cam.MV_CC_SetIntValue("Brightness", 80)
        if ret != 0:
            raise Exception("Set Brightness fail! ret[0x%x]" % ret)
        # 设置像素格式
        ret = self.cam.MV_CC_SetEnumValue("PixelFormat", 0x02180014)
        if ret != 0:
            raise Exception("Set PixelFormat fail! ret[0x%x]" % ret)

        # ch:获取数据包大小 | en:Get payload size
        stParam = MVCC_INTVALUE()
        memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

        ret = self.cam.MV_CC_GetIntValue("PayloadSize", stParam)
        if ret != 0:
            print("get payload size fail! ret[0x%x]" % ret)
            sys.exit()
        self.nPayloadSize = stParam.nCurValue

        # ch:开始取流 | en:Start grab image
        ret = self.cam.MV_CC_StartGrabbing()
        if ret != 0:
            print("start grabbing fail! ret[0x%x]" % ret)
            sys.exit()

        self.data_buf = (c_ubyte * self.nPayloadSize)()

        return self.cam, self.data_buf, self.nPayloadSize

    def init_MV(self):
        '''初始化MV_FRAME_OUT_INFO_EX'''
        self.stFrameInfo = MV_FRAME_OUT_INFO_EX()
        memset(byref(self.stFrameInfo), 0, sizeof(self.stFrameInfo))
        return self.stFrameInfo

    def get_Value(self, param_type, node_name):
        """
        :param cam:            相机实例
        :param_type:           获取节点值得类型
        :param node_name:      节点名 可选 int 、float 、enum 、bool 、string 型节点
        :return:               节点值
        """
        if param_type == "int_value":
            stParam = MVCC_INTVALUE_EX()
            memset(byref(stParam), 0, sizeof(MVCC_INTVALUE_EX))
            ret = self.cam.MV_CC_GetIntValueEx(node_name, stParam)
            if ret != 0:
                raise Exception("获取 int 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stParam.nCurValue

        elif param_type == "float_value":
            stFloatValue = MVCC_FLOATVALUE()
            memset(byref(stFloatValue), 0, sizeof(MVCC_FLOATVALUE))
            ret = self.cam.MV_CC_GetFloatValue(node_name, stFloatValue)
            if ret != 0:
                raise Exception("获取 float 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stFloatValue.fCurValue

        elif param_type == "enum_value":
            stEnumValue = MVCC_ENUMVALUE()
            memset(byref(stEnumValue), 0, sizeof(MVCC_ENUMVALUE))
            ret = self.cam.MV_CC_GetEnumValue(node_name, stEnumValue)
            if ret != 0:
                raise Exception("获取 enum 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stEnumValue.nCurValue

        elif param_type == "bool_value":
            stBool = c_bool(False)
            ret = self.cam.MV_CC_GetBoolValue(node_name, stBool)
            if ret != 0:
                raise Exception("获取 bool 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stBool.value

        elif param_type == "string_value":
            stStringValue = MVCC_STRINGVALUE()
            memset(byref(stStringValue), 0, sizeof(MVCC_STRINGVALUE))
            ret = self.cam.MV_CC_GetStringValue(node_name, stStringValue)
            if ret != 0:
                raise Exception("获取 string 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stStringValue.chCurValue

        else:
            return None

    def set_Value(self, param_type, node_name, node_value):
        """
        :param cam:               相机实例
        :param param_type:        需要设置的节点值得类型
            int:
            float:
            enum:     参考于客户端中该选项的 Enum Entry Value 值即可
            bool:     对应 0 为关，1 为开
            string:   输入值为数字或者英文字符，不能为汉字
        :param node_name:         需要设置的节点名
        :param node_value:        设置给节点的值
        :return:
        """
        if param_type == "int_value":
            ret = self.cam.MV_CC_SetIntValueEx(node_name, int(node_value))
            if ret != 0:
                raise Exception("设置 int 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "float_value":
            ret = self.cam.MV_CC_SetFloatValue(node_name, float(node_value))
            if ret != 0:
                raise Exception("设置 float 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "enum_value":
            ret = self.cam.MV_CC_SetEnumValue(node_name, node_value)
            if ret != 0:
                raise Exception("设置 enum 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "bool_value":
            ret = self.cam.MV_CC_SetBoolValue(node_name, node_value)
            if ret != 0:
                raise Exception("设置 bool 型数据节点 %s 失败 ！ 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "string_value":
            ret = self.cam.MV_CC_SetStringValue(node_name, str(node_value))
            if ret != 0:
                raise Exception("设置 string 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

    def set_exposure_time(self, exp_time):
        self.set_Value(param_type="float_value", node_name="ExposureTime", node_value=float(exp_time))

    # 获取曝光时间值
    def get_exposure_time(self):
        return self.get_Value(param_type="float_value", node_name="ExposureTime")

    # 获取自动白平衡 1开启 0关闭
    def get_balance_white_auto(self):
        return self.get_Value(param_type="enum_value", node_name="BalanceWhiteAuto")

    def get_image(self, width=None):
        """
        :param cam:     相机实例
        :active_way:主动取流方式的不同方法 分别是（getImagebuffer）（getoneframetimeout）
        :return:
        """
        ret = self.cam.MV_CC_GetOneFrameTimeout(self.data_buf, self.nPayloadSize, self.stFrameInfo, 1000)
        if ret == 0:
            # image = np.asarray(self.data_buf).reshape((self.stFrameInfo.nHeight, self.stFrameInfo.nWidth, 3))
            image = np.array(self.data_buf)
            image = image.reshape((self.stFrameInfo.nHeight,self.stFrameInfo.nWidth,3))
            # image = np.asarray(self.data_buf).reshape((self.stFrameInfo.nHeight, self.stFrameInfo.nWidth,2))
            # if width is not None:
            #     image = cv2.resize(image, (width, int(self.stFrameInfo.nHeight * width / self.stFrameInfo.nWidth)))
            #     pass
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image
        else:
            return None

    def get_next_image(self):
        '''获取相机的一帧数据并写入MV_FRAME_OUT_INFO_EX中'''
        self.ret = self.cam.MV_CC_GetOneFrameTimeout(self.data_buf, self.nPayloadSize, self.stFrameInfo, 1000)
        if self.ret == 0:
            # print("get one frame: Width[%d], Height[%d], PixelType[0x%x], nFrameNum[%d]" % (
            # self.stFrameInfo.nWidth, self.stFrameInfo.nHeight, self.stFrameInfo.enPixelType, self.stFrameInfo.nFrameNum))
            return self.data_buf
        else:
            print("no data[0x%x]" % self.ret)
            return None

    def get_next_qimage(self):
        image = np.array(self.data_buf)
        image = image.reshape((self.stFrameInfo.nHeight, self.stFrameInfo.nWidth, 3))
        # print(temp)
        # print(temp.shape)
        # QIm = cv2.cvtColor(QIm, cv2.COLOR_BGR2RGB)  # 这一步获取到的颜色不对，因为默认是BRG，要转化成RGB，颜色才正常
        pyrD1 = cv2.pyrDown(image)  # 向下取样
        pyrD2 = cv2.pyrDown(pyrD1)  # 向下取样
        image_height, image_width, image_depth = pyrD2.shape  # 读取图像高宽深度
        pyrD3 = QImage(pyrD2, image_width, image_height, image_width * image_depth, QImage.Format_RGB888)
        return pyrD3

    def show_runtime_info(self, image):
        exp_time = self.get_exposure_time()
        cv2.putText(image, ("exposure time = %1.1fms" % (exp_time * 0.001)), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    255, 1)

    def saveImage(self, filename):
        image = self.get_image()
        cv2.imwrite('./images/' + filename + '.jpg', image)

    def send_camera_num(self):
        '''设置相机索引'''
        while 1:
            connectionNum = input("请输入要连接的相机索引:")
            try:
                input_result = int(connectionNum)
            except:
                continue
            else:
                if input_result >= self.deviceList.nDeviceNum:
                    print("error: 请输入相机列表中的索引！")
                else:
                    break
        return connectionNum

    def close(self):
        '''相机关闭'''
        self.g_bExit = True
        # ch:停止取流 | en:Stop grab image
        ret = self.cam.MV_CC_StopGrabbing()
        if ret != 0:
            print("stop grabbing fail! ret[0x%x]" % ret)
            del self.data_buf
            sys.exit()

        # ch:关闭设备 | Close device
        ret = self.cam.MV_CC_CloseDevice()
        if ret != 0:
            print("close deivce fail! ret[0x%x]" % ret)
            del self.data_buf
            sys.exit()

        # ch:销毁句柄 | Destroy handle
        ret = self.cam.MV_CC_DestroyHandle()
        if ret != 0:
            print("destroy handle fail! ret[0x%x]" % ret)
            del self.data_buf
            sys.exit()

        del self.data_buf

class HKCamera():
    def __init__(self, CameraIdx=0, log_path=None):
        # enumerate all the camera devices
        deviceList = self.enum_devices()
        self.stop_capturing = False

        # generate a camera instance
        self.cam = self.open_camera(deviceList, CameraIdx, log_path)
        self.start_camera()

    def __del__(self):
        # 结束循环取流
        self.stop_capturing = True
        # 关闭cv2窗口
        cv2.destroyAllWindows()
        if self.cam is None:
            return

        # 停止取流
        ret = self.cam.MV_CC_StopGrabbing()
        if ret != 0:
            raise Exception("stop grabbing fail! ret[0x%x]" % ret)

        # 关闭设备
        ret = self.cam.MV_CC_CloseDevice()
        if ret != 0:
            raise Exception("close deivce fail! ret[0x%x]" % ret)

        # 销毁句柄
        ret = self.cam.MV_CC_DestroyHandle()
        if ret != 0:
            raise Exception("destroy handle fail! ret[0x%x]" % ret)

    @staticmethod
    def enum_devices(device=0, device_way=False):
        """
        device = 0  枚举网口、USB口、未知设备、cameralink 设备
        device = 1 枚举GenTL设备
        """
        if device_way == False:
            if device == 0:
                cameraType = MV_GIGE_DEVICE | MV_USB_DEVICE | MV_UNKNOW_DEVICE | MV_1394_DEVICE | MV_CAMERALINK_DEVICE
                deviceList = MV_CC_DEVICE_INFO_LIST()
                # 枚举设备
                ret = MvCamera.MV_CC_EnumDevices(cameraType, deviceList)
                if ret != 0:
                    raise Exception("enum devices fail! ret[0x%x]" % ret)
                return deviceList
            else:
                pass
        elif device_way == True:
            pass

    def open_camera(self, deviceList, CameraIdx, log_path):
        # generate a camera instance
        camera = MvCamera()

        # 选择设备并创建句柄
        stDeviceList = cast(deviceList.pDeviceInfo[CameraIdx], POINTER(MV_CC_DEVICE_INFO)).contents
        if log_path is not None:
            ret = self.cam.MV_CC_SetSDKLogPath(log_path)
            if ret != 0:
                raise Exception("set Log path  fail! ret[0x%x]" % ret)

            # 创建句柄,生成日志
            ret = camera.MV_CC_CreateHandle(stDeviceList)
            if ret != 0:
                raise Exception("create handle fail! ret[0x%x]" % ret)
        else:
            # 创建句柄,不生成日志
            ret = camera.MV_CC_CreateHandleWithoutLog(stDeviceList)
            if ret != 0:
                raise Exception("create handle fail! ret[0x%x]" % ret)
        if ret != 0:
            raise Exception("Set BalanceWhiteAuto faill! ter[0x%x]" % ret)
        # 打开相机
        ret = camera.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != 0:
            raise Exception("open device fail! ret[0x%x]" % ret)
        # # 探测网络最佳包大小（只对GigE相机有效）
        # if stDeviceList.nTLayerType == MV_GIGE_DEVICE:
        #     nPacketSize = camera.MV_CC_GetOptimalPacketSize()
        #     if int(nPacketSize)>0:
        #         ret = camera.MV_CC_SetIntValue("GevSCPSPacketSize",nPacketSize)
        #         if ret != 0:
        #             raise Exception("Warning: Set Packet Size faill! ret[0x%x]" % ret)
        #     else:
        #         raise Exception("Warning: Get Packet Size faill! ret[0x%x]" % nPacketSize)
        # 设置触发模式为off
        ret = camera.MV_CC_SetEnumValue("TriggerMode",MV_TRIGGER_MODE_OFF)
        if ret != 0:
            raise Exception("set TriggerMode fail! ret[0x%x]" % ret)
        # 关闭自动曝光时间
        ret = camera.MV_CC_SetEnumValue("ExposureAuto",MV_EXPOSURE_AUTO_MODE_OFF)
        if ret != 0:
            raise Exception("set ExposureAuto fail! ret[0x%x]" % ret)
        # 自动增益  连续模式
        ret = camera.MV_CC_SetEnumValue("GainAuto",MV_GAIN_MODE_CONTINUOUS)
        if ret != 0:
            raise Exception("set GainAuto fail! ret[0x%x]" % ret)
        # 增益值 范围 0 - 23.98dB
        # ret = camera.MV_CC_SetFloatValue("Gain",3)
        # if ret != 0:
        #     raise Exception("set Gain fail! ret[0x%x]" % ret)
        # 设置采集帧率 范围：0.1 - 100000
        ret = camera.MV_CC_SetFloatValue("AcquisitionFrameRate", float(50.00))
        if ret != 0:
            raise Exception("Set AcquisitionFrameRate fail! ter[0x%x]" % ret)
        # 设置曝光时间 范围 15 - 9999448
        ret = camera.MV_CC_SetFloatValue("ExposureTime", float(800.00))
        if ret != 0:
            raise Exception("Set ExposureTime fail! ter[0x%x]" % ret)
        # 设置自动白平衡
        ret = camera.MV_CC_SetEnumValue("BalanceWhiteAuto", 1)
        if ret !=0:
            raise Exception("Set BalanceWhiteAuto fail! ret[0x%x]" % ret)
        # 设置亮度 范围 0 - 255
        ret = camera.MV_CC_SetIntValue("Brightness", 80)
        if ret != 0:
            raise Exception("Set Brightness fail! ret[0x%x]" % ret)
        # 设置像素格式
        ret = camera.MV_CC_SetEnumValue("PixelFormat", 0x02180014)
        if ret != 0:
            raise Exception("Set PixelFormat fail! ret[0x%x]" % ret)

        return camera

    def start_camera(self):
        stParam = MVCC_INTVALUE()
        memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

        ret = self.cam.MV_CC_GetIntValue("PayloadSize", stParam)
        if ret != 0:
            raise Exception("get payload size fail! ret[0x%x]" % ret)

        self.nPayloadSize = stParam.nCurValue
        self.data_buf = (c_ubyte * self.nPayloadSize)()
        self.stFrameInfo = MV_FRAME_OUT_INFO_EX()
        memset(byref(self.stFrameInfo), 0, sizeof(self.stFrameInfo))

        self.cam.MV_CC_StartGrabbing()

    def get_Value(self, param_type, node_name):
        """
        :param cam:            相机实例
        :param_type:           获取节点值得类型
        :param node_name:      节点名 可选 int 、float 、enum 、bool 、string 型节点
        :return:               节点值
        """
        if param_type == "int_value":
            stParam = MVCC_INTVALUE_EX()
            memset(byref(stParam), 0, sizeof(MVCC_INTVALUE_EX))
            ret = self.cam.MV_CC_GetIntValueEx(node_name, stParam)
            if ret != 0:
                raise Exception("获取 int 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stParam.nCurValue

        elif param_type == "float_value":
            stFloatValue = MVCC_FLOATVALUE()
            memset(byref(stFloatValue), 0, sizeof(MVCC_FLOATVALUE))
            ret = self.cam.MV_CC_GetFloatValue(node_name, stFloatValue)
            if ret != 0:
                raise Exception("获取 float 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stFloatValue.fCurValue

        elif param_type == "enum_value":
            stEnumValue = MVCC_ENUMVALUE()
            memset(byref(stEnumValue), 0, sizeof(MVCC_ENUMVALUE))
            ret = self.cam.MV_CC_GetEnumValue(node_name, stEnumValue)
            if ret != 0:
                raise Exception("获取 enum 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stEnumValue.nCurValue

        elif param_type == "bool_value":
            stBool = c_bool(False)
            ret = self.cam.MV_CC_GetBoolValue(node_name, stBool)
            if ret != 0:
                raise Exception("获取 bool 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stBool.value

        elif param_type == "string_value":
            stStringValue = MVCC_STRINGVALUE()
            memset(byref(stStringValue), 0, sizeof(MVCC_STRINGVALUE))
            ret = self.cam.MV_CC_GetStringValue(node_name, stStringValue)
            if ret != 0:
                raise Exception("获取 string 型数据 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))
            return stStringValue.chCurValue

        else:
            return None

    def set_Value(self, param_type, node_name, node_value):
        """
        :param cam:               相机实例
        :param param_type:        需要设置的节点值得类型
            int:
            float:
            enum:     参考于客户端中该选项的 Enum Entry Value 值即可
            bool:     对应 0 为关，1 为开
            string:   输入值为数字或者英文字符，不能为汉字
        :param node_name:         需要设置的节点名
        :param node_value:        设置给节点的值
        :return:
        """
        if param_type == "int_value":
            ret = self.cam.MV_CC_SetIntValueEx(node_name, int(node_value))
            if ret != 0:
                raise Exception("设置 int 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "float_value":
            ret = self.cam.MV_CC_SetFloatValue(node_name, float(node_value))
            if ret != 0:
                raise Exception("设置 float 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "enum_value":
            ret = self.cam.MV_CC_SetEnumValue(node_name, node_value)
            if ret != 0:
                raise Exception("设置 enum 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "bool_value":
            ret = self.cam.MV_CC_SetBoolValue(node_name, node_value)
            if ret != 0:
                raise Exception("设置 bool 型数据节点 %s 失败 ！ 报错码 ret[0x%x]" % (node_name, ret))

        elif param_type == "string_value":
            ret = self.cam.MV_CC_SetStringValue(node_name, str(node_value))
            if ret != 0:
                raise Exception("设置 string 型数据节点 %s 失败 ! 报错码 ret[0x%x]" % (node_name, ret))

    def set_exposure_time(self, exp_time):
        self.set_Value(param_type="float_value", node_name="ExposureTime", node_value=float(exp_time))

    # 获取曝光时间值
    def get_exposure_time(self):
        return self.get_Value(param_type="float_value", node_name="ExposureTime")

    # 获取自动白平衡 1开启 0关闭
    def get_balance_white_auto(self):
        return self.get_Value(param_type="enum_value", node_name="BalanceWhiteAuto")

    def get_image(self, width=None):
        """
        :param cam:     相机实例
        :active_way:主动取流方式的不同方法 分别是（getImagebuffer）（getoneframetimeout）
        :return:
        """
        ret = self.cam.MV_CC_GetOneFrameTimeout(self.data_buf, self.nPayloadSize, self.stFrameInfo, 1000)
        if ret == 0:
            # image = np.asarray(self.data_buf).reshape((self.stFrameInfo.nHeight, self.stFrameInfo.nWidth, 3))
            image = np.array(self.data_buf)
            image = image.reshape((self.stFrameInfo.nHeight,self.stFrameInfo.nWidth,3))
            # image = np.asarray(self.data_buf).reshape((self.stFrameInfo.nHeight, self.stFrameInfo.nWidth,2))
            if width is not None:
                image = cv2.resize(image, (width, int(self.stFrameInfo.nHeight * width / self.stFrameInfo.nWidth)))
                pass
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            return image
        else:
            return None

    def show_runtime_info(self, image):
        exp_time = self.get_exposure_time()
        cv2.putText(image, ("exposure time = %1.1fms" % (exp_time * 0.001)), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1)

    def saveImage(self,filename):
        image = self.get_image()
        cv2.imwrite('./images/'+filename+'.jpg',image)

    def start(self):
        # while not self.stop_capturing:
        #  image = camera.get_image(width=800)
        #  if image is not None:
        #      camera.show_runtime_info(image)
        #      cv2.imshow("", image)
        try:

            while True:
                image = self.get_image(width=800)
                if image is not None:
                    self.show_runtime_info(image)
                    cv2.imshow("", image)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q') or key == ord('Q'):
                    cv2.destroyAllWindows()
                    break
        except Exception as e:
            print(e)

if __name__ == '__main__':

    camera = HKCamera()
    # camera.saveImage()
    print(camera.get_exposure_time())
    # camera.set_exposure_time(1234)
    # 42715.0
    print(camera.get_balance_white_auto())
    # camera.set_exposure_time(5000.0)
    camera.start()
    # try:
    #
    #     while True:
    #      image = camera.get_image(width=800)
    #      if image is not None:
    #          camera.show_runtime_info(image)
    #          cv2.imshow("", image)
    #      key = cv2.waitKey(1) & 0xFF
    #      if key == ord('q') or key == ord('Q'):
    #          cv2.destroyAllWindows()
    #          break
    # except Exception as e:
    #     print(e)