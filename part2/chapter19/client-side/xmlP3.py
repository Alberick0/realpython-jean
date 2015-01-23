__author__ = 'alberick'
from xml.etree import ElementTree as et
import requests

# get an xml document from somewhere
xml = requests.get('http://www.w3schools.com/xml/cd_catalog.xml')

with open('response.html', 'wb') as code:
    code.write(xml.content)

doc = et.parse('response.html')

for element in doc.findall('CD'):
    print element.find('TITLE').text
    print element.find('ARTIST').text
    print element.find('YEAR').text, '\n'