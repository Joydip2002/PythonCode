from array import *

def maximum(value,n):
    maxVal = -199999999
    min = value[1]
    for i in range(n):
        # if(value[i] > max):
        #     max = value[i]
        # if(value[i] < min):
        #     min = value[i]
    # return min,max

        mx = max(maxVal,value[i])
        print(mx)
    # print("Maximum Number is: ",max)


value = array('i',[])

n = int(input("Enter Array size: "))
no = 1
for i in range(n):
    x = int(input(f"Enter {no} Element: "))
    value.append(x)
    no+=1

res = maximum(value,n)
print(res)

