import numpy as np
def native_add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape

    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x

num1 = np.array([[1,2,3,4],
                [3,4,5,6],
                [5,6,7,8]])

num2 = np.array([[2,3,4,5],
                 [3,4,5,6],
                 [4,5,6,7]])