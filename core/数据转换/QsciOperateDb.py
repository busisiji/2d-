from core.OperateDb import OperateDb
from lib.data import update_dict_key
from lib.path import globalsdynamic, Globals


class ModbusNameDb(OperateDb):
    """保存的模块使用的参数表表名"""
    keys = ['name']
    data = {}
    table_name = 'ModbusName'
    @classmethod
    def insert_data(cls, rowid):
        super().insert_data(cls.table_name, rowid, cls.keys)
        """创建数据库"""

    @classmethod
    def get_row(cls):
        return super().get_row(cls.table_name)

    @classmethod
    def get_column(cls, column_name):
        return super().get_column(cls.table_name, column_name)

    @classmethod
    def add_data(cls, data):
        super().add_data(cls.table_name, data)


class QsciOperateDb(OperateDb):
    keys = [ 'inputType', 'inputName', 'outputType', 'outputName', 'textPy', 'textVBS','type']
    data = {'id','inputType', 'inputName', 'outputType', 'outputName', 'textPy', 'textVBS','type'}
    table_name = Globals.toname['数据转换']

    @classmethod
    def insert_data(cls, rowid):
        super().insert_data(cls.table_name,rowid, cls.keys)
        """创建数据库"""

    @classmethod
    def get_row(cls):
        return super().get_row(cls.table_name)

    @classmethod
    def add_data(cls, data):
        super().add_data(cls.table_name, data)

    @classmethod
    def delete_table_row(cls, currentRow,name,type_name):
        """数据库删除列表行"""
        data = {}
        result = cls.get_row()
        if not result:
            return
        rowid = Globals.node_index
        data['id'] = rowid
        data[name] = result[cls.keys.index(name)+1]
        data[type_name] = result[cls.keys.index(type_name)+1]
        data[name] = eval(data[name]) if data[name] else []
        data[type_name] = eval(data[type_name]) if data[type_name] else []
        if currentRow < len(data[name]):
            del data[name][currentRow]
        if currentRow < len(data[type_name]):
            del data[type_name][currentRow]

        globalsdynamic.db_child.insert_data(cls.table_name, data, 'id')

    @classmethod
    def clear_table_row(cls,type):
        """数据库清空输入输出参数"""
        if type == 'input':
            data = {'id':0,'inputType':[], 'inputName':[]}
        elif type == 'output':
            data = {'id':0,'outputType':[], 'outputName':[]}
        result = cls.get_row()
        if not result:
            return
        rowid = Globals.node_index
        data['id'] = rowid

        globalsdynamic.db_child.insert_data(cls.table_name, data, 'id')