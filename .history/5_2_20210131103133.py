'''
Author: 零到正无穷
Date: 2021-01-31 08:51:29
LastEditTime: 2021-01-31 10:31:29
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\5_2.py
'''
car = 'Audi'
print(car.lower() == 'audi')
print(car.lower())
#todo 学会使用and 和 or
ageold = 22
ageyounger = 23
print((ageold >20) and (ageyounger > 20))
print((ageyounger > 22) or (ageold > 21))

#todo 检查特定的值在列表中与否
request_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in request_toppings)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
