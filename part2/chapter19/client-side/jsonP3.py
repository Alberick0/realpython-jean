__author__ = 'alberick'
import json
import requests

url = "http://httpbin.org/post"
data = {"colors": [
    {"color":"red", "hex":"#f00"},
    {"color":"green", "hex":"#0f0"},
    {"color":"blue", "hex":"#00f"},
    {"color":"cyan", "hex":"#0ff"},
    {"color":"magenta", "hex":"#f0f"},
    {"color":"yellow", "hex":"#ff0"},
    {"color":"black", "hex":"#000"}
]}
headers = {"content-type": "application/json"}

# post data to the server
response = requests.post(url, data=json.dumps(data), headers=headers)
print response.status_code