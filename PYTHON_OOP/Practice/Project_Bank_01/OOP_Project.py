from bank_account import * 

Shanto = BankAccount(1000,"Shanto")
liza = BankAccount(2000,"Liza")

# Shanto.get_blance()
# liza.get_blance()


# liza.diposit(500)
# Shanto.diposit(10000)

# Shanto.withdraw(10)

# Shanto.transfer(10000,liza)
# Shanto.transfer(100,liza)
# Shanto.get_blance()


# jim = InterestRewardsAcct(1000,"jim")
# jim.get_blance()
# jim.diposit(100)

# jim.transfer(100,Shanto)


blaze = savingsAcct(1000,"Blaze")
blaze.get_blance()
blaze.diposit(100)
blaze.transfer(100,Shanto)