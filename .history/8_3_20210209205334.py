'''
Author: 零到正无穷
Date: 2021-02-09 20:46:13
LastEditTime: 2021-02-09 20:53:34
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_3.py
'''
'''接受名和姓输入，然后组合再次输出，'''
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
