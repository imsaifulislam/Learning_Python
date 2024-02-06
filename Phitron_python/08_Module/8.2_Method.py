""" class Phone:
    
    def call(self):
        print("Ring Ring Ring")
        
    def send_sms(self,number, text):
        sms = f"Sending SMS: {text} To: {number}"
        return sms

m1 = Phone()
m1.call()
x = m1.send_sms("01710561898", "Hello")
print(x) """

# ====================================

class Calculator:
    def add(self,a,b):
        print(a+b)
        
    def sub(self,a,b):
        print(a-b)
        
    def mul(self,a,b):
        print(a*b)
        
    def div(self,a,b):
        print(a/b)
        
x = Calculator()
x.add(10,20)
x.sub(10,20)
x.mul(10,20)
x.div(10,20)
    