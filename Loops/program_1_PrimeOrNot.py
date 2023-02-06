n  = int(input("Enter A Number: "))
flag = 1

# if n == 1 or n == 0:
#     print(f"{n} Is prime Number")
for i in range(2,n):
    if n % i == 0:
        flag = 0
        break
if flag:
    print("Prime Number")
else:
    print("Not Prime Number")