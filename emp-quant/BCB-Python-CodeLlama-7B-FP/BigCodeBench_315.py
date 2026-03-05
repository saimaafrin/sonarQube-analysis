import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
def task_func(dir, api_key, recipient_email):
    """
    Get a list of files in a directory and send that list by e-mail to a specific recipient using a provided SendGrid API key.
    The function should raise the exception for:
        FileNotFoundError: If the specified directory does not exist.
        HTTPError: If an HTTP error occurs during the sending process.
        Exception: For any other exceptions that may occur during the execution.
    The function should output with:
        bool: True if the email was sent successfully. Specifically, a successful send is indicated by an HTTP status code in the 2xx range, which denotes success. False is returned if the directory does not exist.
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
        html_content=f"<p>Here is the list of files in the directory {dir}:</p><ul>"
    )

    # Add the files to the message
    for file in os.listdir(dir):
        message.add_attachment(file)

    # Send the message
    try:
        response = sg.send(message)
        if response.status_code // 100 == 2:
            return True
        else:
            raise HTTPError(f"Failed to send email: {response.status_code}")
    except Exception as e:
        raise e