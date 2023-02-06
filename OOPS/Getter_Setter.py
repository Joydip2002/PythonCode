# class Father:
#     def __init__(self,age = 0):
#         print("You are Inside The Consturctor")
#         self.age = age

#     def setAge(self,x):
#         self.age = x

#     def getAge(self):
#         return self.age

# obj = Father()
# obj.setAge(20)
# print(obj.getAge())

"""Using Decorators @property => Getter,  @func_Name.setter => setter"""

class Father:
    def __init__(self):
        self._age = 0

    @property
    def age(self):
        print("Getter Method Called")
        return self._age

    @age.setter
    def age(self,x):
        print("Setter Method Called")
        self._age = x

obj = Father()
obj.age = 67
print(obj.age)
 