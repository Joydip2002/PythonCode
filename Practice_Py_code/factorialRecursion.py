def factorial(n):
    if n == 1 or n == 1:
        return n
    else:
        return n * factorial(n-1)
item = int(input("Enter A Number: "))
op = factorial(item)
print(f"Factorial Number Is: {op}")