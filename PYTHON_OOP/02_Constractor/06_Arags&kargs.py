# nums = [2,5,7,1,9]
# print(nums)
# print(*nums) #-> unpacking in python



""" def order_pizaa(size,*args):
    print(f"Ordered a {size} Pizaa.")
    print(args)

order_pizaa("Large","Pepperoni","Olives") """

""" def order_pizaa(size,*toppings):
    print(f"Ordered a {size} Pizaa with the following toppins:")
    for topping in toppings:
        print(f"- {topping}")

order_pizaa("Large","Pepperoni","Olives") """

# ===============> krgs

def order_pizaa(size,*toppings, **details):
    print(f"Ordered a {size} Pizaa with the following toppins:")
    
    for topping in toppings:
        print(f"- {topping}")
    # print(details)
    
    print("\nDetailes of the order are: ")
    for key,value in details.items():
        print(f"- {key}: {value}")

order_pizaa("Large","Pepperoni","Olives", delivery=True, tips=5)