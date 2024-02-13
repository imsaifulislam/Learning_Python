""" class student:
    __name = "Shanto"

obj = student()
print(obj.__name) """

# =================

""" class student:
    __name = "Shanto"
    
    def __init__(self):
        print(self.__name)

obj = student() """

# =================

# = privat Method
""" class student:
    __name = "Shanto"
    
    def __init__(self):
        print(self.__name)
        self.__displayInfo()
    
    def __displayInfo(self):
        print("Private Methods")

obj = student() """

# obj.__displayInfo()

# ================================


class Student:
    __name = "Shanto" #-> Private Variable
    
    def __init__(self):
        print(self.__name) #-> Private Variable Call
        self.__displayInfo() #-> Call Private  Method
        
    # -> Private Method
    def __displayInfo(self):
        print("Private <😉/> Method")
        
    
obj = Student()
# print(obj.__name)