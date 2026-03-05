
import smtplib
from email.message import EmailMessage
import getpass

SERVER_ADDRESS = "localhost"
SERVER_PORT = 25
BUFFER_SIZE = 1024
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

def task_func(client_socket):
    # Get the sender's email and password
    sender_email = input("Enter the sender's email: ")
    sender_password = getpass.getpass(prompt="Enter the sender's password: ")

    # Get the recipient's email
    recipient_email = input("Enter the recipient's email: ")

    # Create a new email message
    msg = EmailMessage()
    msg["Subject"] = "Test Email"
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg.set_content("This is a test email sent using Python's smtplib module.")

    # Connect to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    # Authenticate with the SMTP server
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)

    # Close the SMTP connection
    server.quit()

    # Print a success message
    print("Email sent successfully!")

# Run the task function
task_func(None)