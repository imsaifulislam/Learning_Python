""" 

Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value
Hints: Search about dict() function

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

Expected Output:
{'Ten': 10, 'Twenty': 20, 'Thirty': 30}


"""

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

final_dict = dict(zip(keys,values))
print(final_dict)