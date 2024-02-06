# 8-4 Static, class attribute, instance attriclass phone:
    
""" class phone:
    
    # -> Static / class attribute
    menufacture = 'china'
    
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
        
    def send_sms(self,text,number):
        print(f"Sending: {text} to {number}")


phone1 = phone("Realme",25000,"Green")
print(phone1.brand, phone1.price, phone1.color, phone1.menufacture)
phone1.send_sms("Hello World","01710561898") """


# ========================================================
# Class Attribute
""" 
    *
"""
""" class shop:
    cart =[]
    def __init__(self,buyer):
        self.buyer = buyer
        
    def add_to_cart(self,item):
        self.cart.append(item)
        
shopper_1 = shop('Shanto')
shopper_1.add_to_cart("T-shirt")
print(shopper_1.cart)
        
shopper_2 = shop('Shanto XYS')
shopper_2.add_to_cart("Shoe")
print(shopper_2.cart) """

# =====================================

class laptop:
    
    def __init__(self,brand,age):
        self.brand =brand
        self.age = age
        
    def incrage_age(self):
        self.last_age = self.age
        self.age = self.age+1
        
    def repair(self, life_incrace= -5):
        self.incrage_age = life_incrace
        
my_laptop = laptop("Asus",5)
# my_laptop.incrage_age()
# my_laptop.incrage_age()
# my_laptop.age = 17
# my_laptop.incrage_age()
# # print(my_laptop.last_age)
my_laptop.repair(-10)
print(my_laptop.age)