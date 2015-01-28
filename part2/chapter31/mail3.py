__author__ = 'alberick'
import imaplib

# email account info from where we'll be sending the email from
imap_host = ''
imap_port = ''
user = ''
password = ''

# login to the mail server
server = imaplib.IMAP4_SSL(imap_host, imap_port)
server.login(user, password)

# select the inbox
status, num = server.select('Inbox')

#fetch the email and the information you wish to display
status, data = server.fetch(num[0], '(BODY[TEXT])')

# print the results
print data[0][1]
server.close()
server.logout()