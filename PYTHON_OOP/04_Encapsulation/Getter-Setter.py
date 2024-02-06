class Student:
    def __init__(self):
        self.__name = "" #private Variable
    
    
    def getName(self):
        return self.__name
    
    def setName(self,name):
        self.__name = name

obj = Student()
obj.setName("Shanto")
print(obj.getName())