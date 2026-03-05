import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json
def task_func(smtp_server, smtp_port, smtp_username, smtp_password):
    class EmailHandler(http.server.SimpleHTTPRequestHandler):
        def do_POST(self):
            try:
                # Get the email data from the request body
                email_data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))

                # Check if the email data is valid JSON
                if not isinstance(email_data, dict):
                    raise JSONDecodeError

                # Check if the email data contains the required keys
                if 'subject' not in email_data or 'message' not in email_data or 'to' not in email_data:
                    raise ValueError

                # Set up the email message
                msg = MIMEText(email_data['message'])
                msg['Subject'] = email_data['subject']
                msg['To'] = email_data['to']

                # Send the email using the provided SMTP server and credentials
                smtp = smtplib.SMTP(smtp_server, smtp_port)
                smtp.login(smtp_username, smtp_password)
                smtp.sendmail(smtp_username, email_data['to'], msg.as_string())
                smtp.quit()

                # Return a 200 OK response
                self.send_response(200)
                self.end_headers()
                return

            except JSONDecodeError:
                # Return a 400 Bad Request response if the email data is not valid JSON
                self.send_response(400)
                self.end_headers()
                return

            except ValueError:
                # Return a 400 Bad Request response if the email data is missing required keys
                self.send_response(400)
                self.end_headers()
                return

            except smtplib.SMTPAuthenticationError:
                # Return a 535 Authentication Failed response if there is an authentication issue with the SMTP server
                self.send_response(535)
                self.end_headers()
                return

    return EmailHandler