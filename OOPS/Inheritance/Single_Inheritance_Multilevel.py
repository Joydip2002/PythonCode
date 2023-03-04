class Two_Wheeler:
    def color(self,c):
        print(f"Color is: {c}")
    def oil_Capacity(self,x):
        print(f"Oil Capacity is: {x} Liter")

class Four_Wheeler(Two_Wheeler):
    Four_Oli = 35
    print(f"Four Wheeler Oil Capacity is: {Four_Oli}")

class Eight_Wheeler(Four_Wheeler):
    Four_Oli = 65
    print(f"Eight Wheeler Oil Capacity is: {Four_Oli}")
# obj = Two_Wheeler()
# obj2 = Four_Wheeler()
obj3 = Eight_Wheeler()

# obj.color("Red")
# obj.oil_Capacity(20)
obj3.color("Black")
obj3.oil_Capacity(45)