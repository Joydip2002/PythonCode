from array import *

#Linear Search Function
def searchLinear(value,n,se):
    for i in range(1,n):
        if(value[i] == se):
            return i;
    return -1


value = array("i",[])
n = int(input("Enter Array Size: "))
for i in range(n):
    x = int(input("Enter Array Elements: "))
    value.append(x)

#For Printing
for i in range(n):
    print(value[i])

n = len(value)
print(n)
se = int(input("Enter Search Element: "))


#searching Function
res = searchLinear(value,n,se)
if(res == -1):
   print("Not Found",res)
else:
     print("Element Found",res)
