import os

from PyQt5.QtCore import QPointF, QSizeF
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QTableWidgetItem, QComboBox, QLineEdit, QSpinBox, QApplication

from core.坐标标定.CameraCalibrationDb import CCNameDb
from core.数据合并.PooleOperateDb import PooleOperateDb
from core.模板匹配.STMOperateDb import STMOperateDb
from core.网络通讯.ModbusOperateDb import ModbusOperateDb, ModbusNameDb
from core.颜色识别.CROperateDb import CROperateDb
from lib.data import convert_JSON
from lib.db import DB
from lib.path import globalsdynamic, Globals, path_join
from lib.utils import  addImageNew, addImageBetween


def init_mainWindow(window):
    '''初始化主窗口'''
    if globalsdynamic.db_main:
        for label_central in window.label_central_class[int(window.comboBox.currentIndex())]:
            label_central.clear() # 清除图片
            label_name = label_central.objectName()
            child_name = label_name.split('_')[1]
            sql = f"SELECT temppath FROM ImageCapture WHERE name = '{child_name}'"
            temp_path = globalsdynamic.db_main.execute_sql(sql)[0][0] if globalsdynamic.db_main.execute_sql(sql) else ''  # 样板图像
            if temp_path and os.path.exists(temp_path):
                if '2d-' in temp_path:
                    temp_path = temp_path.split('2d-\\')[-1]
                addImageBetween(label_central, temp_path)



def init_visionWindow(window):
    '''初始化视觉窗口'''
    window.View.clear()
    blackimg_path = path_join(Globals.project_path,'icon/black.jpg')
    if os.path.exists(blackimg_path):
        window.View.showImgpath(blackimg_path)
    if globalsdynamic.temp_path and os.path.exists(globalsdynamic.temp_path):
        window.View.showImgpath(globalsdynamic.temp_path)

    result = globalsdynamic.db_main.query_colum('ImageCapture', globalsdynamic.child)
    if not result:
        return
    result = result[0]
    if result:
        # 初始化掩码
        if result[3]:
            mask = convert_JSON(result[3])
            if len(mask) == 5: # mask 0：左上角点（item坐标系中图像左上角为(0,0)的点） 1：掩码大小 2：图像左上角点（item坐标系中填充图形左上角为(0,0)） 3：item窗口大小 4：掩码类型

                now_cur = window.View.curViewSize # 现在窗口大小
                save_cur = mask[3] # 保存掩码时窗口大小
                scale_w = now_cur.width() * 1.0 / save_cur[0]
                scale_h = now_cur.height() * 1.0 / save_cur[1]

                now_back = window.View.playbackItem.pos() # 现在填充图形大小

                scale = min(scale_w,scale_h)
                window.View.addNewMask(id="SelectionBox", type=mask[-1], pos=QPointF(mask[0][0]*scale+now_back.x(), mask[0][1]*scale+now_back.y()),
                                       size=QSizeF(mask[1][0]*scale, mask[1][1]*scale),typeOne=False)

                window.comboBox_9.setCurrentText(mask[-1]) #



def init_imageCapture(window):
    '''初始化图像采集窗口数据'''
    # for widget in [window.listWidget_2, window.listWidget, window.label_2,
    #                window.label_6, window.lineEdit]:
    for widget in [window.listWidget_2, window.lineEdit]:
        widget.clear()
    if globalsdynamic.temp_path and os.path.exists(globalsdynamic.temp_path):
        temp_path = globalsdynamic.temp_path
        # listWidgets = [window.listWidget_2, window.listWidget]
        # labels = [window.label_2, window.label_6]
        listWidgets = [window.listWidget_2]
        labels = [window.label_2]
        for i in range(len(listWidgets)):
            addImageNew(labels[i], temp_path, 374, 200)
            listWidgets[i].addItem(temp_path)
            listWidgets[i].set_currentItem_matching_text(temp_path)
        window.lineEdit.setText(temp_path)

    # 初始化参数
    result = globalsdynamic.db_main.query_colum('ImageCapture', globalsdynamic.child)
    if not result:
        return
    result = result[0]
    if result[2]:
        parameters = convert_JSON(result[2])
        window.comboBox_3.setCurrentText(parameters[0])
        window.comboBox_7.setCurrentText(parameters[1])
        window.comboBox_18.setCurrentText(parameters[2])
        window.comboBox_14.setCurrentText(parameters[3])
        window.comboBox_34.setCurrentText(parameters[4])
        window.comboBox_42.setCurrentText(parameters[5])
        window.comboBox_44.setCurrentText(parameters[6])
        window.spinBox_21.setValue(int(parameters[7]))
        window.comboBox_17.setCurrentText(parameters[8])

