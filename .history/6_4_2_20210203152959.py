'''
Author: Daylight
Date: 2021-02-03 12:02:37
LastEditTime: 2021-02-03 15:29:59
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\6_4_2.py
'''
#todo 在字典中存储列表,在字典中存储披萨的信息
pizza = {
    'crust' : 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

#todo 概述所点的披萨
print(f"You ordered a {pizza['crust']} - crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

