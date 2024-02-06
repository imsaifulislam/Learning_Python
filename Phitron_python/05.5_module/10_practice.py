set1 = {10, 20, 30,60}
set2 = {20, 40, 50,80}

set1.difference_update(set2)
print(set1)

set2.difference_update(set1)
print(set2)