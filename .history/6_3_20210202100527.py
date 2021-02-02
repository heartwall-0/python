'''
Author: Daylight
Date: 2021-02-02 09:38:06
LastEditTime: 2021-02-02 10:05:26
LastEditors: Please set LastEditors
Description: Practice for dictionaries in python
FilePath: \python\6_3.py
'''
'''
使用for循环来遍历字典
'''
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")