'''
Author: your name
Date: 2021-02-16 09:26:49
LastEditTime: 2021-02-16 09:29:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_1_1.py
'''
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:51]}...")
print(len(pi_string))