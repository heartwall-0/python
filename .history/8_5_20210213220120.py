'''
Author: Daylight
Date: 2021-02-13 21:48:57
LastEditTime: 2021-02-13 22:01:15
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
'''
输出: 
---------------------------------------------
Making a pizza with the following toppings:
 - pepperoni

Making a pizza with the following toppings:
 - mushrooms
 - green peppers
 - extra cheese
----------------------------------------------

def make_pizza(*toppings):
    print(f"\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''

'''结合使用位置实参和任意数量实参'''
def make_pizza(size, *toppings):
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


