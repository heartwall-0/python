'''
Author: 零到正无穷
Date: 2021-02-09 20:46:13
LastEditTime: 2021-02-11 08:45:38
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

#todo 输出个人的信息
def get_person_information(first_name, last_name, middle_name = ' ', age = None, Profession = ' '):
    person_information = {'first': first_name, 'last': last_name, 'middle': middle_name, 'age': age,\
        'Profession': Profession}
    if age:
        person_information['age'] = age
    
    return person_information

information = get_person_information(first_name = 'wang', last_name = 'tao', age = 26, Profession = None)
print(information)

#todo 结合使用函数和while循环

def get_formatted_namem(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_namem(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#todo 结合使用函数和while循环的另一版本，由于上面的代码是无限循环，所以应有结束机制

def get_formatted_namee(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")

    f_name = input("First naem: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_namee(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
