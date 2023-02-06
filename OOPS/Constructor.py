# The __init__ method 
# The __init__ method is similar to constructors in C++ and Java. It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object. 

class ConstructorA():
    def __init__(self,name):
        self.name = name

obj = ConstructorA("Joydip")
print(obj.name)