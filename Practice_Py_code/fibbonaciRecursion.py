def fibbonanci(n):
    if n <= 1:
        return n
    elif n > 1:
        return fibbonanci(n - 1) + fibbonanci(n - 2)

n = int(input("Enter A Number: "))
for i in range(n):
    print(fibbonanci(i),end=" ")
