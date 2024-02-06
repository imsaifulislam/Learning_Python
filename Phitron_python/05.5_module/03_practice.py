""" 

list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd"]

"""


""" def add_lists_index_wide(list1, list2):
    result= []
    min_length = min(len(list1), len(list2))
    
    for i in range(min_length):
        result.append(list1[i]+list2[i])
        
    if len(list1)>len(list2):
        result.extend(list1[min_length:])
    else:
        result.extend(list2[min_length:])
    
    return result

list1 = ["M", "na", "i", "Bo"]
list2 = ["y", "me", "s", "nd", "Extra"]

result_list = add_lists_index_wide(list1, list2)
print("Resultant List:", result_list) """



""" def add_two_list_wisely(list1, list2):

    result = [] #-> empty List for add Data

    min_len = min(len(list1), len(list2)) #-> Check Min Length

    for i in range(min_len):
        result.append(list1[i]*list2[i])

    if len(list1) > len(list2):
        result.extend(list1[min_len:])
    else:
        result.extend(list2[min_len:])
    
    return result


# list1 = ["M","Na","i","sha"]
# list2 = ["y","me","s","nto"]
list1 = [1,5,6,9,8]
list2 = [1,5,6,9,8]

final_list = add_two_list_wisely(list1,list2)
print(final_list) """



""" def add_two_list_wisely(list1, list2):

    result = [] #-> empty List for add Data

    min_len = min(len(list1), len(list2)) #-> Check Min Length

    for i in range(min_len):
        result.append(list1[i]*list2[i])

    if len(list1) > len(list2):
        result.extend(list1[min_len:])
    else:
        result.extend(list2[min_len:])
    
    return result


# list1 = ["M","Na","i","sha"]
# list2 = ["y","me","s","nto"]
list1 = [1,5,6,9,8]
list2 = [1,5,6,9,8]

final_list = add_two_list_wisely(list1,list2)
print(final_list) """ 

# -> Add sum from 2 list

def CalculateFromListData(listA,listB):
    result = []
    
    min_len = min(len(listA),len(listB))
    
    for i in range(min_len):
        result.append(listA[i]+listB[i])
        
    if len(listA)>len(listB):
        result.extend(listA[min_len:])
    else:
        result.extend(listB[min_len:])
    
    return result

l1 = [1,2,3,4,5,8]
l2 = [3,4,5,6,7,1]

final_reslut = CalculateFromListData(l1,l2)
print(final_reslut)