import requests
import tkinter as tk

import json



def getNews():
    api_key = "4a8d80e980854252b47d3a5602e7c39c",
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=4a8d80e980854252b47d3a5602e7c39c"
    news = requests.get(url).json()

    articles = news["articles"]

    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["title"])

    for i in range(10):
        my_news = my_news + str(i+1) + ". " + my_articles[i] + "\n"

    # print(my_news)
    label.config(text=my_news)

canvas = tk.Tk()
# canvas.geometry("900x600")
canvas.title("News App")

button = tk.Button(canvas, font=24, text="Reload", command=getNews)
button.pack(pady=20)

label = tk.Label(canvas, font=18, justify="left")
label.pack(pady=20)

getNews()
canvas.mainloop()
