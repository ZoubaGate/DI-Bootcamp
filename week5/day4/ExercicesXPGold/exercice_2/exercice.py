import requests
url="https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
response = requests.get(url)
i=0
while i<10:
    print(response.json())
    i+=1