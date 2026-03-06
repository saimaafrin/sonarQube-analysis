
import json
import smtplib
from email.mime.text import MIMEText

# Constants
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    # Parse the input data
    data = json.loads(input_data)
    
    # Extract recipient email addresses and names
    recipients = data.get('recipients', [])
    names = [recipient['name'] for recipient in recipients]
    
    # Create the email message
    subject = "Extracted Names"
    body = "\n".join(names)
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join([recipient['email'] for recipient in recipients])
    
    # Send the email
    if not smtp:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(email_address, email_password)
    
    smtp.sendmail(EMAIL_ADDRESS, [recipient['email'] for recipient in recipients], msg.as_string())
    smtp.quit()
    
    return names