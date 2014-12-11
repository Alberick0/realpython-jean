# import from CSV

# import the csv library
import csv
import sqlite3

path = '/home/alberick/Documents/python/books/realpython-jean/part2/book2-exercises/sql/employees.csv'

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	# open the csv file and assign it to a variable
	employees = csv.reader(open(path, "rU"))

	# create a new table called employees
	cursor.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	# insert data into the table
	cursor.executemany("INSERT INTO employees(firstname, lastname) VALUES (?,?)", employees)
