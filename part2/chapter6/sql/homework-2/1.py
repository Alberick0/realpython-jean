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
	cars = [
		("Ford", "Mustang", 19),
		("Ford", "Explorer", 14),
		("Ford", "Fusion", 12),
		("Honda", "Civic", 20),
		("Honda", "Accord", 3)
	]

	cursor.executemany("INSERT INTO INVENTORY VALUES (?,?,?)", cars)
