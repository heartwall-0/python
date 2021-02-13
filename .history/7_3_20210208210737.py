'''
Author: Daylight
Date: 2021-02-08 13:59:41
LastEditTime: 2021-02-08 21:07:37
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\7_3.py
'''
'''
                       .::::.
                     .::::::::.
                    :::::::::::
                 ..:::::::::::'
              '::::::::::::'
                .::::::::::
           '::::::::::::::..
                ..::::::::::::.
              ``::::::::::::::::
               ::::``:::::::::'        .:::.
              ::::'   ':::::'       .::::::::.
            .::::'      ::::     .:::::::'::::.
           .:::'       :::::  .:::::::::' ':::::.
          .::'        :::::.:::::::::'      ':::::.
         .::'         ::::::::::::::'         ``::::.
     ...:::           ::::::::::::'              ``::.
    ````':.          ':::::::::'                  ::::..
                       '.:::::'                    ':'````..
'''
'''使用while循环处理列表和和字典'''

'''
该程序的目的是将一个列表转移到另一个列表，其中使用了方法pop和append，pop是弹出列表末尾的元素，
而append是向列表末尾中添加元素。
'''


unconfirmed_users = ['alice', 'brian', 'candace']
confirm_users = []
while unconfirmed_users:
  current_user = unconfirmed_users.pop()  #todo 目的是弹出列表中的元素，赋值给current_user变量
  print(f"Verifying user: {current_user.title()}")
  confirm_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirm_user in confirm_users:
  print(confirm_user.title())