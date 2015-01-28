__author__ = 'alberick'
import pysftp
import sys

server = ''
username = ''
password =''

# Defines the name of the file to download
file_name = sys.argv[1]

# Initialize and pass in SFTP URL and logins
sftp = pysftp.Connection(server, username, password)

# Download the file from the remote server
sftp.get(file_name)

# Closes connection
sftp.close()
