# INSERT Command

# import the sqlite 3 library
import sqlite3

#create the connection object
conn = sqlite3.connect("new.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

# insert data
try:
	cursor.execute("INSERT INTO population VALUES('New York City', 'NY', 820000)")
	cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', 800000)")

	# commit the changes
	conn.commit()
except sqlite3.OperationalError:
	print "Oops! Something went wrong. Try again..."

# close the database connection
conn.close()

"""
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()
	c.execute("INSERT INTO test(~~~~~~)")
	c.execute("INSERT INTO test(~~~~~~)")
"""
