import json
import smtplib
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"
def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    """
    Extracts recipient email addresses and names from a JSON-formatted string and sends the names in an email.
    The sent message should be in the format 'Subject: Extracted Names\n\nName1\nName2\n...'.
    """
    # Extract recipient email addresses and names from the input data
    recipient_emails = []
    recipient_names = []
    for recipient in json.loads(input_data):
        recipient_emails.append(recipient["email"])
        recipient_names.append(recipient["name"])

    # Create an email message
    message = f"Subject: Extracted Names\n\n"
    for name in recipient_names:
        message += f"{name}\n"

    # Send the email
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, recipient_emails, message)
    smtp.quit()

    # Return the list of extracted names
    return recipient_names
input_data = '[{"email": "john.doe@example.com", "name": "John Doe"}, {"email": "jane.doe@example.com", "name": "Jane Doe"}]'