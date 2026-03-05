import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"
def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    # Parse the input JSON data
    data = json.loads(input_data)
    
    # Extract recipient email and names
    recipient_email = data['recipient']['email']
    names = [person['name'] for person in data['recipients']]
    
    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = recipient_email
    msg['Subject'] = 'Extracted Names'
    body = '\n'.join(names)
    msg.attach(MIMEText(body, 'plain'))
    
    # Send the email
    if smtp is None:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_address, email_password)
        text = msg.as_string()
        server.sendmail(email_address, recipient_email, text)
        server.quit()
    else:
        smtp.sendmail(email_address, recipient_email, msg.as_string())
    
    return names