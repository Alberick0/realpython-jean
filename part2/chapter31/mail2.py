__author__ = 'alberick'

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def mail(fromaddr, toaddr, sub, text, smtp_host, smtp_port, user, password):

    # parts of the actual email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = sub
    msg.attach(MIMEText(text))

    # connect to the server
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)

    # initiate communication with server
    server.ehlo()

    # use encryption
    server.starttls()

    # login to the server
    server.login(user, password)

    # send the email
    server.sendmail(fromaddr, toaddr, msg.as_string())

    server.quit()

if __name__ == '__main__':
    fromaddr = ''
    toaddr = ''
    subject = ''
    body_text = ''
    smtp_host = ''
    smtp_port = ''
    user = ''
    password = ''

mail(fromaddr, toaddr, subject, body_text, smtp_host, smtp_port, user, password)
