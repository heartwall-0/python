'''
Author: Daylight
Date: 2021-02-15 20:31:11
LastEditTime: 2021-02-16 08:57:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_1.py
'''
'''文件和异常'''
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)