def init_ShapTemplateMatching(windowSTM):
    '''初始化模板匹配窗口数据'''
    window = windowSTM.ChildVision
    # windowSTM.template_result_noshow()
    # 清空模板
    for widget in [window.label_10, window.listWidget_3, window.lineEdit_2]:
        widget.clear()
    if globalsdynamic.db_data_path and os.path.exists(globalsdynamic.db_data_path): # 有数据库文件
        x = []
        result = STMOperateDb.get_row()
        if result:

            # 初始化输出参数
            if result[STMOperateDb.get_key_index('output')]:
                output = result[STMOperateDb.get_key_index('output')]
                output = convert_JSON(output)
                for i in range(len(windowSTM.output_list)):
                    windowSTM.output_list[i].setChecked(output[i])

            # 初始化模板
            if result[STMOperateDb.get_key_index('template_paths')]:
                paths = convert_JSON(result[STMOperateDb.get_key_index('template_paths')])
                names = convert_JSON(result[STMOperateDb.get_key_index('template_names')])
                if paths and names:
                # for x in [x for x in range(max(paths) + 1) if x not in list(paths)]:  # 空隔列表填入黑色模块
                #     paths[x] = Globals.black_image_path
                # if x != []:
                #     paths = dict(sorted(paths.items(), key=lambda x: x[0]))  # 将字典根据键的大小排序
                #     globalsdynamic.db_child.insert_data(Globals.toname['模板匹配'],
                #                                         {'id': Globals.node_index, 'template_paths': paths},
                #                                         'id')  # 更新填入黑色模块的模块列表
                # for path in list(paths.values()):
                    for i in range(len(paths)):
                        windowSTM.template_add(paths[i],names[i])
                    windowSTM.template_show(paths[i])
                    QApplication.processEvents()
                else:
                    windowSTM.template_add()
            else:
                windowSTM.template_add()

            # 初始化参数
            windowSTM.set_spinBox15()
            windowSTM.set_comboBox30()
            if result[STMOperateDb.get_key_index('parameters')]:
                parameters = convert_JSON(result[STMOperateDb.get_key_index('parameters')])
                if parameters:
                    window.comboBox_8.setCurrentIndex(int(parameters[0])) if 0 < len(parameters) else ''
                    window.spinBox_7.setValue(int(parameters[1])) if 1 < len(parameters) else ''
                    window.spinBox_2.setValue(int(parameters[2])) if 2 < len(parameters) else ''
                    window.spinBox_3.setValue(int(parameters[3])) if 3 < len(parameters) else ''
                    window.spinBox_5.setValue(int(parameters[4])) if 4 < len(parameters) else ''
                    window.spinBox_8.setValue(int(parameters[5])) if 5 < len(parameters) else ''
                    window.spinBox_13.setValue(int(parameters[6])) if 6 < len(parameters) else ''
                    window.spinBox_9.setValue(int(parameters[7])) if 7 < len(parameters) else ''
                    window.spinBox_6.setValue(int(parameters[8])) if 8 < len(parameters) else ''
                    window.spinBox_4.setValue(int(parameters[9])) if 9 < len(parameters) else ''
                    window.spinBox_10.setValue(int(parameters[10])) if 10 < len(parameters) else ''
                    window.comboBox_11.setCurrentIndex(int(parameters[11])) if 11 < len(parameters) else ''
                    window.comboBox_30.setCurrentText(parameters[12]) if 12 < len(parameters) else ''
                    window.spinBox_15.setValue(int(parameters[13])) if 13 < len(parameters) else ''
                    windowSTM.template_path = parameters[14] if 14 < len(parameters) else ''
                    window.listWidget_3.set_label_names(convert_JSON(parameters[15])) if 15 < len(parameters) else ''
        else:
            windowSTM.template_add()





def init_ColorRecognition(windowCR):
    '''初始化颜色识别窗口数据'''
    window = windowCR.ChildVision
    window.tableWidget.clear_row(db_name =None)
    if globalsdynamic.db_data_path and os.path.exists(globalsdynamic.db_data_path): # 有数据库文件
        result = CROperateDb.get_row()
        if result:
            names = convert_JSON(result[1]) if result[1] else []
            texts = convert_JSON(result[2]) if result[2] else []
            window.tableWidget.setRowCount(len(names))
            for row in range(len(names)):
                for column in range(3):
                    if column == 0:
                        text = names[row]
                    elif column == 1:
                        text = texts[row]
                    else:
                        text = result[3] if result[3] else ''
                    item = QTableWidgetItem(text)
                    window.tableWidget.setItem(row, column, item)
            window.tableWidget.insertRow(len(names))  # 插入一行

