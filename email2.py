import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = "stunna"
email['to'] = "example@gmail.com"
email['subject'] = "python master"
email.set_content(html.substitute({'name': 'ahmed'}), 'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    #the email that is going to be logged in
    smtp.login('example2@gmail.com', 'password')
    smtp.send_message(email)
    print("all goooooooood!!!!!!!!!!!!!")
    