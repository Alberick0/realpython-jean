# This is the equivalent of a curl request
import requests

url = 'http://text-processing.com/api/sentiment/'
data = {'text': 'Good'}

result = requests.post(url, data)
print result.content

