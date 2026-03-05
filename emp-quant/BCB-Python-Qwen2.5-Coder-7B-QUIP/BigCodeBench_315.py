
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    try:
        # Check if the directory exists
        if not os.path.exists(dir):
            raise FileNotFoundError(f"Directory {dir} does not exist")
        
        # Get the list of files in the directory
        files = os.listdir(dir)
        
        # Create the email message
        message = Mail(
            from_email='your-email@example.com', to_emails=recipient_email,
            subject='List of Files', 
            plain_text_content=f"Files in {dir}: {files}"
        )
        
        # Send the email
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        
        # Check if the email was sent successfully
        if response.status_code == 200:
            return True
        else:
            return False
    except HTTPError as e:
        raise Exception(f"HTTP error occurred: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")