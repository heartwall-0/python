'''
Author: Daylight
Date: 2021-02-08 13:59:41
LastEditTime: 2021-02-08 20:58:54
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



unconfirmed_users = ['alice', 'brian', 'candace']
confirm_users = []
while unconfirmed_users:
  current_user = unconfirmed_users.pop()

  print(f"Verifying user: {current_user.title()}")
  confirm_users.append(current_user)

print("\nThe following users have been confirmed: ")
for confirm_user in confirm_users:
  print(confirm_user.title())