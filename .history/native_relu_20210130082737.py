import numpy as np
def native_relu(x):
    assert len(x.shape) == 2

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)
    return x
#todo 注意矩阵如何定义，以及他和列表的区别
num1 = np.array([[1,2,3,4],
                [3,4,5,6],
                [5,6,7,8],
                [6,7,8,9]])
print(num1.shape)
print(num1.ndim)
 