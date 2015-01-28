__author__ = 'alberick'
import smtplib
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart

# inputs for from, to, subject and body text
fromaddr = raw_input("Sender's email: ")
toaddr = raw_input("To: ")
sub = raw_input('Subject: ')
text = raw_input("Body: ")

# email account info from where we'll be sending the email
smtp_host = ''
smtp_port = ''
user = ''
password = ''

# parts of the actual email
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = sub
msg.attach(MIMEText(text))

# connect to the server
server = smtplib.SMTP()
server.connect(smtp_host, smtp_port)

# initiate communication with server
server.ehlo()

# use encryption
server.starttls()

# login to the server
server.login(user, password)

# send the email
server.sendmail(fromaddr, toaddr, msg.as_string())

# close connection
server.quit()