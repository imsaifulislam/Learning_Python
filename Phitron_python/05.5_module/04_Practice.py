""" 
Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order
Hints: Search google about zip() function

Sample Input: 
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

Sample Output:
10 400
20 300
30 200
40 100

"""

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

result_list = zip(list1,reversed(list2))
print(list(result_list))

for i, j in zip(list1, reversed(list2)):
    print(i,j)
    
