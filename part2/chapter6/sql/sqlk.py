# JOINing data from multiple tables - clean up

import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	cursor.execute("""SELECT DISTINCT population.city, population.population, regions.region FROM population,
regions WHERE population.city = regions.city ORDER BY population.city ASC""")

	results = cursor.fetchall()

	for row in results:
		print "City: ", row[0]
		print "Population: ", row[1]
		print "Region: ", row[2]
		print

