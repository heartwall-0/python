'''
Author: 零到正无穷
Date: 2021-02-17 11:59:25
LastEditTime: 2021-02-17 15:09:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\11_1.py
'''
'''测试函数'''
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_