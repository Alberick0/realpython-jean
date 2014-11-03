import os
import glob

myPath = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 10/Practice files/images'

for element in os.listdir(myPath):
    print os.path.join(myPath, element)

print '\n'

for element in  glob.glob(myPath + '/*.png'):
    print element

print '\n'

for current_folder, subfolders, files_names in os.walk(myPath):
    for file_name in files_names:
        full_file = os.path.join(current_folder, file_name)
        if full_file.endswith('.png'):
            new_file = full_file.replace('.png', '.jpg')
            os.rename(full_file, new_file)

print '\n'

for current_folder, sub_folder, files_names in os.walk(myPath):
    for file_name in files_names:
        if file_name.endswith('.jpg'):
            full_path = os.path.join(current_folder, file_name)
            print os.path.exists(full_path)
