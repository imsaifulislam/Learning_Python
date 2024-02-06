import requests
from bs4 import BeautifulSoup

# req = requests.get( "https://www.youtube.com/playlist?list=PLbGui_ZYuhigZkqrHbI_ZkPBrIr5Rsd5L")
req = requests.get("https://www.jcchouinard.com/web-scraping-with-beautifulsoup-in-python/")

soup = BeautifulSoup(req.text, "html.parser")

res = soup.findAll(id_ = "wp-block-heading")
print(res.prettify())
# print(res)
