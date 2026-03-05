
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    try:
        # Get the list of files in the directory
        file_list = os.listdir(dir)
        # Create a SendGrid API client
        client = SendGridAPIClient(api_key)
        # Create a mail object
        mail = Mail(
            from_email="your_email_address",
            to_email=recipient_email,
            subject="Attachment",
            html_body="<h1>Attachment</h1><p>Please find the attachment</p>"
        )
        # Add the files to the mail object
        for file in file_list:
            mail.attachment(file)
        # Send the mail
        response = client.send_mail(mail)
        # Check the status code of the response
        if response.status_code in range(200, 299):
            return True
        else:
            return False
    except FileNotFoundError:
        raise
    except HTTPError:
        raise
    except Exception:
        raise