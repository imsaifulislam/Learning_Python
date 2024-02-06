class BlanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount,accName):
        self.blance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' Cerated.\nBlance = ${self.blance:.2f}")
        
    def get_blance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.blance:.2f}")
        
    def diposit(self,amount):
        self.blance = self.blance + amount
        print("\nDiposit Complete..")
        self.get_blance()
    
    def viableTransctions(self,amount):
        if self.blance >= amount:
            return
        else:
            raise BlanceException(
                f"\nSorry, Account'{self.name}' only have a blance of ${self.blance:.2f} "
            )    
            
    def withdraw(self,amount):
        try:
            self.viableTransctions(amount)
            self.blance = self.blance - amount
            print("\nWithdraw Complete.")
            self.get_blance()
        except BlanceException as error:
            print(f"\nWithdraw Interrupted: {error}")
            
    def transfer(self,amount, account):
        try:
            print('\n**********\n\nBeginning Transfer.. 🚀')
            self.viableTransctions(amount)
            self.withdraw(amount)
            account.diposit(amount)
            print('\nTransfer Complete! ✅\n\n**********')
        except BlanceException as error:
            print(f"\nTransder Interrupted. ❌ {error}")
            
class InterestRewardsAcct(BankAccount):
    def diposit(self, amount):
        self.blance = self.blance + (amount * 1.05)
        print("\nDiposit Complete.")
        self.get_blance()
        

class savingsAcct(InterestRewardsAcct):
    def __init__(self, initalAmmount, accName):
        super().__init__(initalAmmount, accName)
        self.fee = 5
    
    def withdraw(self, amount):
        try:
            self.viableTransctions(amount + self.fee)
            self.blance = self.blance - (amount + self.fee)
            print("\nWithdraw Complete.")
            self.get_blance()
        except BlanceException as error:
            print(f"\nWithdraw Interruptrd: {error}")