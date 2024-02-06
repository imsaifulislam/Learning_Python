""" 
    * ইউজার প্রথমে তার কত ডলার এর কাজ আছে সেইটা ডলার দিবে
    * এবার সেখান থেকে ২০% কেটে যা হইয় দেখাবে 
    * এবার সেই ডলার এর সাথে ক্লিয়ার হওয়া ডলার এখানে যোগ করবে কিনা সেইটা দেখাবে
    * এবার মুল ডলার টা টাকায় কনভার্ট করে দিবে
    
    * https://www.geeksforgeeks.org/currency-converter-in-python/
"""


def sumOfDoller():
    pass


MainOrderDoller = float(input("Enter Order Doller Emonunt : "))
afterFee = MainOrderDoller / 100 * 20
print("Total Order Doller Is : ", MainOrderDoller)
print("Fee 20% : ", afterFee)
print("Total Doller after Fee : ", MainOrderDoller - afterFee)