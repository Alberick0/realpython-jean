import sqlite3

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""
print prompt

operations = {1: "avg", 2: "max", 3: "min", 4: "sum"}

with sqlite3.connect("newnum.db") as connection:
	cursor = connection.cursor()

	while True:
		try:
			user_input = int(raw_input("Choose your operation: "))
		except ValueError:
			print "Invalid Input, try again"

		if user_input in operations:
			cursor.execute("SELECT {}(num) FROM numbers".format(operations[user_input]))
			print cursor.fetchone()[0]
		else:
			break


