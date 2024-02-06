email = input("Enter your EMail: ")
index = email.index("@")

userName = email[:index]
doMain = email[index+1:]

print(f"Your UserName Is {userName} and doamin is {doMain}")