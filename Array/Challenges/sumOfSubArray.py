from array import *

def sofNumber(data,n):
    sum = 0
    # res = sum
    for i in range(0,n):
        sum = 0
        for j in range(i,n):
            sum += data[j]
            print(sum)
            


data = array('i',[])
n = int(input("Enter Array Size: "))
no = 1
for i in range(n):
    x = int(input("Enter Array Elements: "))
    data.append(x)
    no += 1

sofNumber(data,n)