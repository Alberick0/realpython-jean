from easygui import *
from pyPdf import PdfFileReader, PdfFileWriter

""" This programs reads a pdf file and splits it """

def read_file_name():
    """This function validates the chosen file to read"""
    while True:
        input_file_name = fileopenbox("Choose a PDF file", "File selector", "*.pdf")
        if input_file_name == None:
            print "bye"
            exit()
        elif not input_file_name.endswith(".pdf"):
            msgbox("File has to be PDF", "Choose again!")
        else:
            break
    return input_file_name


def validate_user_entry(pdf_pages):
    """ this function validates the page number the user inputs """
    while True:
        page_num = enterbox("Page number", "Choose the page number")
        try:
            page_num = int(page_num) 
        except ValueError:
            msgbox("Entry was not a number!", "Please introduce the page number")
        except TypeError:
            exit()
            if type(page_num) is int:
                break

        if page_num < 1 or page_num > pdf_pages:
            msgbox("File only has {pages} pages, try again!".format(pages=pdf_pages), "Invalid input")
        else:
            return page_num


def write_output(input_file_name,input_file, start_page, end_page):
    """ This function is in charge of selection the ouput file and writing it """
    while True:
        output_file_name = filesavebox("", "Save the file to?", "*.pdf")
        try:
            if input_file_name == output_file_name:
                msgbox("Output file can't be the same as the Input file")
            else:
                with open(output_file_name, 'wb') as output_file:
                    writer = PdfFileWriter()
                    for current_page in range(start_page, end_page):
                        page = input_file.getPage(current_page)
                        writer.addPage(page)
                    writer.write(output_file)
                break
        except TypeError:
            exit()


def open_file(input_file_name):
    """ This function reads the selected input file """
    input_file = PdfFileReader(file(input_file_name, 'rb'))
    pdf_pages = input_file.getNumPages()
    msgbox("Press 'OK' to continue", "What is the start page?")
    start_page = validate_user_entry(pdf_pages) - 1
    msgbox("Press 'OK' to continue", "What is the ending page?")
    end_page = validate_user_entry(pdf_pages) 
    write_output(input_file_name, input_file, start_page, end_page)


def run_program():
    """ This function opens the file to read """
    open_file(read_file_name())


# Program Main section
run_program()
