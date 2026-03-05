
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError

def task_func(dir, api_key, recipient_email):
    """
    Send a list of files in a directory to a recipient using SendGrid API.

    Args:
        dir (str): Path to the directory containing the files.
        api_key (str): SendGrid API key.
        recipient_email (str): Email address of the recipient.

    Returns:
        bool: True if the email was sent successfully, False otherwise.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        HTTPError: If an HTTP error occurs during the sending process.
        Exception: For any other exceptions that may occur during the execution.
    """
    if not os.path.exists(dir):
        raise FileNotFoundError(f"Directory {dir} does not exist.")

    # Create a SendGrid client
    sg = SendGridAPIClient(api_key)

    # Create a message
    message = Mail(
        from_email="your_email@example.com",
        to_emails=recipient_email,
        subject="List of files in directory",
        html_content="<p>List of files in directory:</p><ul>"
    )

    # Add files to the message
    for file in os.listdir(dir):
        message.add_content(
            Content("text/plain", f"<li>{file}</li>")
        )

    # Send the message
    try:
        response = sg.send(message)
        if response.status_code // 100 == 2:
            return True
        else:
            raise HTTPError(f"Failed to send email: {response.status_code}")
    except Exception as e:
        raise e