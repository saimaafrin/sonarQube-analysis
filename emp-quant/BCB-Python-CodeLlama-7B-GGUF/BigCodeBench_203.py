
import json
import smtplib

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    # Extract recipient email address and names from JSON-formatted string
    data = json.loads(input_data)
    recipient_email = data["recipient_email"]
    names = data["names"]

    # Create email message
    message = f"Subject: Extracted Names\n\n{names}"

    # Send email
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, recipient_email, message)
    smtp.quit()

    # Return list of extracted names
    return names