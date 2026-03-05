
import json
import smtplib

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    # Extract the email address and names from the JSON-formatted string
    json_data = json.loads(input_data)
    email_address = json_data["email_address"]
    names = json_data["names"]

    # Create a message
    message = "Subject: Extracted Names\n\n"
    for name in names:
        message += name + "\n"

    # Send the message
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, email_address, message)
    smtp.quit()

    # Return the list of extracted names
    return names