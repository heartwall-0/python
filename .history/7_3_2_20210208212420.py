'''
Author: your name
Date: 2021-02-08 21:11:05
LastEditTime: 2021-02-08 21:24:19
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\7_3_2.py
'''
'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑       永不宕机     永无BUG
'''

'''
Author: your name
Date: 2021-02-08 21:11:05
LastEditTime: 2021-02-08 21:11:05
LastEditors: your name
Description: In User Settings Edit
FilePath: \python\7_3_2.py
'''
'''删除特定元素的所有列表元素,如下例，删除其中的cat，使用while'''

pets = ['dog', 'cat', 'tiger', 'cat', 'bear', 'cat', 'horse']

while 'cat' in pets:
    pets.remove('cat')
print(pets)

'''使用用户输入来填充字典'''
responses = {}

polling_active = True
while polling_active:
    name  = input("\nwhat is your name? ")
    response = input("What mountain would you like to climb someday? ")
    responses[name] = response

    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")

      