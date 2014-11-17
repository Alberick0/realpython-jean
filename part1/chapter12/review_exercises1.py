import os
from pyPdf import PdfFileReader, PdfFileWriter

path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 12/Practice files'
target_file_name = os.path.join(path, 'The Whistling Gypsy.pdf')
target_file = PdfFileReader(file(target_file_name, 'rb'))
book_info = target_file.getDocumentInfo().title, target_file.getDocumentInfo().author, target_file.getNumPages()

print '''The title of this pdf is "{0[0]}"
Author is {0[1]}
Total number of pages is{0[2]}'''.format(book_info)

print '\n'
print 'Exercise 2'

output_file_name = os.path.join(path, 'Output/The Whistling Gypsy.txt')
with open(output_file_name, 'wb') as output_file:

    for page in range(target_file.getNumPages()):
        text = target_file.getPage(page).extractText()
        output_file.write(text.encode('utf-8'))

print '\n'
print 'Exercise 3'

output_file_name = os.path.join(path, 'Output/The Whistling Gypsy.pdf')

with open(output_file_name, 'wb') as output_file:
    pdf_writer = PdfFileWriter()

    for page in range(1, target_file.getNumPages()):
        pdf_writer.addPage(target_file.getPage(page))

    pdf_writer.write(output_file)


