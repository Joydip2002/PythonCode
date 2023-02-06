# Decorator: In Python , a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another fuubction. The outer function is called th e decorator, which takes the original function as a argunments and returns a modified version of it.

"""Using Simple Function"""

def greet(fx):
    def mfx():
        print("Good Morning!")
        fx()
        print("Good Evening")
    return mfx

@greet  #Decorator
def func_1():
    print("Hello!, Joydip Manna")

func_1()
# greet(func_1)()  #Another way To Call





"""Using Class"""

# class DecoratorClass:
    
#     def greet2(fx):
#         def modi_fx(self):
#             print("Good Morning!")
#             fx(self)
#             print("Good Bye")
#         return modi_fx

#     @greet2
#     def func_1(self):
#         print("I am Function 1")


# obj = DecoratorClass()
# obj.func_1()