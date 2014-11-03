import os

myPath = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 10/Practice files/little pics'


for current_folder, subfolders, files_names in os.walk(myPath):
    for file_name in files_names:
        full_path = os.path.join(current_folder, file_name)
        if os.path.getsize(full_path) < 2000 and full_path.endswith('.jpg'):
            os.remove(full_path)
