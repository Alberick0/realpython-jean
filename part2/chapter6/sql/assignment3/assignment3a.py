import sqlite3
from random import randint

with sqlite3.connect("newnum.db") as connection:
	cursor = connection.cursor()

	cursor.execute("DROP TABLE if exists numbers")
	cursor.execute("CREATE TABLE numbers(num INT)")

	for i in range(100):
		cursor.execute("INSERT INTO numbers VALUES(?)",(randint(0,100),))
