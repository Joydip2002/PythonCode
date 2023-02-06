p = int(input("Enter A Number: "))
flag = 1
# if p == 1 or p == 0:
#     print("prime num1ber")
for i in range(2,p):
    if p % i == 0:
        flag = 0
        break
if flag:
    print("Prime Number")
else:
    print("Non-Prime Number")
