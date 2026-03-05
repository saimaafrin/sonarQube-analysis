
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
    # Extract names using regular expression
    names = re.findall(r'\b[A-Za-z]+\b', text)
    
    # Filter out names enclosed in square brackets
    names = [name for name in names if not re.match(r'.*\[.*\].*', name)]
    
    # Send the names in an email
    message = f"Subject: Extracted Names\n\n{'\n'.join(names)}"
    
    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, recepient_address, message)
    
    # Return the list of names
    return names