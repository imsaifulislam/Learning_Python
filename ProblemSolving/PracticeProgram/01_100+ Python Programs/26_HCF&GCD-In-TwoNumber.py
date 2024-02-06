def findHCFinTwoNumber(x, y):
    if (x > y):
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


def findHCFinThreeNumber(x, y, z):
    if (x > y):
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0) and (z % i == 0)):
            hcf = i
    return hcf


x = 12
y = 30
print("the Hcf of the given two numbers is ", findHCFinTwoNumber(21, 25))
print("the Hcf of the given two numbers is ", findHCFinThreeNumber(24, 40, 56))

# https://www.askpython.com/python/examples/hcf-and-lcm-in-python