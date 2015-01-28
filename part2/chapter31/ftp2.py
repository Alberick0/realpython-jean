__author__ = 'alberick'
import ftplib
import sys

server = 'ftp.debian.org'
username = 'anonymous'
password = 'anonymous'

# Defines the name of th file for download
# file_name = sys.argv[1]
file_name = 'README.html'

# Initialize and pass in FTP URL and login credentials
ftp = ftplib.FTP(server, username, password)
ftp.cwd('debian')

# Create a local file with the same name as the remote file
with open(file_name, 'wb') as f:
    # Write the contents oof the remote file to the local file
    ftp.retrbinary('RETR ' + file_name, f.write)

# Close the connection
ftp.quit()
