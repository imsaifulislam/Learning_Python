""" 
 * Check Prime Number
  যদি কোন নাম্বার কে ১ এবং নিজেকে(১১) দিয়ে ভাগ করা ছাড়া অন্য কোণ নাম্বার দিয়ে ভাগ করা যায়না সেইটা প্রাইম নাম্বার। 
"""

num = int(input("Enter a Number : "))

if num == 1:
    print("Its not a Prime Number")
    
if num > 1 :
    for i in range(2,num):
        if num%i == 0:
            print("Its a Prime Number")
            break
    else:
        print("Its prime number")