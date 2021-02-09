'''
Author: 零到正无穷
Date: 2021-02-09 08:12:47
LastEditTime: 2021-02-09 12:02:42
LastEditors: Please set LastEditors
Description: About the use of python functions
FilePath: \python\8_1.py
'''
'''定义python函数'''
#todo 函数输出
def greet_user():
    print("Hello,world")

greet_user()

#todo 
def greet_users(name):
    print(f"\nHello, {name.title()}!")
greet_users(('eric'))