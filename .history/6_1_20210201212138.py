'''
Author: Daylight 
Date: 2021-02-01 20:18:57
LastEditTime: 2021-02-01 21:21:38
LastEditors: Please set LastEditors
Description: Practice for dictionaries in python
FilePath: \python\6_1.py
'''
#todo 字典（简单的字典）
alien_0 = {'color': 'green', 'point': 5} #! 保存两个键值
alien_1 = {'colors': 'red'}              #! 最简单的字典

print(alien_0['color'])   #? 输出字典的某个键值的方法
print(alien_0['point'])

#todo 假设你射杀了一个外星人，将返回你取得的分数(访问字典中的值)
new_points = alien_0['point']
print(f"You just earned {new_points} points!\n")

'''
 添加键值对(往字典中添加一个键值对):例子，假如要显示外星人在屏幕中的位置，而开始一般在屏幕的
 左上方,需要显示x,y的坐标,字典中元素的顺序与添加顺序相同，有时候还可以先定义一个空字典，再向其中添加键值对
'''
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print('\n')

'''
修改字典中的值，将外星人的颜色进行了更换
'''
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")
'''
另一个例子来说明修改字典
'''
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_2['x_position']}") #!输出原始位置
#todo 向右移动外星人，根据当前的速度确定外星人向右移动多远
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3 #! 这个外星人的移动速度很快
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}.")
''' 删除键值 '''
del alien_2['speed'] #! 通过del[键]来删除其中的某一键值对，删除的键值对会永远的消失


'''由类似对象组成的字典'''
favorite_languages = {
    'Jen': 'python',
    'Sarah': 'c',
    'edward': 'ruby',
    'phil': 'spring'
}



