a = input("Enter Word Here : ")

rev = a[:: -1] #*slicing

if a == rev:
    print("Its a Palingdrome")
else:
    print("Its a Not Palingdrome")
