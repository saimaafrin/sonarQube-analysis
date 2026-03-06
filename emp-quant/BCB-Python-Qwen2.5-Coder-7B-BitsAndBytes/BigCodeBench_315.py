
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    try:
        # Check if the directory exists
        if not os.path.exists(dir):
            return False
        
        # Get the list of files in the directory
        file_list = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        
        # Create the email message
        message = Mail(
            from_email='your-email@example.com',
            to_emails=recipient_email,
            subject='List of Files in Directory',
            plain_text_content='\n'.join(file_list)
        )
        
        # Initialize SendGrid client
        sg = SendGridAPIClient(api_key)
        
        # Send the email
        response = sg.send(message)
        
        # Check if the email was sent successfully
        if response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            return False
    
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Directory not found: {e}")
    
    except HTTPError as e:
        raise HTTPError(f"HTTP error occurred: {e}")
    
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")