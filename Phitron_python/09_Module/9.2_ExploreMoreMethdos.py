from typing import Any


class peopleInfo:
    
    def __init__(self,name,Money, height = 65):
        self.name = name
        self.Money = Money
        self.height = height
    
    def __add__(self,other):
        return self.Money + other.Money
    
    def __mul__(self,other):
        return self.Money * other.Money
    
    def __call__(self):
        print( f"This is {self.name} with Money Have {self.Money}" )
        
    def __er__(self, other):
        return self.Money == other.Money
        
    def __len__(self):
        return self.height

p1 = peopleInfo("Shanto",500,75)
p2 = peopleInfo("Liza",700)

print(p1 + p2)
print(p1 * p2)

p1()
p2()

# print(45>12) #-> 5:33

print("Compare Two Objects : ",p1 == p2)

print(len(p1))