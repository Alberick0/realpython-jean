__author__ = 'alberick'
import pysftp
import sys

server = ''
username = ''
password = ''

# Defines the name of the file to upload
file_name = sys.argv[1]

# Initialize and pass in SFTP URL and login credentials
sftp = pysftp.Connection(server, username, password)

# Upload file
sftp.put(file_name)

# Closes connection
sftp.close()
