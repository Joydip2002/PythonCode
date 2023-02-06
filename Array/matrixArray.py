from numpy import *

# data = array([[1,2,3],[3,4,5]]) # but it is not matrix form
# print(data)

# data = array([[1,2,3],[3,4,5]]) 
# m = matrix(data)   # but it is matrix form
# print(m)
# OR
# data = matrix('1,2,3; 2,3,4')
# print(data)

# Methods
# data = array([[1,2,3],[2,3,4],[3,4,5]])
# m = matrix(data)
# print(data)

#2d to 1d => flatten()
# twoDToSingleD = data.flatten() 
# print(twoDToSingleD)

#reshape() => create dimension
# data = array([12,3,4,5,6,4])

# d = data.reshape(2,3)
# print(d)

# max and min in array
# data = array([1,2,3,4,5])
# maxNo = data.max()
# print(maxNo)
# minNo = data.min()
# print(minNo)

#diagonal()
# data = matrix('1,2,3;4,5,6;7,8,9')
# print(data)
# d = diagonal(data)
# print("Diagonal Elements are: \n",d)

#addition,multiplication
m1 = matrix('1,2,3;4,5,6;7,8,9')
m2 = matrix('12,23,34;45,66,77;5,6,7')

a = m1 + m2
print(a)

mul = m1 * m2
print(mul)


