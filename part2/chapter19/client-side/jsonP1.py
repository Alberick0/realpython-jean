__author__ = 'alberick'
import json

# decode the json file
data = json.load(open('cars.json'))
print data
print json.dumps(data, indent=4, sort_keys=True)