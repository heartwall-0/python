import numpy as np
def native_relu(x):
    assert len(x.shape) == 2   #todo 说明输入得是一个2D张量

    x = x.copy()               #todo 避免覆盖输入的张量
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x
#todo 注意矩阵如何定义，以及他和列表的区别，最外层是圆括号，外层是中括号是列表list
num1 = np.array([[1,2,3,4],
                [3,4,5,6],
                [5,6,7,8]])
num2 = num1.copy()
print(num1.shape)  #todo 输出(3,4)表明是3行4列
print(num1.ndim)   #todo 输出该张量是2D

#todo 定义的num1张量是2D的所以shape[]括号中的数字只能为0,1；所以当输入大于1的数字时其输出有错误
print(num1.shape[0])  #todo 输出3
print(num1.shape[1])  #todo 输出4
#todo 检验定义的函数 以下两条语句输出相同
print(num1)                 
print(native_relu(num1))
#todo 检验x.copy()得函数作用
print(num2)