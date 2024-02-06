""" num = int(input("Enter The Rows: "))

for row in range(1,num+1):
    for col in range(1,row+1):
        print("*",end="")
    print(" ") """
    
num = int(input("Enter the Row: "))

for row in range(1,num+1):
    for col in range(1,row+1):
        print("*", end="") #-> Loop চলার পরে end="" লাইন ইন্ড করছে।
        # print("*", end="")
    print(" ") #-> Loop চলার পরে লাইন ব্রেক নিচ্ছে

""" 
    * প্রথেমে ইনপুট ৫ নেওয়া হলো
    * ১০ নাম্বার লাইনেঃ for row in range(1,num+1)
    *             |> এখানে num+1= ৬ ==< ১ থেকে ৫ পর্যন্ত চল্বে
    *             |> এখানে প্রথমে row থাকবে ১ ==< ট্র, তাই লুপ এর ভিতরে যাবে
    * ১১ নাম্বার লাইনঃ for col in range(1,row+1)
    *             |> এখানে row+1= ২ ==< ১
"""