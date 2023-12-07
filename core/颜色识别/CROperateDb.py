from lib.path import Globals, globalsdynamic
from core.OperateDb import OperateDb

class CROperateDb(OperateDb):
    data = {'id':0,'name':[], 'text':[], 'scale':0}
    keys = ['name', 'text', 'scale', 'temppath','num','modelName']
    table_name = Globals.toname['颜色识别']

    @classmethod
    def insert_data(cls, rowid):
        super().insert_data(cls.table_name, rowid, cls.keys)
        """创建数据库"""

    @classmethod
    def get_row(cls):
        return super().get_row(cls.table_name)

    @classmethod
    def add_data(cls, data):
        super().add_data(cls.table_name,data)

    @classmethod
    def add_table(cls, table_data_column0, table_data_column1,scale):
        """数据库写入颜色表格"""
        rowid = Globals.node_index
        cls.data['id'] = rowid
        cls.data['name'] = table_data_column0
        cls.data['text'] = table_data_column1
        cls.data['scale'] = scale
        globalsdynamic.db_child.insert_data(cls.table_name, cls.data, 'id')

    @classmethod
    def delete_table_row(cls,currentRow):
        """数据库删除列表行"""
        result = cls.get_row()
        if not result:
            return
        rowid = Globals.node_index
        cls.data['id'] = rowid
        cls.data['name'] = result[1]
        cls.data['text'] = result[2]
        cls.data['name'] = eval(cls.data['name']) if cls.data['name'] else []
        cls.data['text'] = eval(cls.data['text']) if cls.data['text'] else []
        if currentRow < len(cls.data['name']):
            del cls.data['name'][currentRow]
        if currentRow < len(cls.data['text']):
            del cls.data['text'][currentRow]
        globalsdynamic.db_child.insert_data(cls.table_name, cls.data, 'id')

