players = ['charles', 'martina', 'michale', 'florence', 'eli']
print(players[0:3])  #todo 打印前三个值
print(players[1:4])  #todo 从第二个列表值打印到第三个列表中的值
print(players[:4])   #todo 没有指定头，则从初始开始打印至索引尾
print(players[2:])
print(players[-3:])  #todo 输出列表末尾的三个元素

#!便利切片
print('\n')
print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())
