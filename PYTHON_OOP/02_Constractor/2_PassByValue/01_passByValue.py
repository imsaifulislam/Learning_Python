class Cat:
    def __init__(self,color,action):
        self.color = color
        self.action = action
    
    def view(self,num,clr):
        num = num +5
        # clr1 = clr
        # clr1[0] = "Green"
        clr[0] = "Green"
        print("Method Inside: ", num)
        # print("Method Inside: ", clr1)
        print("Method Inside: ", clr)
        
# ===================================================

colors = ["Black","Red","Yellow","Blue"]
c1 = Cat("White","Jumping")

x = 55
c1.view(x,colors)
print("Method OutSide: ", x)
print("Method OutSide: ", colors)

""" 
    * এখানে [c1.view(x,colors)] x এর ভেলুটা Pass by Value হচ্ছে, এখানকার মান মেথডের বাহির থেকে পরিবর্তন করা যায়। 
    
    * খানে [c1.view(x,colors)] colors এর ভেলুটা Pass by Refarence হচ্ছে, তার জন্য মেথডের ভিতরে এবং বাহির থেকে এক্সেস করলে একি মান দেখাবে যেইটা মেথড এর ভিতরে করা হইছে। 
    
"""