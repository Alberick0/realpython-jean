# coding=utf-8

"""
• Using the COUNT() function, calculate the total number of orders for each make and
model.
• Output the car’s make and model on one line, the quantity on another line, and then
the order count on the next line. The latter is a bit difficult, but please try it first before
looking at my answer. Remember: Google-it-first!
"""

import sqlite3

with sqlite3.connect("../cars.db") as connection:
	cursor = connection.cursor()

	cursor.execute("""SELECT inventory.Make, inventory.Model, inventory.Quantity, orders.order_date FROM inventory
 INNER JOIN orders on inventory.model = orders.model""")
	results = cursor.fetchall()

	for row in results:
		print row[0], row[1]
		print row[2]
		print row[3]
		print

