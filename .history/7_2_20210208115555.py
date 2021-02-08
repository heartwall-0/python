'''
Author: Daylight
Date: 2021-02-08 11:40:00
LastEditTime: 2021-02-08 11:55:55
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\7_2.py
'''
'''关于while循环的使用'''
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 #todo (current_number = current_number + 1)


Prompt = "\nTell me somthing, and Iwill repeat it back to you: "
Prompt += "\n enter 'quit' to end program."

message = ""
while message != 'quit':
    message = input(Prompt)

    if message != 'quit':
        print(message)
