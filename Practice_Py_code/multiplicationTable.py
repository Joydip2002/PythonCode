def mulFunction(n):
    if n <= 0:
        return n
    elif n >= 1:
        i = n
        for i in range(1,11):
            print(f"{n} * {i} = {n*i}")
        
n = int(input("Enter no Which Multiplication Table You Can Print: "))
mulFunction(n)