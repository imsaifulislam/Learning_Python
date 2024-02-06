""" def NumberToAbs():
    a = int(input("First Number : "))
    b = int(input("Second Number : "))
    c = int(input("Third Number : "))

    abs_a = a if a >= 0 else -a
    abs_b = b if b >= 0 else -b
    abs_c = c if c >= 0 else -c


    print(f"absolute value of {a} is {a}")
    print(f"absolute value of {b} is {b}")
    print(f"absolute value of {c} is {c}")


NumberToAbs() """


# num to abs

def numToAbs():
    a = int(input("Enter 1st Number : "))
    b = int(input("Enter 2nd Number : "))
    c = int(input("Enter 3rd Number : "))

    a_abs = a if a >= 0 else -a
    b_abs = b if b >= 0 else -b
    c_abs = c if c >= 0 else -c

    print(f"Absolute value is {a_abs}")
    print(f"Absolute value is {b_abs}")
    print(f"Absolute value is {c_abs}")
    

numToAbs()