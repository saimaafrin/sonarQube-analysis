import json
import smtplib
from email.mime.text import MIMEText
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"
def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    # Parse the input JSON data
    data = json.loads(input_data)
    
    # Extract recipient email addresses and names
    recipients = data.get('recipients', [])
    names = [recipient.get('name') for recipient in recipients]
    
    # Create the email message
    message = MIMEText('\n'.join(names))
    message['Subject'] = 'Extracted Names'
    message['From'] = email_address
    message['To'] = ', '.join([recipient['email'] for recipient in recipients])
    
    # Send the email
    if smtp is None:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
        smtp.starttls()
        smtp.login(email_address, email_password)
    
    smtp.sendmail(email_address, [recipient['email'] for recipient in recipients], message.as_string())
    smtp.quit()
    
    return names