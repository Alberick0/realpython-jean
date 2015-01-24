__author__ = 'alberick'

import requests
import json

directions = {'origin': 'Central Park',
              'destination': 'Times Square',
              'sensor': False,
              'mode': 'walking'}

url = 'http://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}' \
      '&sensor={sensor}&mode={mode}'.format(origin=directions['origin'],
                                            destination=directions['destination'],
                                            sensor=directions['sensor'],
                                            mode=directions['mode'])

response = requests.get(url)

with open('google.json', 'wb') as gfile:
    gfile.write(response.content)

data = json.load(open('google.json'))

for route in data['routes']:
    for leg in route['legs']:
        for step in leg['steps']:
            print step['html_instructions']
