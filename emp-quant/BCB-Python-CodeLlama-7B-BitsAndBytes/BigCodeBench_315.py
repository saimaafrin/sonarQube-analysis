
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    # Check if the directory exists
    if not os.path.exists(dir):
        raise FileNotFoundError(f"Directory {dir} does not exist")

    # Create a SendGrid client
    sg = SendGridAPIClient(api_key)

    # Create a new mail object
    mail = Mail()

    # Set the sender and recipient
    mail.set_from("sender@example.com")
    mail.add_to(recipient_email)

    # Set the subject and body of the email
    mail.set_subject("List of files in directory")
    mail.set_html("Here is the list of files in the directory:")

    # Get the list of files in the directory
    files = os.listdir(dir)

    # Add the files to the email body
    for file in files:
        mail.add_content(f"<p>{file}</p>")

    # Send the email
    try:
        response = sg.send(mail.get())
        print(f"Email sent successfully with status code {response.status_code}")
        return True
    except HTTPError as e:
        print(f"Error sending email: {e}")
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False