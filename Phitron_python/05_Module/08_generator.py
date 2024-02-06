numbers = [12, 45, 65, 23, 83, 79, 22]


""" def get_Number(nums):
    for num in nums:
        return num


result = get_Number(numbers)
print(result) """

def get_Number(nums):
    for num in nums:
        yield num


result = get_Number(numbers)
print(result)
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))

# https://www.datacamp.com/tutorial/python-iterators-generators-tutorial