""" 
set
    *-> Unique Value Store kore, Double Value theke singel Value ney
"""


num1 = [1, 2, 3, 4, 5, 6, 5, 7, 8, 9]
# print(num1)
num2 = {1, 2, 3, 4, 5, 6, 5, 7, 8, 9}
# print(num2)

empty = set(num1)
print(empty)
empty.add(55)
empty.remove(4)
print(empty)
print(len(empty))