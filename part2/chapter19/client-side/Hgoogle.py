__author__ = 'alberick'
import requests
from xml.etree import ElementTree as et

directions = ['San+Francisco', 'Los+Angeles', 'False', 'driving']
url = 'http://maps.googleapis.com/maps/api/directions/xml?origin={0[0]}&destination={0[1]}' \
      '&sensor={0[2]}&mode={0[3]}'.format(directions)

response = requests.get(url)

with open('google.xml', 'wb') as code:
    code.write(response.content)

data = et.parse('google.xml')

for step in data.findall('route/leg/step/html_instructions'):
    print step.text
