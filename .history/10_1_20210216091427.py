'''
Author: Daylight
Date: 2021-02-15 20:31:11
LastEditTime: 2021-02-16 09:14:27
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_1.py
'''
'''文件和异常'''
#todo 读取pi_digits.txt文件并读出来
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print(contents.rstrip())
print("\n")
#todo 读取数据的另一个方法
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n")
#todo 读取数据的另一个方法

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readline()
    print(lines.rstrip())