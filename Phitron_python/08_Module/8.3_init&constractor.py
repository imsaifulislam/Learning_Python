class phone:
    
    menufacture = 'china'
    
    def __init__(self,brand,price,color):
        self.brand = brand
        self.price = price
        self.color = color
        
    def send_sms(self,text,number):
        print(f"Sending: {text} to {number}")


phone1 = phone("Realme",25000,"Green")
print(phone1.brand, phone1.price, phone1.color, phone1.menufacture)
phone1.send_sms("Hello World","01710561898")
