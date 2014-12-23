import sqlite3
from config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                         name TEXT NOT NULL,
                                         due_date TEXT NOT NULL,
                                         priority INTEGER NOT NULL,
                                         status INTEGER NOT NULL)""")

    cursor.execute('INSERT INTO tasks VALUES(1,"Finish this tutorial", "02/03/2014", 10, 1)')
    cursor.execute('INSERT INTO tasks VALUES(2, "Finish Real Python Course 2", "02/03/2014", 10, 1)')
