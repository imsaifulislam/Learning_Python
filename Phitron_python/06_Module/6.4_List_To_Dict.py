# => List to Dict
# https://builtin.com/software-engineering-perspectives/convert-list-to-dictionary-python
my_list = ['@F1','he@llo','@F2','World','@F3','python']
output_dict = {}

for index,val in enumerate(my_list):
    # print(index,val)
    
    if val[0] == '@':
        output_dict[val] = my_list[index+1]
    

print(output_dict)
    