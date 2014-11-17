import os
import copy
from pyPdf import PdfFileReader, PdfFileWriter

path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 12/Practice files'

input_file_name = os.path.join(path, 'Walrus.pdf')
input_file = PdfFileReader(file(input_file_name, 'rb'))

input_file.decrypt('IamtheWalrus')
output_PDF = PdfFileWriter()

for page_num in range(input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page.rotateCounterClockwise(90)
    page_left = page
    page_right = copy.copy(page)
    upper_right = page_left.mediaBox.upperRight
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)
    
output_file_name = os.path.join(path, 'Output/Walrus.pdf')

with file(output_file_name, 'wb') as output_file:
    output_PDF.write(output_file)
    output_file.close()

