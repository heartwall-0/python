'''
Author: Daylight
Date: 2021-02-13 22:06:53
LastEditTime: 2021-02-13 22:09:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_5_2.py
'''

'''使用任意数量的关键字实参'''

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name']  = last
    return user_info


