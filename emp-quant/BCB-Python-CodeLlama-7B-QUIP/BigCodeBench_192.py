
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
    # Extract names from the text
    names = re.findall(r'[a-zA-Z]+\s[a-zA-Z]+', text)
    # Create a message
    message = "Subject: Extracted Names\n\n"
    for name in names:
        message += name + "\n"
    # Send the message
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, recepient_address, message)
    smtp.quit()
    return names