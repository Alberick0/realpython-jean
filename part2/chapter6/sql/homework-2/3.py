# coding=utf-8
"""
• Using the “inventory” table from the previous homework assignment, add ( INSERT )
5 records (rows of data) to the table. Make sure 3 of the vehicles are Fords while the
other 2 are Hondas. Use any model and quantity for each.
• Update the quantity on two of the records, and then output all of the records from the
table.
• Finally output only records that are for Ford vehicles.
"""

import sqlite3

with sqlite3.connect("../cars.db") as connection:
	cursor = connection.cursor()

	cursor.execute("SELECT * FROM INVENTORY WHERE Make = 'Ford'")

	results = cursor.fetchall()

	for row in results:
		print row[0], row[1], row[2]
