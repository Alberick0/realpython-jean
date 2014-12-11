# coding=utf-8
"""• Add another table to accompany your “inventory” table called “orders”. This table
should have the following fields: “make”, “model”, and “order_date”. Make sure to
only include makes and models for the cars found in the inventory table. Add 15 records
(3 for each car), each with a separate order date (YYYY-MM-DD).
• Finally output the car’s make and model on one line, the quantity on another line, and
then the order_dates on subsequent lines below that."""

import sqlite3

with sqlite3.connect("/home/alberick/Documents/python/books/realpython-jean/part2/chapter6/sql/cars.db") as connection:
	cursor = connection.cursor()

	cursor.execute("""SELECT DISTINCT inventory.Make, inventory.Model, inventory.Quantity, orders.order_date FROM inventory,orders WHERE inventory.Make = orders.make AND inventory.model = orders.model ORDER BY inventory.make ASC""")

	results = cursor.fetchall()

	for row in results:
		print "Make: {} and Model: {}".format(row[0], row[1])
		print "Quantity: {}".format(row[2])
		print "Order date: {}".format(row[3])
		print
