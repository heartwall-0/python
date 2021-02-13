'''
Author: your name
Date: 2021-02-13 22:25:32
LastEditTime: 2021-02-13 22:31:51
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Python_modularity\making_pizza.py
'''

'''
当python读取pizza.py这个文件时，会在幕后赋值这个文件的所有的代码，此时你可以使用其文件中任意的函数。
当调用时使用模块名称和函数名并且用"."将它们隔开。

import pizza 

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green_peppers', 'extra cheese')
'''

'''
导入特定的函数
'''
from pizza import make_pizza 

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green_peppers', 'extra cheese')