
""" def twoSome(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target - nums[i] == nums[j]:
                return [i,j]
    return None

test = [2,7,11,15]
target = 13

print(twoSome(test,target)) """

# ======================================

""" nums = [2,7,11,15]
target = 9

def twoSum(nums,target):
    hash_map = {}
    #=> i = index [0,1,2,3] , num = value [2,7,11,15]
    for i,num in enumerate(nums):
        # print(i)
        # print(num)
        if target - num in hash_map:
            return [hash_map[target-num],i] #-> has_map[2]
        hash_map[num]  = i
        
    return []
        
print(twoSum(nums,target)) """


# ==================================================================
"""

    
"""
nums = [2,7,11,15]
target = 17

def twoSum(nums,target):
    hash_map = {} #=> Empty Dictonary
    
    for i, num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num], i]
        hash_map[num] = i
    
    return []

print(twoSum(nums,target))