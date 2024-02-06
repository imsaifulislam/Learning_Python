""" 1. Write a Python function to find the maximum of three numbers.
 """


def findMax(MaXA, MaxB, MaXC):
    if MaXA >= MaxB and MaXA >= MaXC:
        print("A Is Max Number", MaXA)
    elif MaxB >= MaXA and MaxB >= MaXC:
        print("B Is Max Number", MaxB)
    else:
        print("C Is Max Number", MaXC)

    return MaXA, MaxB, MaXC


def findMin(MinA, MinB, MinC):
    if MinA <= MinB and MinA <= MinC:
        print("A Is Min Number", MinA)
    elif MinB <= MinA and MinB <= MinC:
        print("B Is Min Number", MinB)
    else:
        print("C Is Min Number", MinC)

    return MinA, MinB, MinC


x1 = input("Enter a Number : ")
x2 = input("Enter b Number : ")
x3 = input("Enter c Number : ")
findMax(x1, x2, x3)
findMin(x1, x2, x3)
