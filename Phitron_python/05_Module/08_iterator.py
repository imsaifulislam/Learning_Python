""" listIs = [1,2,3,4]
print(iter(listIs))
print(iter(listIs)) """

numbers = [12,45,65,23,83,79,22]
num_iter  = iter(numbers)
try:
    print(num_iter)
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
    print(next(num_iter))
except StopIteration:
    print("Stor Iterator")