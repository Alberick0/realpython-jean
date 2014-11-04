import os
import csv

my_path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 10/Practice files'

pastimes = [['Person', 'Favorite pastime']]

with open(os.path.join(my_path, 'pastimes.csv'), 'rb') as my_file:
    reader = csv.reader(my_file)
    next(reader)
    print '\n'
    for Person, Favorite_pastime in reader:
        print '{} favorite pastime is {}'.format(Person, Favorite_pastime)

    print '\n'

    my_file.seek(0)
    next(my_file)
    for row in reader:
        print row

    print '\n'

    my_file.seek(0)
    my_file.next()
    for person, pastime in reader:
        if pastime.lower().find('fighting') >= 0:
            row = [person, pastime, 'Combat']
            pastimes.append(row)
            print '{} pastime includes "fighting" True'.format(person)
        else:
            row = [person, pastime, 'Other']
            pastimes.append(row)
    print '\n'

with open(os.path.join(my_path, 'pastimes.csv'), 'wb') as my_file:
    writer = csv.writer(my_file)
    writer.writerows(pastimes)

with open(os.path.join(my_path, 'Output/categorized pastimes.csv'), 'wb') as my_file:
    writer = csv.writer(my_file)
    pastimes[0] = ['Name', 'Favorite Pastime', 'Type of Pastime']
    writer.writerows(pastimes)
