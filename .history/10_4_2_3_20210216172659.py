'''
Author: 零到正无穷
Date: 2021-02-16 17:22:48
LastEditTime: 2021-02-16 17:26:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_4_2_3.py
'''
import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load()
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"we'll remeber you when you come back, {username}!")
else:
    print((f"Welcome back, {username}."))