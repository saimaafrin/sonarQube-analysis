import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
def task_func(dir, api_key, recipient_email):
    try:
        # Check if the directory exists
        if not os.path.exists(dir):
            raise FileNotFoundError("The specified directory does not exist.")

        # Get the list of files in the directory
        files = os.listdir(dir)

        # Create the email message
        message = Mail(
            from_email='your_email@example.com',
            to_emails=recipient_email,
            subject='List of Files in Directory',
            plain_text_content='\n'.join(files)
        )

        # Send the email using SendGrid
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)

        # Check if the email was sent successfully
        if response.status_code >= 200 and response.status_code < 300:
            return True
        else:
            raise Exception("Failed to send email. HTTP status code: {}".format(response.status_code))

    except FileNotFoundError as e:
        print(e)
        return False
    except HTTPError as e:
        print(e)
        return False
    except Exception as e:
        print(e)
        return False