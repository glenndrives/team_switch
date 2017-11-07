# Import smtplib for sending emails
import smtplib

# import the email module we need
from email.mime.text import MIMEText

def sendemail(msg_body, email_from, email_to):
    msg_body = MIMEText(msg_body)
    msg_body['Subject'] = 'Message from Team Switch'
    msg_body['From'] = email_from
    msg_body['To'] = email_to
    print(msg_body)
    server = smtplib.SMTP('webmail.whro.org', 25)
    server.send_message(msg_body)
    server.quit()

sendemail("Hello", "glennh@whro.org", "glennh@whro.org")
