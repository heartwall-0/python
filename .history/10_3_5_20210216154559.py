'''
Author: 零到正无穷
Date: 2021-02-16 15:32:31
LastEditTime: 2021-02-16 15:45:49
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3_5.py
'''
'''处理FileNotFoundError异常'''
filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")