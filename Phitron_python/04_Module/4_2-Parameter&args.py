""" 
    * --< Args
"""


""" def multipluy(*number):
    result = 1
    for num in number:
        result = result*num
    return result


final_Result = multipluy(5, 2, 2)
print(final_Result) """


""" def multipluy(*number):
    # result = 1
    print(number)
    # for num in number:
    #     print(num)
    # return result


final_Result = multipluy(5, 2, 2) """
# print(final_Result)


def add(num1, num2):
    total = num1 + num2
    # print(num1, num2)
    print(f"num1: {num1} , num2: {num2}")
    return total

# result = add(10, 20)
# result = add(num2=10, num1=20)
# #-> এভাবে করে আরগুমেন্ট এর জন্য পেরামিটার এ ডাটা দেওয়া যায়।


# ------------------------------
""" 
    * perameter এর মধ্যে মান দিতে না চাইলে, arguments এর মধ্যে মান ১ দিতে হবে। তাহলে ERROR আসবে না। 

"""


""" def multiply(num1, num2=1):
    result = num1*num2
    return result


output = multiply(45)
print(output) """

# ---------------------------------------------------


def multiply(*number):
    # print(number )
    # return result
    result = 1
    for i in number:
        result = result * i
    return result


output = multiply(45, 20, 10)
print(output)
