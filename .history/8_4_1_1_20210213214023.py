'''
Author: Daylight
Date: 2021-02-13 21:35:15
LastEditTime: 2021-02-13 21:40:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_4_1_1.py
'''
'''
继8_4_1后的完善版代码，用函数高效实现其整个过程
'''

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing models: {current_design}")
        completed_models.append(current_design)
    
def show_completed_design(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

unprinted_desingns = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

