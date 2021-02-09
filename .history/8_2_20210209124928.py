'''
Author: your name
Date: 2021-02-09 12:44:50
LastEditTime: 2021-02-09 12:49:28
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_2.py
'''
'''位置实参'''
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
