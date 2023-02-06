class Demo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    #Alternate Constructor
    @classmethod
    def formStr(cls,string):
        print(string.split("-")[0],string.split("-")[1])

obj = Demo("Joydip","20")
print(obj.name)
print(obj.age)

Demo.formStr("Joydip-20")
# print(obj.name)
# print(obj.age)