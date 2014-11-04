import os
import csv

myPath = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 10/Practice files'

with open(os.path.join(myPath, 'pastimes.csv'), 'rb') as myFile:
    reader = csv.reader(myFile)
    next(reader)
    print '\n'
    for Person, Favorite_pastime in reader:
        print '{} favorite pastime is {}'.format(Person, Favorite_pastime)

    print '\n'

    myFile.seek(0)
    next(myFile)
    for row in reader:
        print row

    print '\n'

    myFile.seek(0)
    for person, pastime in reader:
        if pastime.lower().find('fighting') >= 0:
            print '{} pastime includes "fighting" True'.format(person)

    print '\n'


'''
with open(os.path.join(myPath, 'pastimes.csv'), 'rb') as myFileRead:
    with open(os.path.join(myPath, 'pastimes.csv'), 'wb') as myFileWrite:
        myReader = csv.reader(myFileRead)
        myWriter = csv.writer(myFileWrite)
        myReader.next()
        myWriter.writerow(['test', 'testing', 'tested'])
        
'''

