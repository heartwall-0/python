'''
Author: your name
Date: 2021-02-16 09:26:49
LastEditTime: 2021-02-16 09:33:33
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

birthday = input("Enter your birthday, in the from mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear int the first million digits of pi!")