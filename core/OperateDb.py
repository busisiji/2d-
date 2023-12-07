from lib.data import convert_JSON
from lib.path import globalsdynamic, Globals


class OperateDb():
    """模块数据库"""
    keys = []
    @classmethod
    def insert_data(cls,table_name,rowid,keys):
        """创建数据库"""
        data = {'id':rowid}
        globalsdynamic.db_child.create_table_primary(table_name, keys, 'id')
        globalsdynamic.db_child.insert_data(table_name, data, 'id')

    @classmethod
    def get_key_index(cls, key):
        return cls.keys.index(key)+1

    @classmethod
    def get_row(cls,table_name,row = None):
        """获取当前打开窗口的行数据"""
        if not row:
            row = Globals.node_index
        results = globalsdynamic.db_child.query_data_table(table_name)
        if not results:
            return []
        indexes = [index for index, value in enumerate(results) if str(value[0]) == str(row)]
        if not indexes:
            return []
        return convert_JSON(results[indexes[0]])

    @classmethod
    def get_column(cls,table_name,column_name):
        """获取当前打开窗口的列数据"""
        result = cls.get_row()
        if result and result[cls.get_key_index(column_name)]:
            model_name = result[cls.get_key_index(column_name)]
            return convert_JSON(model_name)
        return None

    @classmethod
    def add_data(cls,table_name,data):
        """数据库写入"""
        data['id'] = Globals.node_index
        globalsdynamic.db_child.insert_data(table_name, data, 'id')


class DataDb():
    """子项目数据库"""

    keys = []
    table_name = ''

    @classmethod
    def insert_data(cls):
        """创建数据库"""
        globalsdynamic.db_main.create_tables(cls.table_name, cls.keys)

    @classmethod
    def get_names(cls):
        """获取主键列表"""
        results = globalsdynamic.db_main.query_data_table(cls.table_name)
        if not results:
            return []
        names = [str(result[0]) for result in results]
        return names

    @classmethod
    def get_row(cls, name):
        """获取当前名称的行数据"""
        result = globalsdynamic.db_main.query_colum(cls.table_name, name)
        result = result[0] if result else result
        return result

    @classmethod
    def add_data(cls, data):
        globalsdynamic.db_main.insert_data(cls.table_name, data, 'name')

    @classmethod
    def delete_row(cls, rowName):
        """删除行"""
        globalsdynamic.db_main.delete_row_if(cls.table_name, f'name = "{str(rowName)}"')