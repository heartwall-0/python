'''
Author: 零到正无穷
Date: 2021-02-16 16:45:46
LastEditTime: 2021-02-16 16:48:01
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_4_2_1.py
'''
import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
