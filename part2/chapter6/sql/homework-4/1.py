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

	make_and_models = {
		'Mustang':"SELECT COUNT(make) FROM orders WHERE model = 'Mustang'",
		'Civic':"SELECT COUNT(make) FROM orders WHERE model = 'Civic'",
		'Fusion':"SELECT COUNT(make) FROM orders WHERE model = 'Fusion'",
		'Accord':"SELECT COUNT(make) FROM orders WHERE model = 'Accord'",
		'Explorer':"SELECT COUNT(make) FROM orders WHERE model = 'Explorer'"
	}


	for key, value in make_and_models.iteritems():
		cursor.execute(value)
		results = cursor.fetchone()
		print key, results[0]

