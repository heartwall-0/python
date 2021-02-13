from keras.layers import dot
import numpy as np

num1 = [[1,2],[3,4]]
num2 = [[5,6],[8,9]]
# output = dot([num1,num2], axes = (2,2))
# print(output)

out = np.dot(num1, num2)
print(out)