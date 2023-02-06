# Map:  Taking a function and a list as arguments and returning a new list with the function applied to  each element of the list.
# map is return list datatype. It is Hof(Higher Order Function) cause Inside it a functionn arguments exists
li = [1,2,3,4,5]

cubeList = list(map(lambda x:x*x*x,li)) #lamda function: it is inbuild function in python
print("Using Map: ",cubeList,end="\n\n")


#Filter: Filter is used to filter the list based on the condition.
li = [12,2,3,47,8,90]

# def newEvenNum(x):
#     if(x%2 == 0):
#         print(x,end=" ")

# for item in li:
#     newEvenNum(item)

# Using filter
newEvenNum = list(filter(lambda x: x%2==0,li))
print("Using Filter: ",newEvenNum,end="\n\n")


#Reduce: Taking a function and a list as arguments and returning a single value obtained by combining the elements of the list. First import reduce.It is usally use for addition,subtraction in one words arithmetic operation.

# import functools
from functools import reduce
li = [12,2,3,47,8,90]

newReduceLi = reduce(lambda x,y: x+y,li)
newSumEvenNo = list(filter(lambda x: x%2 == 0,li))
sum = reduce(lambda x,y: x+y,newEvenNum)
print(newReduceLi)
print(newSumEvenNo)
print(sum)