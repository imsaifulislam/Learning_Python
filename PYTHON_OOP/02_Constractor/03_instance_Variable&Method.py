class car:
    def __init__(self,name,model):
        self.CarName = name        #instanve Variable 
        self.CarModel = model      #instanve Variable 
        self.CarWheel = 4          #instanve Variable 
        
    def carDetails(self):#instanve Method
        print(f"Car Name = {self.CarName}, Car Model ={self.CarModel}, Car Wheel = {self.CarWheel}")

# ==============================================

car1 = car("BMW",2016)
car2 = car("Audi",2018)
car1.carDetails()
car2.carDetails()