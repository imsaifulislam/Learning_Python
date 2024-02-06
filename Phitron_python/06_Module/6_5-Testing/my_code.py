import requests

api_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

def get_response(url):
    return requests.get(url)

if __name__ == "__main__":
    print(__name__)
    res = get_response(api_url)
    print(res)
    
""" 
 * tdd in software development
 -> https://www.youtube.com/watch?v=eAPmXQ0dC7Q
 * unit testing in software engineering
"""