# SELECT statement

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	# use a for loop to iterate through the database, printing the results line by line
	for row in cursor.execute("SELECT firstname, lastname from employees"):
		print row
