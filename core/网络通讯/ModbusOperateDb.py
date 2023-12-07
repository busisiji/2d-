from core.OperateDb import OperateDb, DataDb
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

class ModbusOperateDb(DataDb):
    """保存的参数表"""
    keys = ['name','port', 'mode','time','operation','SlaveID','address',
            'tcpIP','tcpPort','comPort','comBaudRate','comNum','comStop','comVerify',
            'readFun','readNum','writeFun','writeTarget',
            'numType','numFormat',]
    data = {}
    table_name = 'ModbusData'
    # @classmethod
    # def insert_data(cls):
    #     """创建数据库"""
    #     globalsdynamic.db_main.create_tables(cls.table_name, cls.keys)
    #
    # @classmethod
    # def get_names(cls):
    #     """获取主键列表"""
    #     results = globalsdynamic.db_main.query_data_table(cls.table_name)
    #     if not results:
    #         return []
    #     names = [str(result[0]) for result in results]
    #     return names
    #
    # @classmethod
    # def get_row(cls, name):
    #     """获取当前名称的行数据"""
    #     result = globalsdynamic.db_main.query_colum(cls.table_name, name)
    #     result = result[0] if result else result
    #     return result
    #
    # @classmethod
    # def add_data(cls, data):
    #     globalsdynamic.db_main.insert_data(cls.table_name, data, 'name')
    #
    # @classmethod
    # def delete_row(cls,rowName):
    #     """删除行"""
    #     globalsdynamic.db_main.delete_row_if(cls.table_name,f'name = "{str(rowName)}"')