'''
Author: your name
Date: 2021-02-11 08:50:15
LastEditTime: 2021-02-11 10:07:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_4.py
'''
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

username = ['hannah', 'ty', 'margot']
greet_users((username))


