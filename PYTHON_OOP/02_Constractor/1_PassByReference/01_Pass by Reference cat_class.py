class Cat:
    
    def __init__(self,color,action):
        self.color = color
        self.action = action
        
    def view(self):
        print(self.color, "Cat is", self.action)
        
    def compare(self,ct):
        if self.action == ct.action:
            # print("Both Cats are", self.action)
            print("Both Cats are", ct.action)
        else:
            print("They Are Diffferent")

# ===========================================================>

Cat1 = Cat("Brown","Jumping")
Cat1.view()
Cat2 = Cat("White","Running")
Cat2 = Cat("White","Jumping")
Cat2.view()

# => Pass by Reference 
Cat1.compare(Cat2)
