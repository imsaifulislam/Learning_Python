# 9-8 cache decorator, functools and partial function
#https://www.python-engineer.com/posts/functools-overview/
# https://docs.python.org/3/library/functools.html

import time
from functools import cache

@cache
def fib(n):
    if n<=1:
        return 1
    return fib (n-1) + fib(n-2)

start = time.time()
for i in range(37):
    print(i,fib(i))
    
    
end = time.time()
mili_seconds = (end-start)*1000
print("Time TooK : ", mili_seconds)

#* without Cache Time TooK :  10999.712944030762
#* With Cache Time TooK :  5.984067916870117

""" 
 * cache ব্যবহার করে একটা কোড দ্রুত রান করা যায়।

"""