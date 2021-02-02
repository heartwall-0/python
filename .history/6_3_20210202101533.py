'''
Author: Daylight
Date: 2021-02-02 09:38:06
LastEditTime: 2021-02-02 10:15:33
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
#todo 使用方法item()返回一个键值对
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

'''由类似对象组成的字典'''
favorite_languages = {
    'Jen': 'python',
    'Sarah': 'c',
    'edward': 'ruby',
    'phil': 'spring',
}#! 最后一个键值对后面的都好是为了方便以后添加键值对做好了准备

#todo 遍历整个字典，包括键值对
for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.title()}")

#todo 使用方法keys遍历键值(只是键值)
for name in favorite_languages:
    print(f"\n{name.title()}")

for name in favorite_languages.keys():
    print(f"\n{name.title()}")