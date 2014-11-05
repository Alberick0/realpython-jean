import os
import csv

score_list = dict()

file_path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 10/Practice files'

with open(os.path.join(file_path, 'scores.csv'), 'rb') as my_file:
    reader = csv.reader(my_file)
    for name, score in reader:
        if not score_list.has_key(name):
            score_list[name] = score
        else:
            if int(score_list[name]) < int(score):
                score_list[name] = score

for name, value in sorted(score_list.iteritems()):
    print name, value

