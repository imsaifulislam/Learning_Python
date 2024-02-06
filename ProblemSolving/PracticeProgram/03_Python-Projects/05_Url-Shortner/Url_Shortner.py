# pip install pyshorteners
# pip install pyperclip

import pyshorteners
import webbrowser
import time

url = input("Enter The url : ")


def shotenurl(url):
    s = pyshorteners.Shortener()
    print("Here Is Short URL: ", s.tinyurl.short(url))


shotenurl(url)
time.sleep(5)
webbrowser.open(url)
