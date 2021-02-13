'''
Author: Daylight
Date: 2021-02-02 09:38:06
LastEditTime: 2021-02-02 10:49:11
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

#todo 使用方法keys遍历键值(只是键值),且下面两种方法的结果相同
for name in favorite_languages:
    print(f"\n{name.title()}")

for name in favorite_languages.keys():
    print(f"\n{name.title()}")
    print(name)

#todo 对这个遍历字典的方法好好理解
friends = ['phil', 'Sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()} , I see you love {language}!")

if "erin" not in favorite_languages.keys():
    print("Erin, please take our poll!")


'''
按特定的顺序返回字典中的键值对.
使用方法sorted()
使用方法set()查找列表中独一无二的元素
'''
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

for language in set(favorite_languages.values()):
    print(language.title())

'''集合和字典的区别,当花括号内部内没键值时，很可能定义的是集合'''
languages = {'python', 'ruby'. 'c', 'python'}
print(languages)