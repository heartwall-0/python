'''
Author: Daylight
Date: 2021-02-14 20:29:23
LastEditTime: 2021-02-14 20:39:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\9_3.py
'''
'''子类继承父类,创建子类时父类必须在当前文件中'''
import car

class ElectriCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectriCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())