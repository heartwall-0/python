'''
Author: Daylight
Date: 2021-02-03 11:28:07
LastEditTime: 2021-02-03 11:37:26
LastEditors: Please set LastEditors
Description: Dictionary nesting
FilePath: \python\6_4.py
'''

'''输出整个0,1,2字典。输出的一种方法'''
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

ailens1 = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points'； 10， 'speed': 'slow'}
    aliens1.append(new_alien)
#todo 输出前5个外星人
for alien in ailens1[:5]:
    print('...')
#todo 显示创建了多少的外星人
print(f"Total number of ailens: {len(aliens1)}.")