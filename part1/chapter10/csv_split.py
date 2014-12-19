import os
import csv
import argparse

chunks = []
temp_list = []

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", required=True,
                    help="csv input file (with extension)", type=str)
parser.add_argument("-o", "--output_file", required=True,
                    help="csv output file (without extension)", type=str)
parser.add_argument("-r", "--row_limit", required=True,
                    help="row limit to split csv at", type=int)
args = parser.parse_args()



def validate_file(file_name):
    return os.path.exists(file_name) 


def file_reader(file_name):
    with open(file_name, 'rb') as my_file:
        reader = csv.reader(my_file)

        for row in reader:
            temp_list.append(row)


def validate_rows(file_name, rows_split):
        if len(temp_list[1:]) >= rows_split:
            return True
        else:
            return False


def row_splitter(rows_split):
    start = 1
    end = rows_split
    
    for chunk in range(len(temp_list) / rows_split):
        chunks.append([])
        chunks[chunk].extend(temp_list[start:end + 1])
        start += rows_split
        end += rows_split


def file_writer(output_name):
    for chunk in chunks:
        with open(output_name + '-{}.csv'.format(chunks.index(chunk)), 'wb') as my_file:
            writer = csv.writer(my_file)
            writer.writerow(temp_list[0])
            writer.writerows(chunk)


def csv_split(args):
    file_name = args.input_file
    rows_split = args.row_limit
    output_name = args.output_file

    if not validate_file(file_name) == True:
        print 'File does not exist, please check and try again'
        return None

    file_reader(file_name)

    if not validate_rows(file_name, rows_split) == True:
        print 'Error. File {} only has {} rows, invalid split number "{}"'.format(file_name, len(temp_list[1:]), rows_split)
        return None

    row_splitter(rows_split)
    file_writer(output_name)

csv_split(args)

