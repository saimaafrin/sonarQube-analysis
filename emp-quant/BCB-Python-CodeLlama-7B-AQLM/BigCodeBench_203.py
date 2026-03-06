import json
import smtplib
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "your.email@gmail.com"
EMAIL_PASSWORD = "your.password"
def task_func(input_data=None, smtp_server=SMTP_SERVER, smtp_port=SMTP_PORT, email_address=EMAIL_ADDRESS, email_password=EMAIL_PASSWORD, smtp=None):
    """
    Extract recepient email address and names from JSON-formatted string and send the names in an email. The sent message should be in the format 'Subject: Extracted Names\n\nName1\nName2\n...'.

    Parameters:
    input_data (str): JSON-formatted string containing the recipient email address and the list of names.
    smtp_server (str): The SMTP server to use for sending the email.
    smtp_port (int): The port to use for the SMTP server.
    email_address (str): The email address from which to send the email.
    email_password (str): The password for the email address.
    
    Returns:
    list: A list of extracted names.
    
    Requirements:
    - re
    - smtplib

    Example:
    >>> from unittest.mock import MagicMock
    >>> mock_smtp_instance = MagicMock()
    >>> mock_smtp = MagicMock(return_value=mock_smtp_instance)
    >>> task_func('{"recipient": "recipient@example.com", "names": ["Josie Smith", "Mugsy Dog Smith"]}', smtp=mock_smtp)
    ['Josie Smith', 'Mugsy Dog Smith']
    """
    # Extract recipient email address and names from JSON-formatted string
    input_data = json.loads(input_data)
    recipient = input_data["recipient"]
    names = input_data["names"]

    # Create message
    message = "Subject: Extracted Names\n\n"
    for name in names:
        message += name + "\n"

    # Send message
    smtp = smtplib.SMTP(smtp_server, smtp_port)
    smtp.starttls()
    smtp.login(email_address, email_password)
    smtp.sendmail(email_address, recipient, message)
    smtp.quit()

    # Return extracted names
    return names