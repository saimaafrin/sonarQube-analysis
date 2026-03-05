import re
import smtplib
from email.mime.text import MIMEText
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"
def task_func(text=TEXT, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, recepient_address=RECEPIENT_ADDRESS):
    # Extract names using regular expression
    names = re.findall(r'\b[A-Za-z]+\s[A-Za-z]+\b', text)
    
    # Create email message
    subject = "Extracted Names"
    body = "\n".join(names)
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = email_address
    message['To'] = recepient_address
    
    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, recepient_address, message.as_string())
    
    return names