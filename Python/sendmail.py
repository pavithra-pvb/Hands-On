import smtplib
from email.mime.text import MIMEText

subject = "Test Email from Python"
body = "Test mail sent from a Python program"
sender = "mdnpavi@gmail.com"
recipients = ["mdnpavi@gmail.com", "pavipvbhat.23704@gmail.com"]
password = "eagf plkk eusk qhzg"


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)