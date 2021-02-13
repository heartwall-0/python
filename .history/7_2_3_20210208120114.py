'''
Author: Daylight
Date: 2021-02-08 11:58:53
LastEditTime: 2021-02-08 12:01:02
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\7_2_3.py
'''
'''学会使用标志位'''

Prompt = "\nTell me somthing, and Iwill repeat it back to you: "
Prompt += "\n enter 'quit' to end program."

active = True
while active:
    message = input(Prompt)

    if message == 'quit':
        active = False
    else:
        print(message)