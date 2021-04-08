import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = "stunna"
email['to'] = "example@gmail.com"
email['subject'] = "python master"

email.set_content("I am python master............")
with smtplib.SMTP(host='smpt.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example2@gmail.com', 'password')
    smtp.send_message(email)
    print("all gooood bossss")