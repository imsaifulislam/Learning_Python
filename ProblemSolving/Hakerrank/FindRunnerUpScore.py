n = 5
arr = [2, 3, 6, 6, 5]
arr.sort(reverse = True)

largest = arr[0]

for ele in arr[1: ]:
    if ele<largest:
        print(ele)
        break