class House:
    def __init__(self): #constractor
        self.window = 4 #Instance Variable
        self.door = 2 #Instance Variable
        
    def view(self): #instance Method
        print(self.window,"Widnwos", self.door, "Doors")
        
# =========================================================

house1 = House() #Creating Object
house1.window = 6 #Update Instance Variable value
house1.view()

house2 = House() #Creating Object
house2.door = 3 #Update Instance Variable value
house2.view()

