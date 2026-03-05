import smtplib
from email.message import EmailMessage
import getpass
BUFFER_SIZE = 1024
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
def task_func(client_socket):
    # Receive message from client socket
    message = client_socket.recv(BUFFER_SIZE).decode()

    # Get sender's email, recipient's email, and sender's email password
    sender_email = input("Enter sender's email: ")
    recipient_email = input("Enter recipient's email: ")
    sender_password = getpass.getpass("Enter sender's email password: ")

    # Create email message
    email_message = EmailMessage()
    email_message["From"] = sender_email
    email_message["To"] = recipient_email
    email_message["Subject"] = "Email from client socket"
    email_message.set_content(message)

    # Send email via SMTP server
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()
    smtp_server.login(sender_email, sender_password)
    smtp_server.send_message(email_message)
    smtp_server.quit()

    # Output
    print("Email sent successfully!")