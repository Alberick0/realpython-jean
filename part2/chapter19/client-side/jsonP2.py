__author__ = 'alberick'
import json

data = json.load(open('cars.json'))
print data[0]['CAR'][0]['MAKE']