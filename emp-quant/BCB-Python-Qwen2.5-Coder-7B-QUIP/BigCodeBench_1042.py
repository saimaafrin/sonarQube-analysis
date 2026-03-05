
import smtplib
from email.message import EmailMessage
import getpass
SERVER_ADDRESS = "localhost"
SERVER_PORT = 25
BUFFER_SIZE = 1024
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def task_func(client_socket):
    # Receive the message from the client
    message = client_socket.recv(BUFFER_SIZE).decode('utf-8')
    
    # Split the message into sender, recipient, and body
    sender, recipient, body = message.split('\n')
    
    # Create the email message
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = sender
    msg['To'] = recipient
    
    # Connect to the SMTP server
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.starttls()
        smtp.login(sender, getpass.getpass(f"Enter password for {sender}: "))
        smtp.send_message(msg)
    
    # Close the client socket
    client_socket.close()
    
    # Output None
    print(None)