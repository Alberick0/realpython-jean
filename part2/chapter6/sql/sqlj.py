# JOINing data from multiple tables

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	# retrieve data
	cursor.execute("""SELECT population._ROWID_, population.city, population.population, regions.region
	FROM population, regions WHERE population.city = regions.city""")

	results = cursor.fetchall()

	for row in results:
		print row
