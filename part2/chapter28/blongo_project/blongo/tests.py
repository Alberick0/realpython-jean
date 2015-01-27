from django.test import TestCase
import pymongo

# Create your tests here.

def get_collection(conn):

    dbs = conn.database_names()

    if 'blongo' in dbs:
        # connect to the db
        db = conn.blog

        # grab all collections
        collections = db.collection_names()

        # output all collections
        print "Collections"
        print "-----------"

        for collection in collections:
            print collection

        # pick a collection to view
        col = raw_input('\n Type in a collection to show the fields: ')

        if col in collections:
            get_items(db[col].find())
        else:
            print "Sorry. The '{}' collection doesn't exist".format(col)
    else:
        print "Sorry. The 'blongo' db doesn't exist"

    conn.close()

def get_items(collection_name):

    for items in collection_name:
        print items

if __name__ == '__main__':

    # Open the MongoDB connection
    conn = pymongo.Connection('mongodb://localhost:27017')
    get_collection(conn)