from core.OperateDb import OperateDb
from lib.data import update_dict_key, convert_JSON
from lib.path import globalsdynamic, Globals


class STMOperateDb(OperateDb):
    data = {'template_paths': {}}
    # 模板图像路径，模板名称，模型路径，匹配参数，输出参数,模板类型
    keys = ['template_paths', 'template_names', 'modelName', 'parameters', 'output', 'type_selects']
    table_name = Globals.toname['模板匹配']

    @classmethod
    def insert_data(cls, rowid):
        super().insert_data(cls.table_name,rowid, cls.keys)
        """创建数据库"""

    @classmethod
    def get_row(cls):
        return super().get_row(cls.table_name)

    @classmethod
    def get_column(cls,column_name):
        return super().get_column(cls.table_name,column_name)

    @classmethod
    def add_data(cls, data):
        super().add_data(cls.table_name, data)

    @classmethod
    def add_module(cls,currentRow,data,name='template_paths'):
        """数据库写入模块"""
        cls.data = {}
        cls.data['id'] = Globals.node_index
        cls.data[name] = {}
        # 加上之前数据
        result = cls.get_row()
        if result and result[cls.get_key_index('template_paths')]:
            cls.data.update(convert_JSON(result[cls.get_key_index('template_paths')]))

        cls.data[name][currentRow] = data
        globalsdynamic.db_child.insert_data(cls.table_name, cls.data, 'id')
    @classmethod
    def delete_module(cls, currentRow,name='template_paths'):
        """数据库删除模块"""
        result = cls.get_row()
        if not result:
            return
        paths = convert_JSON(result[cls.keys.index(name)+1])
        paths = {int(key): value for key, value in paths.items()}  # 将字典的键全部转换为数字类型
        if currentRow in paths:
            del paths[currentRow]
        paths = update_dict_key(paths, currentRow, -1)
        globalsdynamic.db_child.insert_data(cls.table_name,
                                            {'id': Globals.node_index, name: paths}, 'id')

    @classmethod
    def delete_allmodule(cls):
        """数据库清空模块"""
        globalsdynamic.db_child.insert_data(cls.table_name,
                                            {'id': Globals.node_index, 'template_paths': None}, 'id')

