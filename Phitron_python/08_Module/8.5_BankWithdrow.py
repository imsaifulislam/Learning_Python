class Bank:
    
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
        