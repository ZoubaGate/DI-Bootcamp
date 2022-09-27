'''
    Using the requests and time modules, create a function which returns the amount of time it takes a webpage to load (how long it takes for a complete response to a request).
Test your code with multiple sites such as google, ynet, imdb, etc.
'''
#import requests module
import requests

#Making a get request
response = requests.get('http://www.google.com')

#print response
print(response)

#print elapsed time
print(response.elapsed)
