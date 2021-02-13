'''
Author: your name
Date: 2021-02-13 22:20:45
LastEditTime: 2021-02-13 22:25:11
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Python_modularity\pizza.py
'''
def make_pizza(size, *toppings):
    print(f"\nMaking a {size} - inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")