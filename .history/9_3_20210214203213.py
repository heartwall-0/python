'''
Author: Daylight
Date: 2021-02-14 20:29:23
LastEditTime: 2021-02-14 20:32:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\9_3.py
'''
'''子类继承父类'''
import 9_3

class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
