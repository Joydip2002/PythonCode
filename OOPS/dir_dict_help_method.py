class demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def factorial(n):
        
        fact = 1
        for i in range(1,n+1):
            fact *= i
        return fact

print(demo.factorial(5))

print(demo.factorial.__dict__)

obj = demo("Joydip",24)
print(obj.__dict__)
print(help(demo))

