import os
from pyPdf import PdfFileReader, PdfFileWriter

path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 12/Practice files'
input_file_name = os.path.join(path, 'The Emperor.pdf')
input_file = PdfFileReader(file(input_file_name, 'rb'))

merge_file_name = os.path.join(path, 'Emperor cover sheet.pdf')
merge_file = PdfFileReader(file(merge_file_name, 'rb'))

output_file_name = os.path.join(path, 'Output/The Covered Emperor.pdf')
pdf_writer = PdfFileWriter()

with file(output_file_name, 'wb') as output_file:
    pdf_writer.addPage(merge_file.getPage(0))

    for page in range(input_file.getNumPages()):
        pdf_writer.addPage(input_file.getPage(page))

    pdf_writer.write(output_file)

