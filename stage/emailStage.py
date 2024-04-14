import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def read_emails(loc):
    with open(os.path.join(loc), 'r') as file:
        emails = [line.strip() for line in file]
    return emails

def read_login(loc):
    with open(os.path.join(loc), 'r') as file:
        line = file.readline().strip()
        sendermail, senderpass = line.split(';')
    return sendermail, senderpass

def readmsg(loc):
    with open(os.path.join(loc), 'r', encoding='utf-8') as file:
        first = file.readline().strip()
        rest = file.read()
    return first, rest

def attach_file(cvloc):
    with open(os.path.join(cvloc), 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {cvloc}")
    return part

def send_email(smtp_server, port, sendermail, senderpass, recievermail, subject, body, cvloc):
    try:
        msg = MIMEMultipart()
        msg['From'] = sendermail
        msg['To'] = recievermail
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))
        msg.attach(attach_file(cvloc))

        session = smtplib.SMTP(smtp_server, port) 
        session.starttls()
        session.login(sendermail, senderpass)
        text = msg.as_string()
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