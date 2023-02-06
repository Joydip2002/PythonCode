def primeNumber(n):
    flag = 1
    for i in range(2,n):
        if n % i == 0:
            flag = 0
            break;
    if flag == 1:
        print("Prime Number")
    else:
        print("Non-Prime Number") 

n  = int(input("Enter A Number: "))
primeNumber(n)