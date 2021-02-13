players = ['charles', 'martina', 'michale', 'florence', 'eli']
print(players[0:3])  #todo 打印前三个值
print(players[1:4])  #todo 从第二个列表值打印到第三个列表中的值
print(players[:4])   #todo 没有指定头，则从初始开始打印至索引尾
print(players[2:])
print(players[-3:])  #todo 输出列表末尾的三个元素

#!遍历切片
print('\n')
print("Here are the first three players on my team:")

for player in players[:3]:
    print(player.title())

#!复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]

print('My favorite foods are:')
print(my_foods)

print('\nMy friends favorite foods are:')
print(friends_foods)

#todo 以下的代码并不能实现两个列表复制后的独立性，只是将两个列表相互关连了，在书上56页
my_foods1 = ['pizza', 'falafel', 'carrot cake']
friends_foods1 = my_foods1

my_foods1.append('cannoli')
friends_foods1.append('ice_cream')

print('My favorite foods are:')
print(my_foods1)

print('\nMy friends favorite foods are:')
print(friends_foods1)




