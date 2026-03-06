
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
    sender_password = getpass.getpass("Enter the sender's password: ")

    # Get the recipient's email
    recipient_email = input("Enter the recipient's email: ")

    # Create a new EmailMessage object
    email_message = EmailMessage()

    # Set the sender and recipient
    email_message['From'] = sender_email
    email_message['To'] = recipient_email

    # Set the subject and body of the email
    email_message['Subject'] = "Test Email"
    email_message.set_content("This is a test email sent from a Python script.")

    # Connect to the SMTP server
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

    # Login to the SMTP server
    smtp_server.login(sender_email, sender_password)

    # Send the email
    smtp_server.send_message(email_message)

    # Close the SMTP server connection
    smtp_server.quit()

    # Print a success message
    print("Email sent successfully!")

# Call the task_func function with the client socket
task_func(client_socket)