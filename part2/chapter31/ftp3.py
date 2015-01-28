__author__ = 'alberick'
import ftplib
import sys

server = 'localhost'
username = ''
password = ''

# defines the file to upload
# file_name = sys.argv[1]
file_name = ''

# Initialize and pass in FRP URL and login credentials
ftp = ftplib.FTP(server, username, password)

# Opens the local file to upload
with open(file_name, 'rb') as f:

    # Write the contents of the local file to the remote file
    ftp.storbinary('STOR ' + file_name, f)

# Closes the connection
ftp.quit()
