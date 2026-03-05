
import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json

def task_func(smtp_server, smtp_port, smtp_username, smtp_password):
    class EmailHandler:
        def __init__(self, smtp_server, smtp_port, smtp_username, smtp_password):
            self.smtp_server = smtp_server
            self.smtp_port = smtp_port
            self.smtp_username = smtp_username
            self.smtp_password = smtp_password

        def send_email(self, email_data):
            try:
                email_data = json.loads(email_data)
                subject = email_data["subject"]
                message = email_data["message"]
                to = email_data["to"]

                message = MIMEText(message)
                message["Subject"] = subject
                message["To"] = to

                smtp_server = smtplib.SMTP(self.smtp_server, self.smtp_port)
                smtp_server.starttls()
                smtp_server.login(self.smtp_username, self.smtp_password)
                smtp_server.send_message(message)
                smtp_server.quit()

                return {"content-type": "application/json", "content-length": len(message)}
            except json.JSONDecodeError:
                raise http.server.HTTPError(400, "Bad Request")
            except ValueError:
                raise http.server.HTTPError(400, "Bad Request")
            except smtplib.SMTPAuthenticationError:
                raise http.server.HTTPError(535, "Authentication Failed")

    return EmailHandler(smtp_server, smtp_port, smtp_username, smtp_password)