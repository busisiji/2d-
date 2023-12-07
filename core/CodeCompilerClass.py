# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""代码编译器"""
import os
import subprocess
import time
import traceback

from PyQt5.Qsci import *
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from lib.path import path_join, Globals, globalsdynamic
from lib.utils import ch_to_str


class MyQsciScintilla(QsciScintilla):
    def __init__(self):
        super(QsciScintilla,self).__init__()
        """文本编译器"""
        self.setUtf8(True)  # 设置文档的编码格式为 “utf8”
        self.setBraceMatching(QsciScintilla.StrictBraceMatch)  # 设置括号匹配模式

        # 设置字体
        self.myFont = QFont()
        self.myFont.setPointSize(10)
        self.setFont(self.myFont)
        self.setBraceMatching(QsciScintilla.StrictBraceMatch)

        # 设置光标
        self.setCaretWidth(2)  # 光标宽度（以像素为单位），0表示不显示光标
        self.setCaretForegroundColor(QColor("darkCyan"))  # 光标颜色
        self.setCaretLineVisible(True)  # 是否高亮显示光标所在行
        self.setCaretLineBackgroundColor(QColor('#FFCFCF'))  # 光标所在行的底色

        # 设置 Tab 键功能
        self.setIndentationsUseTabs(True)  # 行首缩进采用Tab键，反向缩进是Shift +Tab
        self.setIndentationWidth(4)  # 行首缩进宽度为4个空格
        self.setIndentationGuides(True)  # 显示虚线垂直线的方式来指示缩进
        self.setTabIndents(True)  # 编辑器将行首第一个非空格字符推送到下一个缩进级别
        self.setAutoIndent(True)  # 插入新行时，自动缩进将光标推送到与前一个相同的缩进级别
        self.setTabWidth(4)  # Tab 等于 4 个空格

        # 设置改动标记
        self.setMarginType(1, QsciScintilla.SymbolMargin)  # 设置标号为1的页边用于显示改动标记
        self.setMarginWidth(1, "0000")  # 改动标记占用的宽度

        # 换行
        self.setMarkerForegroundColor(QColor("#FFFFFF"), 0)
        self.setEolMode(QsciScintilla.EolUnix)  # 文件中的每一行都以EOL字符结尾（换行符为 \r \n）
        # self.setEolMode(QsciScintilla.SC_EOL_CRLF)  # 文件中的每一行都以EOL字符结尾
        # self.setEolMode(self.SC_EOL_LF)  # 以\n换行
        self.setWrapMode(self.WrapWord)  # 自动换行。self.WrapWord是父类QsciScintilla的
        self.setAutoIndent(True)  # 换行后自动缩进
        # self.setWrapIndentMode(QsciScintilla.WrapIndentFixed)

        # 设置边栏
        self.setMarginsFont(self.myFont)  # 行号字体
        self.setMarginLineNumbers(0, True)  # 设置标号为0的页边显示行号
        self.setMarginWidth(0, '000')  # 行号宽度
        # self.setMarginType(0, self.NumberMargin)    # 0~4。第0个左边栏显示行号
        # self.setMarginsBackgroundColor(QtGui.QColor(120, 220, 180))  # 边栏背景颜色
        self.setMarginWidth(1, 0)  # 边栏宽度
        # self.setMarginWidth(0, 20)  # 边栏宽度

        # 代码折叠
        self.setFolding(True)  # 代码可折叠
        self.setIndentationGuides(True)  # 设置缩进标记
        # 设置代码自动折叠区域
        self.setFolding(QsciScintilla.PlainFoldStyle)
        # 设置代码折叠和展开时的页边标记 - +
        self.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPEN)
        self.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDER)
        self.markerDefine(QsciScintilla.Minus, QsciScintilla.SC_MARKNUM_FOLDEROPENMID)
        self.markerDefine(QsciScintilla.Plus, QsciScintilla.SC_MARKNUM_FOLDEREND)
        # 设置代码折叠后，+ 的颜色FFFFFF
        self.setMarkerBackgroundColor(QColor("#FFBCBC"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.setMarkerForegroundColor(QColor("red"), QsciScintilla.SC_MARKNUM_FOLDEREND)
        self.setFolding(QsciScintilla.BoxedTreeFoldStyle)  # 启用折叠功能

        # 自动补全
        self.autoCompleteFromAll()
        # self.setAutoCompletionCaseSensitivity(False)  # 自动补全大小写敏感
        self.setAutoCompletionThreshold(1)  # 输入多少个字符才弹出补全提示
        self.setAutoCompletionReplaceWord(False)
        self.setAutoCompletionUseSingle(QsciScintilla.AcusExplicit)
        self.setAttribute(Qt.WA_DeleteOnClose)

    def foldCode(self):
        """实现折叠逻辑"""
        # 遍历每一行
        for line in range(self.editor.lines()):
            # 获取当前行的缩进级别
            indent = self.editor.indentation(line)

            # 检查是否需要折叠
            if indent > 0:
                # 折叠当前行
                self.editor.foldLine(line)
            elif indent == 0:
                # 展开当前行
                # self.editor.unfoldLine(line)
                self.editor.foldAll(False)

class QsciScintillaPy(MyQsciScintilla):
    def __init__(self):
        super(QsciScintillaPy, self).__init__()
        """python文本编译器"""

        # 创建词法分析器
        self.lexer = QsciLexerPython()
        # 把分析器加载到编译器中
        self.setLexer(self.lexer)

        # 自动补全
        apis = QsciAPIs(self.lexer)  # 添加关键字
        if (apis.load(path_join(Globals.project_path, 'core/数据转换/pythonApis.txt'))):
            print("读取成功")
        else:
            print("读取失败")
        apis.prepare()
        self.setAutoCompletionSource(self.AcsAll)  # 自动补全。对于所有Ascii字符


class QsciLexerVBS(QsciLexer):
    def __init__(self, parent):
        super(QsciLexerVBS, self).__init__(parent)
    def description(self, style):
        return "VBS Lexer"

class QsciScintillaVBS(MyQsciScintilla):
    def __init__(self):
        super(QsciScintillaVBS, self).__init__()
        """VBScrip文本编译器"""

        # 创建词法分析器
        self.lexer = QsciLexerVBS(self)
        # 把分析器加载到编译器中
        self.setLexer(self.lexer)

        # 自动补全
        apis = QsciAPIs(self.lexer)  # 添加关键字
        if (apis.load(path_join(Globals.project_path, 'core/数据转换/VBScripApis.txt'))):
            print("读取成功")
        else:
            print("读取失败")
        apis.prepare()
        self.setAutoCompletionSource(self.AcsAll)  # 自动补全。对于所有Ascii字符

        # 设置 Tab 键功能
        self.setIndentationsUseTabs(True)  # 行首缩进采用Tab键，反向缩进是Shift +Tab
        self.setIndentationWidth(2)  # 行首缩进宽度为4个空格
        self.setTabWidth(2)  # Tab 等于 4 个空格

class MyCodeCompiler(QMainWindow):

    _signal = pyqtSignal(str,int,str)
    def __init__(self):
        super(MyCodeCompiler, self).__init__()
        """代码编译器"""

        # 设置窗口的宽高和标题
        # self.setGeometry(300, 300, 800, 400)
        # self.center()

        # 创建一个frame,并设置布局
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.lvBox = QVBoxLayout()
        self.frm.setLayout(self.lvBox)
        self.setCentralWidget(self.frm)

        # 信号
        # self._signal.connect(self.setMenuAction)

        # self.show()

    # 控制台运行结果输出到GUI
    def onUpdateText(self, text):
        """Write console output to text widget."""
        cursor = self.process.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.process.setTextCursor(cursor)
        self.process.ensureCursorVisible()

    def confirm_btn_action(self):
        self.code = self.editor.text()
        self.save_db()

    # 定义一个函数使得窗口居中显示
    def center(self):
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width() - size.width()) / 2
        newTop = (screen.height() - size.height()) / 2
        self.move(int(newLeft), int(newTop))

    def insertionFunction(self,q):
        """插入函数"""
        add_code = q.text().split('(')[0] + '()'
        if '(' in q.text():
            self.editor.insert(add_code) # 插入函数
        # elif '：' in q.text():
        #     self.editor.insert(q.text().split('：')[0] )  # 插入函数
        # self.editor.SendScintilla(self.editor.SCI_SETCURRENTPOS, self.editor.SCI_GETCURRENTPOS)  # 移动光标位置
    def insertVariable(self,q):
        """插入变量"""
        if '：' in q.text():
            self.editor.insert(q.text().split('：')[0])  # 插入变量名
        elif ':' in q.text():
            if ':' in q.text():
                self.editor.insert(q.text().split(':')[0])  # 插入变量名
        else:
            self.editor.insert('{'+q.text()+'}')  # 插入变量名
        # self.editor.SendScintilla(self.editor.SCI_SETCURRENTPOS, self.editor.SCI_GETCURRENTPOS)  # 移动光标位置 不知道为什么光标位置固定在了2008

    def findMenuAction(self,type,text):
        """查找预设变量"""
        actions = []
        if type == 'input':
            actions = self.inputVar.actions()
        elif type == 'output':
            actions = self.outputVar.actions()
        for action in actions:
            if action.text() == text:
                return action


    def setMenuAction(self,type,index, text):
        """增加预设变量"""
        if type == 'input':
            actions = self.inputVar.actions()
            if len(actions) <= index:
                self.inputVar.addAction(text)
            else:
                actions[index].setText(text)
        elif type == 'output':
            actions = self.outputVar.actions()
            if len(actions) <= index:
                self.outputVar.addAction(text)
            else:
                actions[index].setText(text)
    def deleteMenuAction(self,texts:list,type = 'input'):
        """删除预设变量"""
        if type == 'input':
            for text in texts:
                self.inputVar.removeAction(self.findMenuAction(type,text))
        elif type == 'output':
            for text in texts:
                self.outputVar.removeAction(self.findMenuAction(type,text))
    def clearMenuAction(self,type = 'input'):
        """清空预设变量"""
        if type == 'input':
            # for action in self.inputVar.actions():
            #     self.inputVar.removeAction(action)
            self.inputVar.clear()
        elif type == 'output':
            # for action in self.outputVar.actions():
            #     self.outputVar.removeAction(action)
            self.outputVar.clear()
    def save_db(self):
        """保存数据"""
        self.keys = ['id' , 'inputType','inputName','outputType','outputName','textPy','textVBS']
        self.data = {}
        self.data['id'] = Globals.node_index
        if self.objectName() == 'widget_31':
            self.data['textPy'] = self.editor.text()
        elif self.objectName() == 'widget_34':
            self.data['textVBS'] = self.editor.text()
        # globalsdynamic.db_child.create_tables('QsciScintilla' , self.keys)
        globalsdynamic.db_child.insert_data('QsciScintilla' , self.data,'id')

    def get_var_names(self,type='all'):
        """获取使用变量名"""
        names = []
        if type == 'input':
            actions = self.inputVar.actions()
        elif type == 'output':
            actions = self.outputVar.actions()
        else:
            actions = self.inputVar.actions() + self.outputVar.actions()
        for action in actions:
            names.append('{'+action.text()+'}')
        return names

    def remove_parenthesis(self,str):
        """去括号"""
        return str.strip('{').strip('}')
    def btn_action(self,datas={}):
        """执行代码"""
        try:
            if not datas:
                return
            code = self.editor.text()

            if self.objectName() == 'widget_31':
                names = self.get_var_names()
                self.var_dist = {}
                # 输入输出变量写入
                for i in range(len(names)):
                    # if names[i] in code:
                        # self.var_dist[names[i]] = self.remove_parenthesis(names[i])
                        # self.var_dist[names[i]] = datas[self.remove_parenthesis(names[i])]
                        # self.var_dist[names[i]] = "'" + str(self.var_dist[names[i]]) + "'" if isinstance(str(self.var_dist[names[i]]),str) else self.var_dist[names[i]]
                    self.var_dist[names[i]] = f"{ch_to_str('参数变量')}['" + str(
                        self.remove_parenthesis(names[i])) + "']"
                    code = code.replace(names[i], self.var_dist[names[i]])  # 查找替换变量
                new_code = code + '\nMain()'
                exec(new_code, {f'{ch_to_str("参数变量")}':datas})
                return list(datas.values())

            elif self.objectName() == 'widget_34':
                """VBS"""
                self.var_dist = {}
                # 修改变量
                code = code.replace('\t', '  ')  # 修改空格格式

                # 增加变量声明
                init_code = '' # 初始值
                dim_code = 'dim ' # 变量声明
                print_code = '' # 变量输出
                # 输入变量写入
                names = self.get_var_names('input')
                for i in range(len(names)):
                    self.var_dist[names[i]] = datas[self.remove_parenthesis(names[i])]
                    code = code.replace(names[i], self.var_dist[names[i]])  # 查找替换变量
                    # dim_code = dim_code + self.var_dist[names[i]]  # 变量声明
                    # if i != len(names) - 1:
                    #     dim_code = dim_code + ', '
                # code = dim_code + '\n' + code # 变量声明写入

                # 输出变量写入
                names = self.get_var_names('output')
                for i in range(len(names)):
                    self.var_dist[names[i]] = ch_to_str(names[i])  # 修改变量名
                    code = code.replace(names[i], self.var_dist[names[i]])  # 查找替换变量

                    dim_code = dim_code + self.var_dist[names[i]]  # 变量声明
                    init_code = init_code + self.var_dist[names[i]] + '="None"\n'
                    if i != len(names) - 1:
                        dim_code = dim_code + ', '
                    print_code = print_code + f"WScript.StdOut.WriteLine {self.var_dist[names[i]]}\n"  # 变量输出
                code = init_code + '\n' + code  # 输出变量初始值写入
                code = dim_code + '\n' + code  # 输出变量声明写入
                new_code = code.replace(f'End Sub', f"{print_code}End Sub\nMain") # 变量输出写入

                # 将VBScript代码保存到一个临时文件
                vbs_file = path_join(Globals.project_path,'core/数据转换/editor.vbs')
                with open(vbs_file, 'w',encoding='ANSI') as file:
                    file.write(new_code)
                result = subprocess.check_output(['cscript', '//Nologo', vbs_file])
                # 解析输出以获取添加的内容
                result = result.decode('ANSI').strip()
                # 打印添加的内容
                print("Added VBS content:", result)
                # 删除临时文件
                os.remove(vbs_file)
                # 修改输出格式
                if result:
                    result = [x if x!="''" else None for x in result.split('\r\n')]
                return result
        except (Exception, BaseException) as e:
            exstr = traceback.format_exc()
            print(exstr)
            print("运行失败")
        else:
            print('运行成功')

class codeCompilerPy(MyCodeCompiler):
    def __init__(self):
        super(codeCompilerPy, self).__init__()
        """python代码编译器"""

        # 创建文本编辑器
        self.editor = QsciScintillaPy()

        # 绑定折叠事件
        # self.editor.textChanged.connect(self.foldCode)
        # 把编辑器添加到布局
        self.lvBox.addWidget(self.editor)

        # 添加菜单栏
        # self.defDist = {
        #     "int(x)：" : int, "float(x)" : float, "complex(real,imag)" : complex, "str(x)" : str, "eval(str)" : eval,"tuple(s)" : tuple,
        #     "list(s)" : list, "chr(x)" : chr, "ord(x)" : ord, "hex(x)" : hex, "oct(x)" : oct,"bin(x)" : bin,
        # }
        bar = self.menuBar()
        menuFun = bar.addMenu("函数")
        # 基础函数
        convert = menuFun.addMenu("基础函数")
        convert.addAction("len(x)：用于获取字符串、列表、元组等对象的长度")
        convert.addAction("print(x)：打印输出函数，可以将指定的文本或变量输出")
        convert.addAction("type(x)：用于获取变量的数据类型")
        convert.addAction("range(x)：生成一个整数序列")
        convert.addAction("sum(x)：用于计算列表或元组中所有元素的和")
        convert.addAction("max(x)：用于获取列表或元组中的最大值")
        convert.addAction("min()：用于获取列表或元组中的最小值")
        convert.addAction("sorted()：用于对列表或元组进行排序")
        convert.addAction("zip()：用于将多个列表或元组中对应位置的元素组合成一个元组")
        convert.addAction("enumerate()：用于将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标")
        # 转换函数
        convert = menuFun.addMenu("转换函数")
        convert.addAction("int(x)：将x转换为⼀个整数")
        convert.addAction("bool(x)：将x转换为布尔值")
        convert.addAction("float(x)：将x转换为⼀个浮点数")
        convert.addAction("complex(real,imag)：创建⼀个复数，real为实部，imag为虚部")
        convert.addAction("str(x)：将x转换为⼀个字符串")
        convert.addAction("eval(str)：⽤来计算在字符串中的有效Python表达式,并返回⼀个对象")
        convert.addAction("tuple(s)：将序列s转换为⼀个元组")
        convert.addAction("list(s)：将序列s转换为⼀个列表")
        convert.addAction("chr(x)：将⼀个整数转换为⼀个Unicode字符")
        convert.addAction("ord(x)：将⼀个字符转换为它的ASCII整数值")
        convert.addAction("hex(x)：将⼀个整数转换为⼀个⼗六进制字符串")
        convert.addAction("oct(x)：将⼀个整数转换为⼀个⼋进制字符串")
        convert.addAction("bin(x)：将⼀个整数转换为⼀个⼆进制字符串")
        # 字符串函数
        convert = menuFun.addMenu("字符串函数")
        convert.addAction(".find(str,beg,end)：查找子串str第一次出现的位置，如果找到则返回相应的索引，否则返回-1")
        convert.addAction(".rfind(str,beg,end)：类似于 find()函数，不过是从右边开始查找")
        convert.addAction(".upper()：将字符串中所有元素都转为大写")
        convert.addAction(".lower()：将字符串中所有元素都转为小写")
        convert.addAction(".swapcase()：交换大小写。大写转为小写，小写转为大写")
        convert.addAction(".title()：每个单词的第一次字符大写，其余均为小写")
        convert.addAction(".split(seq,num)：以 seq (默认空格)为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串(只需num个seq分隔符)。分割后得到新列表")
        convert.addAction(".rsplit(seq,num)：与split类似，不过是从右边开始分割")
        convert.addAction(".partition(str)：找到字符串中第一个str，并以str为界，将字符串分割为3部分，返回一个新的元组")
        convert.addAction(".rpartition(str)：与partition类似，只不过是反向找")
        convert.addAction(".join(seq)：以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串")
        convert.addAction(".replace(old, new , max)：把 将字符串中的 old 替换成 new,如果 max 赋值，则替换不超过 max 次")
        convert.addAction(".isidentifier()：判断字符串是不是合法标识符(字符、数字、下划线)")
        convert.addAction(".isspace()：判断字符是否只有空白字符(回车、换行和水平制表符)")
        convert.addAction(".isalpha()：判断字符串是否全部由字母组成")
        convert.addAction(".isdigit()：判断字符串是否全部由数字组成，不包括中文数字")
        convert.addAction(".isnumeric()：判断字符串是否全部由数字组成，中文数字也算")
        convert.addAction(".isascii()：如果字符串为空或字符串中的所有字符都是 ASCII，则返回 True，否则返回 False")
        convert.addAction(".strip(str)：去掉左右两边的str字符")
        convert.addAction(".startswith(str)：检查字符串是否以str开头，若是则返回true")
        convert.addAction(".endswith(str)：检查字符串是否以str结尾，若是则返回true")
        convert.addAction(".encode(encoding=‘UTF-8’)：以encoding指定的编码格式编码字符串")
        convert.addAction(".decode((encoding=“utf-8”)：以encoding指定的编码格式解码bytes对象")
        # 数学函数
        convert = menuFun.addMenu("数学函数")
        convert.addAction("math.ceil(x)：向上取整，返回大于或者等于 x 的最小整数")
        convert.addAction("math.floor(x)：向下取整，返回小于或等于 x 的最大整数")
        # convert.addAction("math.copysign(x,y)：返回一个基于x的绝对值和 y 的符号的浮点数")
        convert.addAction("math.fabs(x)：返回数字的绝对值")
        convert.addAction("math.fmod(x,y)：返回余数,返回浮点数")
        # convert.addAction("math.frexp(x)：返回 x 的尾数和指数作为对(m, e) m是一个浮点数，e是一个整数，正好是x == m * 2**e")
        # convert.addAction("math.ldexp(x, i)：返回 x*(2**i) 这基本上是函数 frexp() 的反函数")
        convert.addAction("math.gcd(a,b)：返回整数 a 和 b 的最大公约数")
        convert.addAction("math.modf(x)：返回 x 的小数和整数部分。两个结果都带有 x 的符号并且是浮点数")
        convert.addAction("math.exp(x)：返回 e 次 x 幂 注意：exp()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法")
        convert.addAction("math.log(x,base)：返回 x 的自然对数（底为 base 默认 e）")
        convert.addAction("math.log2(x)：返回 x 以2为底的对数,这通常比 log(x, 2) 更准确")
        convert.addAction("math.log10(x)：返回 x 以10为底的对数,这通常比 log(x, 10) 更准确")
        convert.addAction("math.pow(x,y)：返回 x 的 y 次方的值,返回浮点数")
        convert.addAction("math.sqrt(x)：返回数字 x 的平方根")
        convert = menuFun.addMenu("三角函数")
        convert.addAction("math.cos(x)：返回 x 弧度的余弦值")
        convert.addAction("math.sin(x)：返回 x 弧度的正弦值")
        convert.addAction("math.tan(x)：返回 x 弧度的正切值")
        convert.addAction("math.acos(x)：返回 x 的反余弦值 返回以弧度为单位的浮点数")
        convert.addAction("math.asin(x)：返回 x 的反正弦值 返回以弧度为单位的浮点数")
        convert.addAction("math.atan(x)：返回 x 的反正切值 返回以弧度为单位的浮点数")
        convert.addAction("math.hypot(x,y)：返回从原点到点 (x, y) 的向量长度")
        convert.addAction("math.degrees(x)：将角度 x 从弧度转换为度数")
        convert.addAction("math.radians(x)：将角度 x 从度数转换为弧度")
        menuFun.triggered[QAction].connect(self.insertionFunction)

        # 变量
        menuVar = bar.addMenu("变量")
        self.inputVar = menuVar.addMenu("输入变量")
        self.outputVar = menuVar.addMenu("输出变量")
        menuVar.triggered[QAction].connect(self.insertVariable)

        # 常量
        menuCon = bar.addMenu("常量")
        menuCon.addAction("math.pi：圆周率，值为3.141592653589793")
        menuCon.addAction("math.e：自然对数，值为2.718281828459045")
        menuCon.triggered[QAction].connect(self.insertVariable)

        # 关键字
        menuKey = bar.addMenu("关键字")
        menuKey.addAction("import：用于导入模块，与form结合使用")
        menuKey.addAction("class：用于定义类")
        menuKey.addAction("def：用于定义函数或方法")
        menuKey.addAction("if：条件语句")
        menuKey.addAction("elif：条件语句，与if、else结合使用")
        menuKey.addAction("else：条件语句，与if、else结合使用，也可用于异常和循环语句")
        menuKey.addAction("for：循环语句，与for in结合使用")
        menuKey.addAction("while：循环语句")
        menuKey.addAction("break：中断循环语句的执行")
        menuKey.addAction("in：判断变量是否在序列中")
        menuKey.addAction("is：判断变量是否为某个类的实例")
        menuKey.addAction("and：用于表达式运算，逻辑与操作")
        menuKey.addAction("or：用于表达式运算，逻辑或操作")
        menuKey.addAction("not：用于表达式运算，逻辑或非操作")
        menuKey.addAction("pass：空的类，方法或函数的占位符")
        menuKey.addAction("None：NoneType类型的值,表示什么也没有")
        menuKey.addAction("True：布尔类型的值，表示真，与False相反")
        menuKey.addAction("False：布尔类型的值，表示假，与True想反")
        menuKey.addAction("lambda：定义匿名函数")
        menuKey.addAction("del：删除变量或序列的值")
        menuKey.addAction("as：用于类型转换，取别名")
        menuKey.addAction("assert：断言，用于判断变量或者条件表达式的值是否为真")
        menuKey.triggered[QAction].connect(self.insertVariable)

        # 添加按钮
        self.btn = QPushButton("运行指令")
        self.btn.setFixedWidth(60)
        self.btn.setFixedHeight(30)
        self.btn.clicked.connect(self.btn_action)

        self.confirm_btn = QPushButton("确认")
        self.confirm_btn.setFixedWidth(50)
        self.confirm_btn.setFixedHeight(30)
        self.confirm_btn.clicked.connect(self.confirm_btn_action)

        # 添加显示窗口.
        # self.process = QTextEdit(self, readOnly=True)
        # self.process.ensureCursorVisible()
        # self.process.setLineWrapColumnOrWidth(500)
        # self.process.setLineWrapMode(QTextEdit.FixedPixelWidth)

        # Custom output stream.
        # sys.stdout = Stream(newText=self.onUpdateText) # 在gui上显示终端输出

        # self.lhBox = QHBoxLayout()
        # self.lvBox.addWidget(self.process)
        # self.lhBox.addWidget(self.btn)
        # self.lhBox.addWidget(self.confirm_btn)
        # self.lvBox.addLayout(self.lhBox)

        # self.show()

class codeCompilerVBS(MyCodeCompiler):
    _signal = pyqtSignal(str,int,str)
    def __init__(self):
        super(codeCompilerVBS, self).__init__()
        """VBS代码编译器"""

        # 创建文本编辑器
        self.editor = QsciScintillaVBS()

        # 绑定折叠事件
        # self.editor.textChanged.connect(self.foldCode)
        # 把编辑器添加到布局
        self.lvBox.addWidget(self.editor)

        bar = self.menuBar()
        menuFun = bar.addMenu("函数")
        # 转换函数
        convert = menuFun.addMenu("转换函数")
        convert.addAction("Asc：将制定字符串转为ASC码")
        convert.addAction("Chr：将制定SAC字符转为字符串")
        convert.addAction("CBool：将表达式转为布尔类型")
        convert.addAction("CByte：将表达式转为字节类型")
        convert.addAction("CDbl：将表达式转为双精度Double类型")
        convert.addAction("CInt：将表达式转为整数Integer")
        convert.addAction("CLng：将表达式转为长整形Long")
        convert.addAction("CStr：将表达式转为字符串String")
        convert.addAction("Hex：将制定数字转为十六进制")
        convert.addAction("Oct：将制定数值转位八进制")
        # 字符串函数
        convert = menuFun.addMenu("字符串函数")
        convert.addAction("InStr：返回字符串在另一字符串中首次出现的位置。检索从字符串的第一个字符开始")
        convert.addAction("InStrRev：返回字符串在另一字符串中首次出现的位置。检索从字符串的最末字符开始")
        convert.addAction("LCase：把指定字符串转换为小写")
        convert.addAction("Left：从字符串的左侧返回指定数目的字符")
        convert.addAction("Len：返回字符串中的字符数目")
        convert.addAction("LTrim：删除字符串左侧的空格")
        convert.addAction("RTrim：删除字符串右侧的空格")
        convert.addAction("Trim：删除字符串左侧和右侧的空格")
        convert.addAction("Mid：从字符串返回指定数目的字符")
        convert.addAction("Replace：使用另外一个字符串替换字符串的指定部分指定的次数")
        convert.addAction("Right：返回从字符串右侧开始指定数目的字符")
        convert.addAction("Space：返回由指定数目的空格组成的字符串")
        convert.addAction("StrComp：比较两个字符串，返回代表比较结果的一个值")
        convert.addAction("String：返回包含指定长度的重复字符的字符串")
        convert.addAction("StrReverse：反转字符串")
        convert.addAction("UCase：把指定的字符串转换为大写")
        # 数学函数
        convert = menuFun.addMenu("数学函数")
        convert.addAction("Abs：返回指定数字的绝对值")
        convert.addAction("Atn：返回指定数字的反正切")
        convert.addAction("Cos：返回指定数字 (角度)的余弦")
        convert.addAction("Exp：返回 (自然对数的底)的次方")
        convert.addAction("Int：返回指定数字的整数部分")
        convert.addAction("Fix：返回指定数字的整数部分")
        convert.addAction("Log：返回指定数字的自然对数")
        convert.addAction("Sgn：返回可指示指定的数字的符号的一个整数")
        convert.addAction("Sin：返回指定数字 (角度)的正弦")
        convert.addAction("Sqr：返回指定数字的平方根")
        convert.addAction("Tan：返回指定数字 (角度)的正切")
        # 其他函数
        convert = menuFun.addMenu("其他函数")
        convert.addAction("Array：返回一个包合数组的变量")
        convert.addAction("Filter：返回下标从零开始的数组，其中包含基于特定过滤条件的字符串数组的子集")
        convert.addAction("IsArray：返回一个布尔值，可指示指定的变量是否是数组")
        convert.addAction("Join：返回一个由数组中若干子字符串组成的字符串")
        convert.addAction("LBound：返回指定数组维数的最小下标")
        convert.addAction("Split：返回下标从0开始的一维数组，包含指定数目的子字符串")
        convert.addAction("UBound：返回指定数组维数的最大下标")
        convert.addAction("IsEmpty：返回一个布尔值，指示指定的变量是否已被初始化")
        convert.addAction("IsNull：返回一个布尔值，指示指定的变量是否包含无效数据(Null)")
        convert.addAction("IsNumeric：回一个布尔值，指示指定的表达式是否可作为数字来计算  ")
        convert.addAction("Round：对数进行四舍五入")
        convert.addAction("TypeName：返回指定变量的子类型")
        convert.addAction("VarType：返回指示变量了类型的值")
        # 跳转函数
        convert = menuFun.addMenu("跳转函数")
        convert.addAction("GotoFunction：跳转到指定功能块")
        convert.addAction("GotoExit：结束程序")
        # 显示函数
        convert = menuFun.addMenu("显示函数")
        convert.addAction("DispText：显示文本信息")
        convert.addAction("DispPoint：显示点")
        convert.addAction("DispLine：显示线")

        # 变量
        menuVar = bar.addMenu("变量")
        self.inputVar = menuVar.addMenu("输入变量")
        self.outputVar = menuVar.addMenu("输出变量")
        menuVar.triggered[QAction].connect(self.insertVariable)

        # 信号
        self._signal.connect(self.setMenuAction)

        # self.show()