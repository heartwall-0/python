'''
Author: Daylight
Date: 2021-02-13 22:06:53
LastEditTime: 2021-02-13 22:12:56
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_5_2.py
'''

'''使用任意数量的关键字实参'''
'''
输出： 
{'location': 'printceton', 'field': 'physics', 'first_name': 'albert', 'last_name': 'einstein'}
最后的一个参数可以添加人一个键值对，或者任意个键值对
'''

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name']  = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'printceton', field = 'physics')

print(f"{user_profile} \n")