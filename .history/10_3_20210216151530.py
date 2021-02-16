'''
Author: 零到正无穷
Date: 2021-02-16 15:09:15
LastEditTime: 2021-02-16 15:15:30
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\10_3.py
'''
'''处理文件异常'''

#todo 处理ZeroDivisionError异常
# print(5/0) #? 这句会报错如下:
"""
Traceback (most recent call last):
  File "e:\Python\python\10_3.py", line 12, in <module>
    print(5/0) #? 这句会报错如下:
ZeroDivisionError: division by zero

"""

#todo 遇到上述问题我们可以使用type-except代码块来解决

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")