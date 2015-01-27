__author__ = 'alberick'

import pymongo

# Open the MongoDB connection
conn = pymongo.Connection('mongodb://localhost:27017')

# print the available MongoDB databases
databases = conn.database_names()
for db in databases:
    print db

# Close the MongoDB connection
conn.close()