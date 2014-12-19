# blog.py - controller

# imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g
import sqlite3
import os
from functools import wraps  # this is used to extend capabilities of the functions with other functions

# configuration
DATABASE = "blog.db"
USERNAME = 'admin'
PASSWORD = 'pass'
SECRET_KEY = os.urandom(24)

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)

# function used for connection to the database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))

    return wrap


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
                        request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html')


@app.route('/main')
@login_required  # when the users request main it will hit first login_required function
def main():
    g.db = connect_db()  # connects to the database
    cur = g.db.execute("SELECT * FROM posts")  # fetches data from the posts table within the DB
    posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]  # assigns the data retrieved
    g.db.close()
    return render_template('main.html', posts=posts)  # passes that variable to the main.html file


@app.route('/logout')
def logout():
    session.pop('logged_in', None)  # this logs you out
    flash('You were logged out')  # stores a message to be called later by get_flashed_message()
    return redirect(url_for('login'))  # url_for provides the url for that function


@app.route('/add', methods=['POST'])
@login_required
def add():
    title = request.form['title']
    post = request.form['post']
    if not title or not post:
        flash("All fields are required. Please try again.")
        return redirect(url_for('main'))
    else:
        g.db = connect_db()
        g.db.execute('INSERT INTO posts (title, post) VALUES (?,?)',
                     [request.form['title'], request.form['post']])
        g.db.commit()
        g.db.close()
        flash("New entry was successfully posted")
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)  # This is starting the server
