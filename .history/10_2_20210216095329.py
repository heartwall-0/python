'''
Author: 零到正无穷
Date: 2021-02-16 09:35:23
LastEditTime: 2021-02-16 09:48:10
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_2.py
'''
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

with open(filename, 'a') as file_object:
    file_object.write("I also finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in browser.\n")