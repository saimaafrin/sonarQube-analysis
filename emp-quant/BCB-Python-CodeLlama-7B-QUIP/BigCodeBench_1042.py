
import smtplib
from email.message import EmailMessage
import getpass

SERVER_ADDRESS = "localhost"
SERVER_PORT = 25
BUFFER_SIZE = 1024
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def task_func(client_socket):
    sender_email = getpass.getpass("Enter sender's email: ")
    recipient_email = getpass.getpass("Enter recipient's email: ")
    password = getpass.getpass("Enter sender's password: ")

    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()
    smtp_server.login(sender_email, password)

    message = EmailMessage()
    message.set_subject("Message from client")
    message.set_from(sender_email)
    message.set_to(recipient_email)
    message.set_body(client_socket.recv(BUFFER_SIZE))

    smtp_server.send_message(message)
    smtp_server.quit()

    client_socket.send(b"Message sent")