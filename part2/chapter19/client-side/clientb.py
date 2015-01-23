__author__ = 'alberick'
import requests

r = requests.get('http://www.python.org')
with open('test_request.html', 'wb') as code:
    code.write(r.content)
