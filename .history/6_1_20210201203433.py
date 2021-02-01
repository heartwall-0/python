'''
Author: Daylight 
Date: 2021-02-01 20:18:57
LastEditTime: 2021-02-01 20:34:32
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\6_1.py
'''
#todo 字典（简单的字典）
alien_0 = {'color': 'green', 'point': 5} #! 保存两个键值
alien_1 = {'colors': 'red'}              #! 最简单的字典

print(alien_0['color'])   #? 输出字典的某个键值的方法
print(alien_0['point'])

#todo 假设你射杀了一个外星人，将返回你取得的分数(访问字典中的值)
new_points = alien_0['point']
print(f"You just earned {new_points} points!")

#todo 添加键值对
