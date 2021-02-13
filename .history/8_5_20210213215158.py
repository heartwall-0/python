'''
Author: Daylight
Date: 2021-02-13 21:48:57
LastEditTime: 2021-02-13 21:51:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_5.py
'''
'''传递任意数量的参数'''

def make_pizza(*topping):
    """打印顾客所需的配料"""
    print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')