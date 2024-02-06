""" 
    * Dunder Method : 
"""

""" class person:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money
    
    def __add__(self,other):
        # return self.money + other.money
        return self.age + other.age
        
axy = person("shanto",23,2000)
axz = person("shan",20,20000)
print(axy + axz) """



# **********************************

class Fruits:
    def __init__(self,name:str) -> None:
        self.name = name
    
    def __mul__(self, other:int) -> str:
        return self.name * other
    
    def __len__(self) -> int:
        return len(self.name)
    
    def __str__(self)->str:
        return self.name
    
    
banana: Fruits = Fruits('Banana')
# print(banana*4)
# print(banana.__mul__(4))
print(str(banana))