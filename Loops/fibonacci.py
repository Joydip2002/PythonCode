n = int(input("Enter No of Terms: "))

a = -1
b = 1
# print(a)
# print(b)
temp = 0
for i in range(0,n):
    temp = a + b
    a = b
    b = temp
    print(temp)





