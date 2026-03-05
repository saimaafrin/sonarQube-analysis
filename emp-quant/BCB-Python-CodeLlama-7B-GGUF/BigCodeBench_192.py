
import re
import smtplib

# Constants
TEXT = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
RECEPIENT_ADDRESS = "names@gmail.com"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"

def task_func(text=TEXT, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, recepient_address=RECEPIENT_ADDRESS, smtp=None):
    # Extract names from text
    names = re.findall(r'\[?([A-Z][a-z]* [A-Z][a-z]*)\]?', text)

    # Create email message
    message = f"Subject: Extracted Names\n\n"
    for name in names:
        message += f"{name}\n"

    # Send email
    if smtp is None:
        smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, recepient_address, message)
    smtp.quit()

task_func()