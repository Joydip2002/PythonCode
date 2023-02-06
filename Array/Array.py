# import array as arr
 
#  i => signed int
#  I =>unsigned int
#  f => float
#  d => double
#  l => signed long
#  L => unsigned long
#  u => uni character


# vals = arr.array('i',[1,2,4,5])

# print(len(vals))
# print(vals)
# print(vals.buffer_info()) #=> checking array size with address..
# vals.append(7)
# print(vals)

# vals.reverse()
# print(vals)

# vals.typecode()
# print(vals)


#Traverse in Array

# for i in range(0,4):
#     print(vals[i])

# or
# for i in range(len(vals)):
#     print(vals[i])

# or
# for i in vals:
#     print(i)


# copy array
# newArr = arr.array(vals.typecode,(a for a in vals))
# print(newArr)

# By user input Array
from array import *
vals = array('i',[])
ui = int(input("Enter Arrays Size: "))

for i in range(ui):
    x = int(input("Enter Arrays Elements: "))
    vals.append(x)

print(vals)

#searching
se = int(input("Enter search element: "))
k =0
flag = 0
for i in range(len(vals)):
    if(vals[i] == se):
        flag = 1
        print(k)
        break
    k+=1

if(flag == 0):
    print("not found")
