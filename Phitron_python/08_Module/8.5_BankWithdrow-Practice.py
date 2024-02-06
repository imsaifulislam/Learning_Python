""" class Bank:
    
    def __init__(self,balance):
        self.blance = balance
        self.min_withdraw = 100
        self.max_withdraw = 10000
    
    def get_blance(self):
        return self.blance
    
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            return f"No Money For You. Minmun withdraw: {self.min_withdraw}"
        elif amount > self.max_withdraw:
            return f"You Crossed Max Limit {self.max_withdraw}"
        elif amount > self.blance:
            return "You are Broke!! No money for you"
        else:
            self.blance = self.blance - amount
            return f"Here is your Money: {amount}"
        
    def diposit(self,amount):
        self.blance = self.blance + amount
        
my_bank = Bank(8000)
reply = my_bank.withdraw(900)
print(reply)

print(my_bank.get_blance())

my_bank.diposit(5000)
print(my_bank.get_blance())
         """
# ======================================================================
         
""" class Bank:
    
    def __init__(self,blance):
        self.blance = blance
        self.min_withdraw = 100
        self.max_withdraw = 1000
        
    def get_blance(self):
        return self.blance
    
    def withdraw(self,amount):
        
        if amount < self.min_withdraw:
            # * এমাউন্ট যদি মিনিমাল উথড্রো থেকে কম হয় তাহলে এইটা প্রিন্ট করবে
            return f"No Money For you. Minmun Withdraw {self.min_withdraw}"
        
        elif amount > self.max_withdraw:
            # * এমাউন্ট যদি মেক্সিমাম উথড্রো থেকে বেশি হয় তাহলে এইটা প্রিন্ট করবে
            return f"You Cross The Max Limit {self.max_withdraw}"
        
        elif amount > self.blance:
            # * এমাউন্ট যদি বেলেন্স থেকে বেশি হয়
            return "You Are Broke !!!"
        
        else:
            # * বেলেন্স থেকে এমাউন্ট তুল্লে যেইটা অবশিষ্ট থাকবে 
            self.blance = self.blance - amount
            return f"Here Is your Money: {amount}"
        
    def diposit(self,amount):
        self.blance = self.blance +amount 
        
            

my_bank = Bank(8000)
reply = my_bank.withdraw(5000)
print(reply)
print(my_bank.get_blance())

my_bank.diposit(500)
print(my_bank.get_blance()) """

# ======================================================================

""" 
    * Create A Class
    * instance variable --> blance, min, max Ammount
    *

"""
""" 
class Bank:
    
    def __init__(self,blance):
        self.blance = blance
        self.min_withdraw = 500
        self.max_withdraw = 25000
        self.ATM_charge = 15
        
    def get_blance(self):
        return f"You Have {self.blance - self.ATM_charge} Taka For Withdraw"
    
    def withdraw(self,amount):
        if amount < self.min_withdraw:
            return f"No Money! Minimum Withdraw is {self.min_withdraw}"
        elif amount > self.max_withdraw:
            return f"You Cross The Max Withdraw {self.max_withdraw}"
        elif amount > self.blance:
            return f"You Enter Wrong Ammount, Don't Have Enough Cash For Withdraw"
        else:
            self.blance = self.blance - amount
            return f"Withdraw Done ! Take You Cash {amount} Taka"
        
        
    def diposit(self,amount):
        self.blance = self.blance + amount
        return f"you Diposit {amount} Taka Is DONE :) Now You Blance is: {self.blance}"
    
    
customer1 = Bank(8000)

# print("=========== Withdraw DONE ============" )
# reply = customer1.withdraw(5000)
# print(reply)
# print(customer1.get_blance(), "\n")

# print("=========== DIPOSITE DONE ============" )
# diposits = customer1.diposit(500)
# print(diposits)
# print(customer1.get_blance())
 """
 
#  ===========================================================================
""" Create Banking Management System"""

class bank:
    
    def __init__(self,blance):
        self.Blance = blance
        self.min_withdraw = 500
        self.max_withdraw = 25000
        
    def Check_Blance(self):
        return self.Blance
    
    def withdraw(self,ammount):
        # chekc if ammount Less 
        pass


















