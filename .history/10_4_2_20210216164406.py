'''
Author: 零到正无穷
Date: 2021-02-16 16:38:25
LastEditTime: 2021-02-16 16:44:06
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_4_2.py
'''
'''保存和读取用户生成的数据'''
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We will remeber you when you come back, {username}!")
