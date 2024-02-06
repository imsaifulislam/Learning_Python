""" email = input("Enter your EMail: ")
index = email.index("@")

userName = email[:index]
doMain = email[index+1:]

print(f"Your UserName Is {userName}\ndoamin is {doMain}") """



# ======================================

# -> User input
email = input("Enter Your email: ")

indexOfEmail = email.index("@")

userNameOfEmail = email[:indexOfEmail]
doaminOfEmail = email[indexOfEmail+1:]

print(f"Your Email Is : {userNameOfEmail}\nYour Domain Is : {doaminOfEmail}")