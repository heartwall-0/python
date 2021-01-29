squares = []
for value in range(1, 11):
    squar = value ** 2
    squares.append(squar)

print(squares)

#!另一版本
squares1 = []
for value in range(1, 11):
    squares1.append(value ** 2)

print(squares1)

#!查找列表中的最大最小总和：
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))   #todo 列表中最小值
print(max(digits))   #todo 列表中最大值
print(sum(digits))   #todo 列表中总和

numbers = list(range(1, 1000001))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

#? for value in range(1, 1000001):
#?     print(value)

#!第一个数是起始值，第二个数是终止数，第三个数步长
for value in range(1, 21, 2):
    print(value)

print("\n")

for value in range(3, 31, 3):
    print(value)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)

print(cubes)

#!列表解析
cubes1 = [value ** 3 for value in range(1, 11)]
print(cubes1)