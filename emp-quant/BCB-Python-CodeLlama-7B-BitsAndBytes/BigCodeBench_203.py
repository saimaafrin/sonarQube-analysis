
import json
import smtplib

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    # Extract the recipient email address and names from the JSON-formatted string
    data = json.loads(input_data)
    recipient_email = data["recipient_email"]
    names = data["names"]

    # Create a new SMTP session
    smtp = smtplib.SMTP(smtp_server, smtp_port)

    # Log in to the SMTP server
    smtp.login(email_address, email_password)

    # Send the email
    subject = "Extracted Names"
    message = "\n".join(names)
    smtp.sendmail(email_address, recipient_email, f"Subject: {subject}\n\n{message}")

    # Close the SMTP session
    smtp.quit()

    # Return the list of extracted names
    return names