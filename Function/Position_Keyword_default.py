def add(a,b=3):  #Formal Argument
    c = a + b
    return c

res = add(5,10) #Actual Argument
print(res)
res1 = add(b = 50,a = 20) # Keyword 
print(res1)
res1 = add(20) # default value 
print(res1)
