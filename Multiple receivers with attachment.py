import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from emails import emails

Sender = input("Please enter Sender's Email : ")
Password = input("please enter your Password: ")
server = smtplib.SMTP_SSL('smtp.gmail.com')
server.ehlo()
server.login(Sender,Password)
msg = MIMEMultipart('alternative')
msg['Subject'] = 'Test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))
filename = 'ok.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)
#loop = 0
for i in emails:  
    text = msg.as_string()
    server.sendmail(Sender,i ,text)