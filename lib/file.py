import json
import os
import shutil

from PIL import Image

from lib.path import get_project_root, path_join, Globals, globalsdynamic

project_path = get_project_root()

def make_new_folder(folder_path):
    '''创建新文件夹'''
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print("已创建新文件夹:", folder_path)
    else:
        print("文件夹已存在:", folder_path)

def write_new_file(path,text=''):
    # 创建一个新文件并写入内容
    file = open(path, "w",encoding='utf-8')
    file.write(text)
    file.close()
def write_new_json(path,text={}):
    # 创建一个新文件并写入内容
    file = open(path, "w",encoding='utf-8')
    write_json(text,path)
    file.close()

def save_as_file(filename, destination):
    '''文件另存为'''
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Image file '{filename}' not found.")
        shutil.copyfile(filename, destination)
        print(f"Image '{filename}' saved to '{destination}'.")
    except Exception as e:
        print(e)

def delete_file(file_path):
    """删除文件"""
    # 检查文件是否存在
    if os.path.exists(file_path):
        # 删除文件
        os.remove(file_path)
        print("文件已成功删除")
    else:
        print("文件不存在")

def delete_folder(folder_path):
    '''删除文件夹'''
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print("已删除文件夹:", folder_path)
    else:
        print("文件夹不存在:", folder_path)

def delete_images_with_prefix(folder_path, prefix):
    """删除文件夹下指定前缀的图片文件"""
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.startswith(prefix) and file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif','.bmp')):
                os.remove(os.path.join(root, file))


def clear_folder_if_exceeded_numbe(folder_path,num=100):
    """文件超过一定数量则清空文件夹的所有文件"""
    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        # 获取文件夹中的文件数量
        file_count = len(os.listdir(folder_path))
        # 如果文件数量多于100，则清空文件夹
        if file_count > num:
            # 删除文件夹中的所有文件
            shutil.rmtree(folder_path)
            # 重新创建空文件夹
            os.mkdir(folder_path)
            print("文件夹已清空")

def clear_folder(folder_path):
    '''清空文件夹'''
    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        # 遍历文件夹中的所有文件和子文件夹
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            # 判断是否为文件
            if os.path.isfile(file_path):
                # 删除文件
                os.remove(file_path)
            # 判断是否为文件夹
            elif os.path.isdir(file_path):
                # 递归调用清空文件夹函数
                shutil.rmtree(file_path)
    else:
        print(f"文件夹 {folder_path} 不存在")

def rename_file(folder_path,new_folder_name):
    '''重命名文件名'''
    if os.path.exists(folder_path):
        os.rename(folder_path, new_folder_name)
        print("已将文件夹重命名为:", new_folder_name)
    else:
        print("文件夹不存在:", folder_path)
# def rename_file(folder_path, new_folder_name):
#     '''重命名文件名'''
#     if os.path.exists(folder_path):
#         new_folder_path = os.path.join(os.path.dirname(folder_path), new_folder_name)
#         try:
#             shutil.move(folder_path, new_folder_path)
#             print("已将文件夹重命名为:", new_folder_name)
#         except Exception as e:
#             print("重命名失败:", str(e))
#     else:
#         print("文件夹不存在:", folder_path)



def scale_image(image_path,temp_filename, w, h):
    '''图像缩放'''
    # 打开图像
    image = Image.open(image_path)

    # 获取原始图像的宽度和高度
    original_width, original_height = image.size

    # 计算缩放比例
    if original_width / w > original_height / h:
        scale_width = w / original_width
        scale_height = scale_width
    else:
        scale_height = h / original_height
        scale_width = scale_height

    # 计算缩放后的宽度和高度
    scaled_width = int(original_width * scale_width)
    scaled_height = int(original_height * scale_height)

    # 缩放图像
    scaled_image = image.resize((scaled_width, scaled_height))

    # 保存缩放后的图像为临时文件
    scaled_image.save(temp_filename)

    # 返回缩放后的图像
    return scaled_image

def read_json(json_path):
    '''读取json文件'''
    with open(json_path, 'r') as file:
        json_data = json.load(file)
    return json_data

def write_json(json_data,json_path):
    '''写入json文件'''
    # 打开文件并将数据写入JSON文件
    with open(json_path, 'w') as file:
        json.dump(json_data, file)