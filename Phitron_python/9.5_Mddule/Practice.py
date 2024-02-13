""" class Student:
    def __init__(self,name,Roll):
        self.name = name
        self.Roll = Roll


student1 = Student("Shanto",35)
print(student1.name)     
print(student1.Roll)      """
# =====================================



class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity
        #* 4. Define a property that must have the same value for every class instance (object)
        self.Wheel = 6
    
    

class Bus(Vehicle):
    """ __sppedMax = 650
    
    def __init__(self):
        print("Max SPEED IS = ",self.__sppedMax) """
        
    def __init__(self,speedMax,speedMin):
        self.__maxSpeed = speedMax
        self.__minSpeed = speedMin
        
        
        


School_bus = Bus("School Volvo", 12, 50)
print(School_bus.name)
print(School_bus.mileage)
print(School_bus.capacity)
print(School_bus.Wheel)

# * ✅ Check the type of the object school_bus
# print(type( School_bus))

# * ✅ Check if School_bus is also an instance of the Vehicle class.
# print(isinstance(School_bus, Vehicle))