'''
Author: 零到正无穷
Date: 2021-01-31 10:43:22
LastEditTime: 2021-01-31 12:15:14
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\5_3.py
'''
#todo if语句的使用
age = 19
if age >= 18:
    print("You are oold enough to vote!")
    print("Have you registered to vote yet?\n")

#todo if-else语句的使用
age = 19
if age >= 20:
    print("You are oold enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#todo if-elif-else
 
age = 12

if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")