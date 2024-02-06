# Python Program to Find the Sum of Natural Numbers Using Recursion

def NNS(n):
    if n <= 1:
        return n
    else:
        return (n)+NNS(n-1)


n = int(input("Enter a Number : "))
if n <= 0:
    print("Enter a Positve Number")
else:
    print("The Sum of Natural Number Upto Given Number is ", NNS(n))
