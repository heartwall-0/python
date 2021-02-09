'''
Author: 零到正无穷
Date: 2021-02-09 20:46:13
LastEditTime: 2021-02-09 21:08:43
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\8_3.py
'''
'''接受名和姓输入，然后组合再次输出'''
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
print("\n")
#todo 输出：Jimi Hendrix

#todo 有中间名时显示用判断语句显示
def get_formatted_named(first_name, last_name, middle_name = ' '):
    if middle_name == ' ':
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician1 = build_person('jimi', 'hendrix')
print(musician1)