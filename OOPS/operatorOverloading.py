class Vector:
    def __init__(self,i,j,k) -> None:
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self) -> str: #dander method
        return f"{self.i}i + {self.j}j + {self.k}k"

    def __add__(self,x) -> None:
        # return (f"{self.i + x.i}i + {self.j + x.j}j + {self.k }k")  #type str
        return Vector(self.i + x.i , self.j + x.j , self.k + x.k) # type vector

obj1 = Vector(3,4,5)
print(obj1)
obj2 = Vector(2,6,5)
print(obj2)
print(obj1+obj2)