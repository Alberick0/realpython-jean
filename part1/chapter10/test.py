import os
import csv

path = '/home/alberick/Documents/python/books/realpython-jean/part1/book1-exercises/Course materials/Chapter 10/Practice files'

# Read in a CSV and display each row except the header row

# Append a third column and write out the resulting CSV with a new header

in_file_path = os.path.join(path, "pastimes.csv")
out_file_path = os.path.join(path, "pastimes.csv")


with open(in_file_path, "rb") as in_file, open(out_file_path, "wb") as out_file:

    csv_reader = csv.reader(in_file)

    csv_writer = csv.writer(out_file)



    # skip header row and write a new output header row


    csv_writer.writerow(["Name", "Favorite Pastime", "Type of pastime"])



    for row in csv_reader:

        print row

        # Check if "Favorite Pastime" includes "fighting"

        if row[1].lower().find("fighting") != -1:

            row.append("Combat")

        else:

            row.append("Other")

        # Add the new row to the output

        csv_writer.writerow(row)
