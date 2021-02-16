'''
Author: 零到正无穷
Date: 2021-02-16 15:56:43
LastEditTime: 2021-02-16 16:00:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3_6.py
'''
'''分析文件'''
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()