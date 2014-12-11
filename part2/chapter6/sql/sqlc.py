import sqlite3

with sqlite3.connect("new.db") as connection:
	cursor = connection.cursor()

	# Insert multiple records using a tuple
	cities = [
		("Boston", "MA", 600000),
		("Chicago", "IL", 2700000),
		('Houston', 'TX', 2100000),
		('Phoenix', 'AZ', 1500000)
	]

	# insert data into the table
	cursor.executemany("INSERT INTO population VALUES(?,?,?)", cities)