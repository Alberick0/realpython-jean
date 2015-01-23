__author__ = 'alberick'
from xml.etree import ElementTree as et

doc = et.parse('cars.xml')

# outputs make, mode, and cost of each car
for element in doc.findall("CAR"):
    print element.find('MAKE').text
    print element.find('MODEL').text
    print element.find('COST').text

