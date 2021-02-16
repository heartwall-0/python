'''
Author: 零到正无穷
Date: 2021-02-16 17:27:51
LastEditTime: 2021-02-16 17:30:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_4_3.py
'''
import json

def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remeber you when you come back, {username}!")
    else:
        print((f"Welcome back, {username}!"))