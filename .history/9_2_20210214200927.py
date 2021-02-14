'''
Author: Daylight
Date: 2021-02-14 20:03:42
LastEditTime: 2021-02-14 20:08:38
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\9_2.py
'''
'''使用类和实例'''

class Car:
    def __init__(self, make, model, year):
        self.make = make 
        self.model = model
        self.year = year

    def get_descriptive_name():
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
