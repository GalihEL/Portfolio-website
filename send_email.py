import smtplib
import ssl
import os

# giving the function to be able to send email


def get_server(message):
    host = "smtp.gmail.com"
    port = 465
    email = "galihclassroom@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = email
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, password)
        server.sendmail(email, receiver, message)
