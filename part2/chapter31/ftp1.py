__author__ = 'alberick'

import ftplib

server = 'ftp.debian.org'
username = 'anonymous'
password = 'anonymous'

# Initialize and pass in FTP URL and login credentials (if applicable)
ftp = ftplib.FTP(host=server, user=username, passwd=password)

# Create a list to receive the data
data = []

# Append the directories and files to the list
ftp.cwd('debian')
ftp.dir(data.append)

# Close the connection
ftp.quit()

# Print out the directories and files, line by line
for l in data:
    print l