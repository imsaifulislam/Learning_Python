class cat:
    def __init__(self,color,action):
        self.color = color
        self.action = action
    
    def view(self):
        print(f"{self.color} Color Cat and its {self.action}")
    
    def compare(self,CompCatAction):
        if self.action == CompCatAction.action:
            print("Both Are Same Action",CompCatAction.action)
        else:
            print("They Are Different")
        

cat1 = cat("Brown","Running")
cat1.view()
print(cat1)

print("\n===========================\n")

cat2 = cat("White","Jumping")
cat2.view()
print(cat1)

print("\n===========================\n")

cat1.compare(cat2)