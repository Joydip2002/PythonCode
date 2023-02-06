# class A:
#     # print("I am Class A")
#     def sum(x,y):
#         print(f"Sum is: {x+y}")

# Joy = A()
# # print(Joy)
# print(Joy.__class__.sum(3,4))

# self keyword in python:  self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in python. It binds the attributes with the given arguments.

class dog:
    print("This is dog class")
    name = "Rocky"

    def dogName(self,n):
        print(f"This id dog Name Class. Dog name is {n}")

    def dogColor(self,color):
        print(f"Color is: {color}")


obj = dog()
print(obj.name)
obj.dogName("Tommy")
obj.dogColor("gray")
