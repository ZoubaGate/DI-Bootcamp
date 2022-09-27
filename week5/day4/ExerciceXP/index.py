import requests

response = requests.get("https://api.chucknorris.io/")
print(response["body"])