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
    # Load the JSON data
    data = json.loads(input_data)

    # Extract the recipient email addresses and names
    recipients = []
    for recipient in data["recipients"]:
        recipients.append(recipient["email"])

    # Create the email message
    message = "Subject: Extracted Names\n\n"
    for recipient in recipients:
        message += recipient + "\n"

    # Send the email
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, recipients, message)
    smtp.quit()

    # Return the list of extracted names
    return recipients
input_data = '{"recipients": [{"email": "john.doe@example.com", "name": "John Doe"}, {"email": "jane.doe@example.com", "name": "Jane Doe"}]}'