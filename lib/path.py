import json
import os

from PyQt5.QtWidgets import QApplication

from lib.db import DB


def get_project_root():
    '''获取项目根目录'''
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def path_join(path1,path2):
    '''路径合并'''
    return os.path.join(path1, path2)

def path_join_path_project(path):
    """与项目根目录合并"""
    return path_join(Globals.project_path,path)

def get_file_name(folder_path):
    '''遍历目录，获取文件名'''
    if os.path.exists(folder_path):
        return os.listdir(folder_path)
    else:
        print("目录不存在:", folder_path)


def get_item_file_name(row,value):
    '''
    根据项目文件的命名格式获取项目文件名

    :param row: 项目序号
    :param value: 项目名
    :return: 项目文件名
    '''
    data_path = path_join(get_project_root(), 'data')  # 项目文件存储路径
    return path_join(data_path,'项目' + str(row) + '：' + str(value))

class Globals:
    '''静态路径'''
    project_path = get_project_root() # 项目根路径
    datas_path = path_join(project_path, 'data')  # 项目文件存储路径
    db_main_path = path_join(project_path, 'main.db') # 主数据库存储路径
    filename = path_join(project_path, 'log/example.log') # log文件存储路径
    temporarily_path = path_join(project_path, 'temporary') # 临时文件存储路径
    black_image_path = path_join(temporarily_path, "black_image.jpg") # 全黑图片临时存储路径
    color_image_path = path_join(temporarily_path, 'color.jpg')  # 要识别颜色的图片临时存储路径
    types = ["数值","字符","点","图像"] # 数据类型
    node_index = 1 # 打开的参数窗口是第几个流程
    isSignalSlotConnection = {'模板匹配':False,'颜色识别':False} # close()不会断开信号，只连接一次就行，不然会重复触发
    toname = {'模板匹配':'ShapTemplateMatching','颜色识别':'ColorRecognitionTable',
              '数据转换':'QsciScintilla','数据合并':'Poole','数据拆分':'Split','网络通讯':'ModbusName',
              '坐标标定':'CCName','自定义输出':'Output'} # 图名-表名
    nodekeys = ['title', 'types', 'texts', 'icons', 'parameters',
                     'boxs']  # 图元名 图元标题 是输入节点还是输出节点  连接的图元输入节点 连接的图元输出节点
    timeout = 10 # 模块超时时间 s

    screenheight = 1920
    screenwidth = 1080
    # temp_suffix = 'jpg' # 样板图像的后缀
    # temp_path = '' # 样板图像的路径img_path = 's'
    db_main = DB(db_main_path) # 主数据库



class GlobalsDynamic():
    '''动态路径'''
    def __init__(self):
        self.update_main_path()

    def update_data_path(self):
        """更新项目路径"""
        self.row = Globals.db_main.execute_sql("SELECT DISTINCT row FROM Now")[0][0] if Globals.db_main.execute_sql(
            "SELECT DISTINCT row FROM Now") else ''  # 当前项目索引
        self.value = Globals.db_main.execute_sql("SELECT DISTINCT value FROM Now")[0][0] if Globals.db_main.execute_sql(
            "SELECT DISTINCT value FROM Now") else ''  # 当前项目名称
        self.project_data_path = path_join(Globals.datas_path, self.value) if self.value else ''  # 当前项目文件路径
        self.db_data_path = path_join(self.project_data_path, 'database.db') if os.path.exists(
            self.project_data_path) else ''  # 数据库存储路径
        self.db_main = DB(self.db_data_path) if os.path.exists(self.project_data_path) else ''  # 项目数据数据库存储路径

    def update_child_data_path(self):
        """更新子项目路径"""
        self.child = Globals.db_main.execute_sql("SELECT DISTINCT child FROM Now")[0][0] if Globals.db_main.execute_sql(
            "SELECT DISTINCT child FROM Now") else ''  # 当前子项目名称
        if self.child:
            self.data_path = path_join(self.project_data_path, self.child) if os.path.exists(self.project_data_path) else '' # 当前子项目文件路径
            if self.data_path and not os.path.exists(self.data_path):
                os.makedirs(self.data_path)
            self.db_data_path = path_join(self.data_path, 'database.db') if os.path.exists(self.data_path) else '' # 数据库存储路径
            self.db_child = DB(self.db_data_path)# 子项目数据数据库存储路径
        else:
            self.db_child = None # 子项目数据数据库存储路径

    def update_mlpmodle_path(self):
        """更新颜色识别模型存储路径"""
        self.mlpmodle_path = path_join(self.data_path, 'color.mlp')
    def update_temp(self):
        """更新样板路径与后缀名"""
        if self.db_main:
            sql = f"SELECT temppath FROM ImageCapture WHERE name = '{self.child}'"
            self.temp_path = self.db_main.execute_sql(sql)
            self.temp_path = self.db_main.execute_sql(sql)[0][0] if self.temp_path else ''
            # path_join(self.data_path, 'temp.jpg')
            self.temp_suffix = self.temp_path.split('.')[-1] if self.temp_path and os.path.exists(
                self.temp_path) else 'jpg'  # 样板图像的后缀
            # self.temp_halcon_path = self.temp_path.split('temp')[0] + 'temp_halcon.' + self.temp_suffix if self.temp_path else ''
            self.temp_halcon_path = self.temp_path
        else:
            self.temp_path = ''
            self.temp_suffix = 'jpg'
            self.temp_halcon_path = ''

        if '2d-' in self.temp_path:
            self.temp_path = self.temp_path.split('2d-\\')[-1]
        print(self.temp_path)


    def update_main_path(self):
        self.update_data_path()
        self.update_child_data_path()
        self.update_mlpmodle_path()
        self.update_temp()


def getPath(path):
    """
    获取项目路径
    @return:
    """
    return path_join(Globals.project_path,path)

globalsdynamic = GlobalsDynamic()
