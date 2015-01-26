__author__ = 'alberick'
import json
import requests
import sqlite3

KEY = ''
url = 'http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey={}'.format(KEY)

data = requests.get(url)
output = json.loads(data.content)
movies = output['movies']

with sqlite3.connect('rotten.db') as db:
    cur = db.cursor()

    # loop all the movies and insert the data in a new row in the db
    for movie in movies:
        cur.execute("INSERT INTO new_movies VALUES (?,?,?,?,?,?,?)",
                    (movie['title'],
                     movie['year'],
                     movie['mpaa_rating'],
                     movie["release_dates"]["theater"], movie["runtime"],
                     movie["ratings"]["critics_score"],
                     movie["ratings"]["audience_score"]))

    cur.execute("SELECT * FROM new_movies ORDER BY title ASC")

    for r in cur.fetchall():
        print r
