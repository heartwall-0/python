'''
Author: Daylight
Date: 2021-02-08 11:32:23
LastEditTime: 2021-02-08 11:39:07
LastEditors: Please set LastEditors
Description: Modulo operator
FilePath: \python\7_1_3.py
'''
'''判断一个数是偶数还是奇数'''
number = input("Please enter any number: ")

if int(number) % 2 == 0:
    print(f"\nThis number is even!")
else:
    print(f"This number is odd!")