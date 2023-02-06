# def means => defination function
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f = f * i
#     return f

# n = int(input("Enter a Number: "))
# res = fact(n)
# print(res)


#You Can return Multiple value
def add_sub(a,b):
    c = a + b
    d = a - b
    m = a * b
    return c,d,m

a = int(input("Enter First Element: "))
b = int(input("Enter Second Element: "))
res = add_sub(a,b)
print(res)