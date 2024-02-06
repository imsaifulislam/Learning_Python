# partial Function in python

# import 
""" def gereter_than(a,b):
    return a>b

def make_comparator(n):
    return lambda a: a>n


num20 = make_comparator(20)
print(num20(10))
print(num20(30)) """
# x = partial

# ->********************

""" from functools import partial

def greater_then(a,b):
    return a>b

# greaterThen = partial(greater_then,10)
greaterThen = partial(greater_then,b=10)
greaterThen = partial(greater_then,a=19, b=10)
# print(greaterThen(20))
print(greaterThen()) """

# ------------------------------------

from functools import partial
# import datetime as dt
import pandas_datareader as web

# def get_stock_Data(ticker:str, start:str, end:str):
def get_stock_Data(ticker, start, end) -> str:
    return web.DataReader(ticker, "yahoo", start,end)


print(get_stock_Data("aapl", "1/1/2019","10/1/2019"))