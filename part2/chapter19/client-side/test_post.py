__author__ = 'alberick'
import requests

data = {'fname': 'Jean', 'lname': 'Guzman'}
url = 'http://httpbin.org/post'

r = requests.post(url, data)
print r.content
