from PyQt5.QtCore import pyqtSignal

from core.MyClass import MyTableWidget
from lib.path import Globals, globalsdynamic
from core.OperateDb import OperateDb


class OutputOperateDb(OperateDb):
    data = {}
    keys = ['types', 'texts']
    table_name = Globals.toname['自定义输出']

    @classmethod
    def insert_data(cls, rowid):
        super().insert_data(cls.table_name, rowid, cls.keys)
        """创建数据库"""
    @classmethod
    def get_row(cls):
        return super().get_row(cls.table_name)

    @classmethod
    def add_data(cls, data):
        super().add_data(cls.table_name, data)
