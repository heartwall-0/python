'''
Author: Daylight
Date: 2021-02-03 11:43:25
LastEditTime: 2021-02-03 11:56:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \python\6_4_1.py
'''
#todo 按照方法一的输出，创建一个空列表来存放外星人信息
aliens = []
#todo 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 10, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['spped'] = 'medium'
        alien['points'] = 15

#todo 显示前五个外星人
for alien in aliensp[:5]:
    print(alien)
print('...')