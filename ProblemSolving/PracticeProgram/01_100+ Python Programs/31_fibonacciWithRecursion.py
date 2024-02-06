# Display Fibonacci Sequence Using Recursion | Python Program
""" 
    --> Fibonacci Sequence 0,1,1,2,3,5,8,13
    --> 
"""


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


n = int(input("Enter a Number Here : "))

if n <= 0:
    print("Enter positive Number")
else:
    print("Fibonacci Sequence")
    for i in range(n):
        print(fibo(i))


# print(fibo(5))
