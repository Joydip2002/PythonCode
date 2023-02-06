class Employee:
    company = "Google"

    
    def showDetails(self,name):
        print(f"Name is {name} who worked at {self.company}")

    @classmethod
    def classMethod(self):
        self.company = "Apple"
        print(f"Change Company Name by the classmethod decorators is {self.company}")

    @staticmethod
    def staticMethod():
        print("I am Static Method")

e1 = Employee()
print(e1.company)
# Employee.showDetails(e1,"Joydip")  #Another Way Called Instance
e1.showDetails("Joydip")
e1.classMethod()
print(e1.company)

Employee.staticMethod()