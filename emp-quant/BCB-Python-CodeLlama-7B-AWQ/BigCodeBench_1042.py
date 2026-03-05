import smtplib
from email.message import EmailMessage
import getpass
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
def task_func(client_socket):
    sender_email = input("Enter sender's email: ")
    recipient_email = input("Enter recipient's email: ")
    sender_password = getpass.getpass("Enter sender's password: ")

    # Create a new email message
    msg = EmailMessage()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Test email from Python"
    msg.set_content("This is a test email sent from Python.")

    # Log in to the SMTP server
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.send_message(msg)

    # Close the SMTP connection
    server.quit()

    print("Email sent successfully!")
client_socket = "dummy_socket"