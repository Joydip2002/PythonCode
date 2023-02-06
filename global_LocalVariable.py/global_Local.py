a = 50 #global

def check():
    # global a     #it is not a correct approach
    a = 20 #local
    x =globals()['a'] #global
    print(x) 

check()

print(a)