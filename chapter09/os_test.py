"""
练习:
1.利用os模块编写一个能实现dir -l 输出的程序
2.编写一个程序,能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件,并打印出相对路径
"""
# import os
#
# current_path = os.getcwd() # 定位到当前目录
# def find(filekey):
#     filepath_list = [x for x in os.listdir() if os.path.isfile(x) and filekey in os.path.splitext(x)[0]] # 当前目录下包含filekey的文件
#
#     for i in filepath_list:
#         abs_path = os.path.abspath(i) # 文件绝对路径
#         rel_path = os.path.relpath(abs_path, current_path) # 文件在当前文件夹下的相对路径
#         print('.\\' + rel_path) # 输出相对路径.\rel_path
#
#     subfolder_list = [x for x in os.listdir() if os.path.isdir(x)] # 当前文件夹下的所有目录
#
#     for i in subfolder_list:
#         os.chdir(i)  # 切至子目录
#         find(filekey) # 迭代find()
#         os.chdir('..') # 切回上级目录

# find('test')
#
import os

sep = os.path.sep

def searchFile(key='', p='.', L=None): # key关键字,p当前位置,L符合条件的文件列表
    if L is None:
        L = []
    path = p
    for x in os.listdir(path):
        filePath = path + sep + x # 该文件下文件或目录的相对路径
        if os.path.isdir(filePath):
            searchFile(key, filePath, L) # 如果是文件夹,则迭代search,
        if os.path.isfile(filePath) and os.path.split(filePath)[1].find(key) > -1: # 如果是文件,则追加绝对路径到L中
            L.append(os.path.abspath(filePath))
    return L

for s in searchFile('py'):
    print(s)

#找到特定后缀名的文件







# import os
#
# current_file = os.getcwd()
# def find(filekey):
#     filepath_list = [x for x in os.listdir() if os.path.isfile(x) and filekey in os.path.splitext(x)[0]]
#     for i in filepath_list:
#         abs_path = os.path.abspath(i)
#         rel_path = os.path.relpath(abs_path, current_file)
#         print('.\\' + rel_path)
#
#     subfolder_list = [x for x in os.listdir() if os.path.isdir(x)]
#
#     for i in subfolder_list:
#         os.chdir(i)
#         find(filekey)
#         os.chdir('..')
#
#
# find('python')