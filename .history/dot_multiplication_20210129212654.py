from keras.layers import dot
num1 = [[1,2],[3,4]]
num2 = [[5,6],[8,9]]
output = dot(num1,num2)
print(output)