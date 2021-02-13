'''
Author: Daylight
Date: 2021-02-08 08:39:00
LastEditTime: 2021-02-08 08:47:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\7_1_2.py
'''
'''
想要将输入的字符串转化为数字，那么你需要使用方法int()
'''
age = input("Please enter your age: ")

if int(age) < 4:
    price = 0
elif int(age) < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.\n")
