__author__ = 'alberick'
import pysftp

server = '127.0.0.1'
username = 'vagrant'
password = 'vagrant'

sftp = pysftp.Connection(server, username, password)

# Get the directory and file listing
data = sftp.listdir()

# Closes the connection
sftp.close()

# Prints out the directories and file, line by line
for l in data:
    print l