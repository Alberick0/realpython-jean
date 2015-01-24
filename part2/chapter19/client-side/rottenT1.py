__author__ = 'alberick'
import sqlite3

with sqlite3.connect('rotten.db') as db:
    sor = db.cursor()

    # create table
    sor.execute("""CREATE TABLE new_movies(title TEXT, year INT, rating text, release text, runtime INT,
                                                         critics_review INT, audience_review INT)""")
