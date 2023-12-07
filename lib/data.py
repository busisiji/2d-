import json


def adapt_JSON(data):
    """序列号列表"""
    if  isinstance(data, list) or isinstance(data, dict):
        return json.dumps(data).encode('utf8')
    else:
        return data

def convert_JSON(data):
    """反序列化"""
    if isinstance(data, list):
        new_data = []
        for i in data:
            new_data.append(convert_JSON(i))
        return new_data
    if isinstance(data, tuple):
        new_data = []
        for i in data:
            new_data.append(convert_JSON(i))
        return tuple(new_data)
    if isinstance(data,dict):
        for item in data:
            data[item] = convert_JSON(data[item])
        return data
    if not data or not isinstance(data,bytes):
        return data
    return json.loads(data.decode('utf8'))

def update_dict_key(dictionary,num_compare,num_add):
    """修改字典的键"""
    for key in list(dictionary.keys()):
        if key > num_compare:
            new_key = key + num_add
            dictionary[new_key] = dictionary.pop(key)

    return  dictionary

def Merge(dict1, dict2):
    """字典合并"""
    return(dict2.update(dict1))