'''
Author: Daylight
Date: 2021-02-13 21:48:57
LastEditTime: 2021-02-13 21:57:05
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_5.py
'''
'''传递任意数量的参数'''
'''
输出: 
----------------------------------------------------
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
----------------------------------------------------

def make_pizza(*topping):
    """打印顾客所需的配料"""
    print(topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
'''将函数的print替换为一个循环来描述所要的披萨'''
def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")