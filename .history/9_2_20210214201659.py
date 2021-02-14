'''
Author: Daylight
Date: 2021-02-14 20:03:42
LastEditTime: 2021-02-14 20:16:16
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
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"The car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odometer()