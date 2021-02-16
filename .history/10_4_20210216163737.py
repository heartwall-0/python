'''
Author: 零到正无穷
Date: 2021-02-16 16:28:54
LastEditTime: 2021-02-16 16:37:37
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_4.py
'''
'''使用json.dump和json.load'''
import json

numbers = [2, 3, 4, 5, 6, 7, 12, 14]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)#todo 将数据写入

with open(filename) as f:
    numbers = json.load(f) #todo 将存储在寄送的数据加载出来
print(numbers)