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
print(min(digits))
print(max(digits))
print(sum(digits))