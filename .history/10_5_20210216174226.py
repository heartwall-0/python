'''
Author: 零到正无穷
Date: 2021-02-16 17:33:13
LastEditTime: 2021-02-16 17:42:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_5.py
'''
import json

def get_stored_username():
    '''如果存储了用户名，就获取他'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_new_username():
    username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
    return username


def greet_user():
    '''问候用户，并指出其名字'''
    username = get_stored_username()
    if username:
        print((f"Welcome back, {username}!"))
    else:
        
            print(f"we'll remeber you when you come back, {username}!")

greet_user()