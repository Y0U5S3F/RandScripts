import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def read_emails(location):
    with open(os.path.join(location), 'r') as file:
        emails = [line.strip() for line in file]
    return emails

def read_login(location):
    with open(os.path.join(location), 'r') as file:
        line = file.readline().strip()
        sendermail, senderpass = line.split(';')
    return sendermail, senderpass

def readmsg(location):
    with open(os.path.join(location), 'r', encoding='utf-8') as file:
        first = file.readline().strip()
        rest = file.read()
    return first, rest

def attach_file(file_location):
    with open(os.path.join(file_location), 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {file_location}")
    return part

def send_email(smtp_server, port, sendermail, senderpass, recievermail, subject, body, file_location):
    try:
        message = MIMEMultipart()
        message['From'] = sendermail
        message['To'] = recievermail
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain', 'utf-8'))  # Specify UTF-8 charset here
        message.attach(attach_file(file_location))

        session = smtplib.SMTP(smtp_server, port) 
        session.starttls()
        session.login(sendermail, senderpass)
        text = message.as_string()
        session.sendmail(sendermail, recievermail, text)
        session.quit()
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

sendermail, senderpass = read_login('login.txt')
emails = read_emails('emails.txt')
for email in emails:
    subject, body = readmsg('stage.txt')
    send_email('smtp-mail.outlook.com', 587, sendermail, senderpass, email, subject, body, 'cv.pdf')
    print(f"Done sending to {email}")