""" 
     1 2 3 4
    ---------
1   |*| | | |
    ---------
2   |*|*| | |
    ---------
3   |*|*|*| |
    ---------
4   |*|*|*|*|
    ---------
    
    i => Row
    j => Column
"""

for i in range(1,5):
    for j in range(1,5):
        if j<=i:
            print("*",end="")
        else:
         print(" ",end="")
    print()

