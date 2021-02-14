'''
Author: your name
Date: 2021-02-14 18:45:02
LastEditTime: 2021-02-14 18:48:39
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\9_1.py
'''
class Dog:

    def __init__(self, name, age):
         self.name = name 
         self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")