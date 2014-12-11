# coding=utf-8
"""• Add another table to accompany your “inventory” table called “orders”. This table
should have the following fields: “make”, “model”, and “order_date”. Make sure to
only include makes and models for the cars found in the inventory table. Add 15 records
(3 for each car), each with a separate order date (YYYY-MM-DD).
• Finally output the car’s make and model on one line, the quantity on another line, and
then the order_dates on subsequent lines below that."""

import sqlite3

with sqlite3.connect("../cars.db") as connection:
	cursor = connection.cursor()

	cursor.execute("CREATE TABLE orders(make TEXT, model TEXT, order_date DATE)")

	orders = [
		('Ford', 'Mustang', '2014-01-22'),
		('Ford', 'Mustang', '2014-01-23'),
		('Ford', 'Mustang', '2014-01-24'),
		('Honda', 'Civic', '2014-01-25'),
		('Honda', 'Civic', '2014-01-26'),
		('Honda', 'Civic', '2014-01-27'),
		('Ford', 'Fusion', '2014-01-28'),
		('Ford', 'Fusion', '2014-01-22'),
		('Ford', 'Fusion', '2014-01-23'),
		('Honda', 'Accord', '2014-01-24'),
		('Honda', 'Accord', '2014-01-25'),
		('Honda', 'Accord', '2014-01-26'),
		('Ford', 'Explorer', '2014-01-27'),
		('Ford', 'Explorer', '2014-01-28'),
		('Ford', 'Explorer', '2014-01-22'),
		]

	cursor.executemany("INSERT INTO orders VALUES (?,?,?)", orders)
	cursor.execute("SELECT * FROM orders")

	results = cursor.fetchall()

	for row in results:
		print row