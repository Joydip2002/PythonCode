class Demo:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age

    def demoPrint(self):
        print("This is Demo Class")

class Demo1(Demo):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)


    def demo1print(self):
        print("This is demo 1 class")
        super().demoPrint()

class Demo2(Demo1):
    def __init__(self) -> None:
        super().demoPrint()


# obj = Demo()
# print(obj.name,obj.age)

# obj1 = Demo1("Joydip",23)
# obj1.demo1print()

obj2 = Demo2()
