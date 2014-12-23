# config.py

import os

# grabs the folder there the script runs
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'pass'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret'

# defines the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)
