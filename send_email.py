import smtplib
from email.mime.text import MIMEText
import os

def send_email(subject, body):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = os.environ['SMTP_USER']
    smtp_pass = os.environ['SMTP_PASS']

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = smtp_user
    msg['To'] = 'recipient-email@example.com'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.send_message(msg)

if __name__ == '__main__':
    import sys
    subject = sys.argv[1]
    body = sys.argv[2]
    send_email(subject, body)
