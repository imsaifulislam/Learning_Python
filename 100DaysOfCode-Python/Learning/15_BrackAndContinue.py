"""
    -> Brack        => Stop Loop
    -> Continue     =>
"""

""" for i in range(12):
    if (i == 10):
        break
    print("5 X ", i+1, "=", 5*(i+1)) """

""" for i in range(12):
    if (i == 10):
        print("Skip the iteration")
        continue
    print("5 X ", i, "=", 5*i) """
    

for i in range(1,101,1):
    print(i, end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you.")
