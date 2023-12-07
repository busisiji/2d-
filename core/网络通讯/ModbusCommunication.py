import time

import modbus_tk.defines as md
import serial
from modbus_tk import modbus_rtu
from modbus_tk import modbus_tcp

def connect_rtu( port='com1', baudrate=9600,bytesize=8,parity='None',stopbits=1,timeout=5):
    """
    # port：串口
    # baudrate：波特率
    # bytesize：字节大小
    # parity：校验位
    # stopbits：停止位
    # timeout：读超时设置
    # writeTimeout：写超时
    # xonxoff：软件流控
    # rtscts：硬件流控
    # dsrdtr：硬件流控
    """
    try:
        if parity == "None":
            parity = serial.PARITY_NONE
        elif parity == "Odd":
            parity = serial.PARITY_ODD
        else:
            parity = serial.PARITY_EVEN

        xonxoff = False  # 软件流控
        dsrdtr = False  # 硬件流控 DTR
        rtscts = False  # 硬件流控 RTS

        master = modbus_rtu.RtuMaster(serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, parity=parity, stopbits=stopbits,xonxoff=xonxoff))
        # master.set_verbose(True)
        master.set_timeout(timeout)
        return master
    except Exception as e:
        print('wrong')
        raise  # 重新引发异常

def connect_tcp(ip='127.0.0.0', port=502, time=5):
    try:
        master = modbus_tcp.TcpMaster(ip, port)
        master.set_timeout(time)
        return master
    except Exception as e:
        print('wrong')

class Plc():
    '''
    功能码                         编号              含义
    READ_COILS                   H01               读线圈
    READ_DISCRETE_INPUTS         H02               读离散输入
    READ_HOLDING_REGISTERS       H03              读保持寄存器
    READ_INPUT_REGISTERS         H04              读输入寄存器（模拟量）
    WRITE_SINGLE_COIL            H05              写单一线圈
    WRITE_SINGLE_REGISTER        H06              写单一寄存器
    WRITE_MULTIPLE_COILS         H15              写多个线圈
    WRITE_MULTIPLE_REGISTERS     H16              写多个寄存器
    '''

    # VERSION 2.0 引入单例模式

    def __init__(self, master):
        self.master = master
        self.fun = {
            'Read(01) 线圈状态' : self.get_01,
            'Read(02) 输入状态' : self.get_02,
            'Read(03) 保持寄存器' : self.get_03,
            'Read(04) 输入寄存器' : self.get_04,
            'Wirte(05) 单线圈' : self.set_05,
            'Wirte(06) 单寄存器' : self.set_06,
            'Wirte(15) 多线圈' : self.set_15,
            'Wirte(16) 多寄存器' : self.set_16,
        }

    def get_01(self, slave=1, adr=0, num=0):  # 读线圈Q区
        db = self.master.execute(slave=slave, function_code=md.READ_COILS, starting_address=adr, quantity_of_x=num)
        return db

    def get_02(self, slave=1, adr=0, num=0):  # 读输入信号
        db = self.master.execute(slave=slave, function_code=md.READ_DISCRETE_INPUTS, starting_address=adr,
                                 quantity_of_x=num)
        return db

    def get_03(self, slave=1, adr=0, num=0):  # 读保持寄存器
        db = self.master.execute(slave=slave, function_code=md.READ_HOLDING_REGISTERS, starting_address=adr,
                                 quantity_of_x=num)
        return db

    def get_04(self, slave=1, adr=0, num=0):  # 读输入寄存器
        db = self.master.execute(slave=slave, function_code=md.READ_INPUT_REGISTERS, starting_address=adr,
                                 quantity_of_x=num)
        return db

    def set_05(self, slave=1, adr=0, value=0):  # 写单个线圈
        db = self.master.execute(slave=slave, function_code=md.WRITE_SINGLE_COIL, starting_address=adr, output_value=value)

    def set_06(self, slave=1, adr=0, value=0):  # 写单个寄存器
        db = self.master.execute(slave=slave, function_code=md.WRITE_SINGLE_REGISTER, starting_address=adr,output_value=value)

    def set_15(self, slave=1, adr=0, value=[]):  # 写多个线圈
        db = self.master.execute(slave=slave, function_code=md.WRITE_MULTIPLE_COILS, starting_address=adr,output_value=value)

    def set_16(self, slave=1, adr=0, value=[]):  # 写多个寄存器
        db = self.master.execute(slave=slave, function_code=md.WRITE_MULTIPLE_REGISTERS, starting_address=adr,output_value=value)

if __name__ == '__main__':
    # master = connect_tcp('192.168.1.47')
    # new_plc = Plc(master)  # 建立一个plc对象
    # print(new_plc.set_06(10,7,9999))

    master = connect_rtu('com8',timeout=1.0)
    new_plc = Plc(master)  # 建立一个plc对象
    print(new_plc.get_03(1, 0, 10))