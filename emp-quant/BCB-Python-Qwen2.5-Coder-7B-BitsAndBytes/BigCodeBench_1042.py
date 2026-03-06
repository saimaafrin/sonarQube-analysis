
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
    message = client_socket.recv(BUFFER_SIZE).decode()
    
    # Get user input for email details
    sender_email = input("Enter your email address: ")
    receiver_email = input("Enter the recipient's email address: ")
    sender_password = getpass.getpass("Enter your email password: ")
    
    # Create the email message
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Client Message'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()