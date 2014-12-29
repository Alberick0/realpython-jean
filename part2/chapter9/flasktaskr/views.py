# views.py

from flask import Flask, flash, redirect, render_template, request, session, url_for, g
from functools import wraps
from forms import AddTaskForm
import sqlite3

app = Flask(__name__)
app.config.from_object('config')


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return test(*args, **kwargs)
        else:
            flash("Please login first")
            return redirect(url_for('login'))

    return wrap


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You are logged out")
    return redirect(url_for('login'))


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials'
            return render_template('login.html', error=error)
        else:
            session['logged_in'] = True
            return redirect(url_for('tasks'))
    if request.method == 'GET':
        return render_template('login.html')


@app.route('/tasks/')
@login_required
def tasks():
    g.db = connect_db()
    cursor = g.db.execute('SELECT name, due_date, priority, task_id FROM tasks WHERE STATUS=1')
    open_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cursor.fetchall()]
    cursor = g.db.execute('SELECT name, due_date, priority, task_id FROM tasks WHERE STATUS=0')
    closed_tasks = [dict(name=row[0], due_date=row[1], priority=row[2], task_id=row[3]) for row in cursor.fetchall()]
    return render_template('tasks.html', open_tasks=open_tasks, closed_tasks=closed_tasks,
                           form=AddTaskForm(request.form))


# Add new tasks:
@app.route('/add/', methods=['POST'])
@login_required
def new_task():
    g.db = connect_db()
    name = request.form['name']
    date = request.form['due_date']
    priority = request.form['priority']
    if not name or not date or not priority:
        flash("All fields are required. Please try again.")
        return redirect(url_for('tasks'))
    else:
        g.db.execute("INSERT INTO tasks (name, due_date, priority, status) VALUES (?,?,?,1)",
                     [request.form['name'], request.form['due_date'], request.form['priority']])
        g.db.commit()
        g.db.close()
        flash("New entry was successfully posted. Thanks.")
        return redirect(url_for('tasks'))


# Mark tasks as complete:
@app.route('/complete/<int:task_id>/', )
@login_required
def complete(task_id):
    g.db = connect_db()
    g.db.execute('UPDATE tasks SET status = 0 WHERE task_id=' + str(task_id))
    g.db.commit()
    g.db.close()
    flash("Task was marked as complete")
    return redirect(url_for('tasks'))


# Delete Tasks:
@app.route('/delete/<int:task_id>/', )
@login_required
def delete_entry(task_id):
    g.db = connect_db()
    g.db.execute('DELETE FROM tasks WHERE task_id=' + str(task_id))
    g.db.commit()
    g.db.close()
    flash('The task was deleted')
    return redirect(url_for('tasks'))