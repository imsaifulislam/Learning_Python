class BankAccount:
    
    def __init__(self,amount,AceName):
        self.amount = amount
        self.name = AceName
        
        print(f"\nAcount Name = {self.name}\nAccount Blance = ${self.amount:.2f}")
    
    def get_blance(self):
        print(f"\n{self.name} Account Blance Have = ${self.amount:.2f}")
        
    def diposit(self,amount):
        self.amount = self.amount + amount
        print(f"\nDiposit Complete..")
        self.get_blance()