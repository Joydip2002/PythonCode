# import array 

# arr1 = array.array('i',[1,2,3,4,5])
# # print(arr1)
# arr2 = arr1  #---> this approach copy data but point in same address
# print(arr2)
# print(id(arr1))
# print(id(arr2))


#This Copy is Called Shallow Copy.Cause if u changes values of arr1 of any index then it is changes automatically in arr2
# from numpy import *
# arr1 = array([1,2,3,4,5])
# arr1[2]=5  # modify data in arr1
# arr2 = arr1.view()
# print(arr1)
# print(arr2)

#deep Copy => This copy Copy the content in another address. 
from numpy import *
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
#changes value in arr1 but not effect in arr2
arr1[2] = 10
print(arr1)
print(arr2)