def init_CameraCalibration(CCModbus):
    """初始化坐标标定窗口"""
    window = CCModbus.ChildVision
    CCModbus.updata_name_changeds(isUdata=False)

    result = CCNameDb.get_row()
    if result and result[1]:
        name = result[1]
        window.comboBox_45.setCurrentText(name)
    CCModbus.updataTODb()

def init_QsciScintilla(windowQsci):
    """初始化数据转换窗口"""
    window = windowQsci.ChildVision
    result = globalsdynamic.db_child.query_colum(Globals.toname['数据转换'], Globals.node_index,'id')
    # 初始化表格
    window.tableWidget_4.clear_row(True)
    window.tableWidget_5.clear_row(True)
    if not result:
        # 初始化代码
        window.widget_31.editor.setText("import math\n# 导入模块\n# ------------------\ndef Main():\n    # 此处添加代码\n# ------------------\n")
        window.widget_34.editor.setText("\n'变量声明\n'------------------\nSub Main()\n  '此处添加代码\nEnd Sub\n'------------------\n")
        return

    id, inputType, inputName, outputType, outputName, textPy,textVBS,type = result[0]
    inputType = convert_JSON(inputType) if inputType else []
    inputName = convert_JSON(inputName) if inputName else []
    outputType = convert_JSON(outputType) if outputType else []
    outputName = convert_JSON(outputName) if outputName else []
    type = convert_JSON(type) if type else 0

    window.tabWidget_10.setCurrentIndex(int(type))

    # 初始化代码
    if not textPy:
        window.widget_31.editor.setText("import math\n# 导入模块\n# ------------------\ndef Main():\n    # 此处添加代码\n\n# ------------------\n")
    else:
        window.widget_31.editor.setText(textPy)
    if not textVBS:
        window.widget_34.editor.setText("\n'变量声明\n'------------------\nSub Main()\n  '此处添加代码\n\nEnd Sub\n'------------------\n")
    else:
        window.widget_34.editor.setText(textVBS)

    # 初始化表格和预设变量
    for i in range(len(inputName)):
        window.tableWidget_4.set_row_data(i,[inputType[i],inputName[i]]) # 初始化参数表格
        window.widget_31.setMenuAction('input',i,inputName[i]) # 初始化预设变量
        window.widget_34.setMenuAction('input', i, inputName[i])  # 初始化预设变量
    for i in range(len(outputName)):
        window.tableWidget_5.set_row_data(i, [outputType[i],outputName[i]])  # 初始化参数表格
        window.widget_31.setMenuAction('output',i,outputName[i]) # 初始化预设变量
        window.widget_34.setMenuAction('output', i, outputName[i])  # 初始化预设变量


def init_Modbus(windowModbus):
    """初始化网络通讯窗口"""
    window = windowModbus.ChildVision
    windowModbus.updata_name_changeds(isUdata = False)
    result = ModbusNameDb.get_row()
    if result and result[1]:
        window.comboBox_43.setCurrentText(result[1])
    windowModbus.updataTODb()

def init_Poole(windowPoole):
    """初始化数据合并窗口"""
    window = windowPoole.ChildVision
    result = PooleOperateDb.get_row()
    if result and result[1] and result[2]:
        window.comboBox_31.setCurrentText(result[1])
        window.spinBox_16.setValue(int(result[2]))

def init_Output(windowOutput):
    """初始化自定义输出窗口"""
    window = windowOutput.ChildVision
    text = window.tableWidget_2.init_table_data()
    windowOutput.updata_tip(text=text)

def init_parameters(ChildVision,index):
    """流程树运行初始化"""
    window = ChildVision.Childs[index]
    if window.title == '模板匹配':
        init_ShapTemplateMatching(window)
    elif window.title == '颜色识别':
        init_ColorRecognition(window)
    elif window.title == '坐标标定':
        init_CameraCalibration(window)
    elif window.title == '数据转换':
        init_QsciScintilla(window)
    elif window.title == '网络通讯':
        init_Modbus(window)
    elif window.title == '数据合并':
        init_Poole(window)
    elif window.title == '自定义输出':
        init_Output(window)