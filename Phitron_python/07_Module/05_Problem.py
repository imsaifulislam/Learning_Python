""" def create_list(): 
    d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
    listIs = []
    
    for i,j in enumerate(d):
        temp = [i,j]
        listIs.append(temp)
    
    print(listIs)

create_list() """



""" def create_list(): 
    d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
    listIs = list(d.items())
    
    print(listIs)

create_list() """



""" def create_list(): 
    d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
    listIs = []
    
    for index,val in enumerate(d):
        # print(index,val)
        if val[0] == d.keys():
            listIs[val] = listIs[index+1]
            # index.append(listIs)
            
    print(listIs)

create_list() """



""" d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
# list = list(d.items())
list = list(d.keys().values())
print(list) """


def create_list(ListIs):
    list_from_dict = []

    for key, value in ListIs.items():
        list_from_dict.append(key)
        list_from_dict.append(value)

    return print(list_from_dict)

d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}
create_list(d)