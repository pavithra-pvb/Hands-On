import smtplib, ssl
import external_custom_script

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "mdnpavi@gmail.com"
receiver_email = "bhat.pavithra.azureproj@gmail.com"
password = input("Input password: ")
message = external_custom_script.transcribed_message()
context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as email_server:
    email_server.login(sender_email, password)
    email_server.sendmail(sender_email, receiver_email, message)