# In python, you can Assign a function to a variable
# then you can pass that variable in other function
# as argument, 

# def add(a,b): #-> add fucntion
#     return a+b

# def sub(a,b): #-> sub fucntion
#     return a-b

# def mult(a,b): #-> mul fucntion
#     return a*b

""" 
    func => Function Variable
    func(a,b) => Variable name is used to Call the function
"""
# def calc(func,a,b):
#     res = func(a,b)
#     print(res)
    
# # => Assigning Functions to the Variable
# a = add #Assign add function to a Variable
# s = sub #Assign sub function to a Variable
# m = mult #Assign mult function to a Variable

# calc(a,1,2) #Passing a to calc
# calc(s,1,2) #Passing s to calc
# calc(m,1,2) #Passing m to calc

# =================================================


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def calc(func, a,b):
    result = func(a,b)
    print(result)

a = add
s = sub
m = mult

calc(a,10,20)
calc(s,10,20)
calc(m,10,20)







""" 
এই কোডটি একটি সহজ ক্যালকুলেটর ডেমোনস্ট্রেশন করে, যা বিভিন্ন গণিত অপারেশন পারফরম করতে ব্যবহার হচ্ছে এবং ফাংশনগুলি ভ্যারিয়েবলগুলির সাথে যোগাযোগ করা হচ্ছে। নিচে প্রতিটি অংশ এবং কোডে ব্যবহৃত ভাষা বাংলায় বিশদভাবে ব্যাখ্যা করা হয়েছে:

1. **ফাংশন ডিফাইনিশন:**
    ```python
    def add(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    ```

    এখানে, তিনটি ফাংশন (`add`, `sub`, এবং `mult`) ডিফাইন করা হয়েছে যারা যোগ, বিয়োগ, এবং গুণনের কাজ করতে সক্ষম। প্রতিটি ফাংশন দুটি প্যারামিটার (`a` এবং `b`) নেয় এবং প্রতিটি অপারেশনের ফলাফল প্রদান করে।

2. **হায়ার-অর্ডার ফাংশন:**
    ```python
    def calc(func, a, b):
        result = func(a, b)
        print(result)
    ```

    `calc` ফাংশনটি একটি হায়ার-অর্ডার ফাংশন, যা তিনটি প্যারামিটার নিয়ে যায়: `func` (একটি ফাংশন), `a`, এবং `b`। এটি প্রদানকৃত ফাংশন (`func`) দিয়ে প্রদত্ত আর্গুমেন্ট (`a` এবং `b`) দিয়ে কল করে, ফলাফলটি `result` ভ্যারিয়েবলে সংরক্ষণ করে এবং ফলাফলটি প্রিন্ট করে।

3. **ফাংশন এলিয়াস:**
    ```python
    a = add
    s = sub
    m = mult
    ```

    এখানে, এলিয়াস তৈরি করা হয়েছে (`a`, `s`, এবং `m`), যারা মোট `add`, `sub`, এবং `mult` ফাংশনগুলির জন্য ব্যবহার করা যাবে। এটি তাদেরকে ছোট নাম দিয়ে উল্লেখ করার জন্য অনুমতি দেয়।

4. **ফাংশন কল:**
    ```python
    calc(a, 10, 20)
    calc(s, 10, 20)
    calc(m, 10, 20)
    ```

    এই লাইনগুলি দেখাচ্ছে যেভাবে বিভিন্ন ফাংশনগুলি (`add`, `sub`, এবং `mult`) এবং আর্গুমেন্ট দিয়ে `calc` ফাংশনটি ব্যবহার করা হয়। এই অপারেশনগুলির ফলাফলগুলি প্রিন্ট করা হয়েছে।

5. **আউটপুট:**
    ```
    30
    -10
    200
    ```

    কোডের আউটপুট হলো যোগ, বিয়োগ, এবং গুণন অপারেশনগুলির ফলাফল, প্রদান করা ফাং

শন এবং আর্গুমেন্টগুলি ব্যবহার করে।

সারাংশে, এই কোডটি পাইথনে ফাংশনগুলি কোনও প্রথম-শ্রেণীক অবজেক্ট হিসেবে ব্যবহার করা হয়, যা তাদেরকে ভ্যারিয়েবল (`a`, `s`, এবং `m`) এ অ্যাসাইন করতে এবং অন্যান্য ফাংশন (`calc`) তাদের সাথে যোগাযোগ করতে এবং কল করতে সাধারিত করে।

"""




