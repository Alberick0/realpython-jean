# SELECT statement, remove unicode characters

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	cursor.execute("SELECT firstname, lastname from employees")

	# fetchall() retrieves all records from the query
	rows = cursor.fetchall()

	# outputs the rows to the screen row by row
	for r in rows:
		print r
