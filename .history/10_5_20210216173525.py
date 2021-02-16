'''
Author: 零到正无穷
Date: 2021-02-16 17:33:13
LastEditTime: 2021-02-16 17:35:25
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_5.py
'''
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
    filename = 'username.json'
    
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remeber you when you come back, {username}!")
    else:
        print((f"Welcome back, {username}!"))