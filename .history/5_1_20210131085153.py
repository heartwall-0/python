'''
Author: 零到正无穷
Date: 2021-01-31 08:47:21
LastEditTime: 2021-01-31 08:51:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\5_1.py
'''
cars = ['audi', 'bmw', 'subarn', 'toyota']
#todo if语句的使用
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())