'''
Author: 零到正无穷
Date: 2021-02-16 15:19:27
LastEditTime: 2021-02-16 15:25:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3_3.py
'''
'''使用异常避免崩溃'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)