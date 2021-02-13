'''
Author: your name
Date: 2021-02-09 12:44:50
LastEditTime: 2021-02-09 13:03:10
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_2.py
'''
'''位置实参,也就是C中的实参和形参。且调用时应该对应相应的参数'''
def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    print('\n')

describe_pet('hamster', 'harry')
#todo 多次调用函数
describe_pet('dog', 'willie')
#todo 另一种调用方法,关键字实参，好处是避免了形参的位置是否正确
describe_pet(animal_type = 'hamster', pet_name = 'harry')
#? 等效describe_pet(pet_name = 'harry', animal_type = 'hamster')

'''
默认值参数，describe_pet(animal_type = 'dog', pet_name),
例子如上所示，当你发现在输入数据时大多数是dog，那么将指定默认值，如果你调用时没有指定animal_type的值，那么
该函数将默认输入dog。
'''
def describe_pets(animal_type = 'dog', pet_name):
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
    print('\n')
describe_pets(pet_name = 'willie')


