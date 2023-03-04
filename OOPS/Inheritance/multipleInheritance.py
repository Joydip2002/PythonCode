class Animal:
    def __init__(self,animal_Name,animal_Color):
        self.animal_Name = animal_Name
        self.animal_color = animal_Color
    
    def aboutAnimal(self):
        print(f"Animal Name is {self.animal_Name} and color is {self.animal_color}")

class Mammal:
    def __init__(self,mammal_name):
        self.mammal_name = mammal_name
        # self.color = color

    def aboutMammal(self):
        print(f"Mammal Name is {self.mammal_name}")

class DerivedAnimalClass(Animal,Mammal):
    def accessMammalData(self):
        print("This is Derived Class")


obj = DerivedAnimalClass("Cat","Mammal")
obj.aboutAnimal()
obj.accessMammalData()
obj1 = Mammal("Snake")
obj1.aboutMammal()
