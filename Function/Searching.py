from numpy import *
from array import *
def linearSearch(value,se):
    for i in range(len(value)):
        if(value[i] == se):
            return 1
    return -1

def binarySearch(value,se):
    start = 0
    # print(type(start))
    end = len(value)
    # print(type(end))
    while(start <= end):
        mid = int((start + end)/2)
        # print(type(mid))
        if(value[mid] == se):
            return 1
        elif(value[mid] < se):
            start = mid +1
        else:
            end = mid -1
    return -1

n = int(input("Enter Array Size: "))
vals = array('i',[])

for i in range(n):
    x = int(input("Enter Arrays Elements: "))
    vals.append(x)

searchEle = int(input("Enter Search Element: "))

while True:
    print("1. Linear Search: ")
    print("2. Binary Search: ")
    print("3. Exist")
    key = input("Enter Your Choice: ")
    match key:
        case '1':
            res = linearSearch(vals,searchEle)
            print(res)
        case '2':
            binRes = binarySearch(vals,searchEle)
            print(binRes)
        case '3':
            exit(1)
        case _:
            print("Wrong Choice")
            

