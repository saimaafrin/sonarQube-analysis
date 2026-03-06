
import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json

class EmailHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Get the email data from the request body
        email_data = self.rfile.read(int(self.headers['Content-Length']))
        try:
            email_data = json.loads(email_data)
        except json.JSONDecodeError:
            self.send_error(400, 'Bad Request')
            return

        # Check if the email data is valid
        if 'subject' not in email_data or 'message' not in email_data or 'to' not in email_data:
            self.send_error(400, 'Bad Request')
            return

        # Create the email message
        message = MIMEText(email_data['message'])
        message['Subject'] = email_data['subject']
        message['To'] = email_data['to']

        # Send the email
        try:
            smtp_server = smtplib.SMTP(smtp_server, smtp_port)
            smtp_server.login(smtp_username, smtp_password)
            smtp_server.sendmail(email_data['from'], email_data['to'], message.as_string())
            smtp_server.quit()
        except smtplib.SMTPAuthenticationError:
            self.send_error(535, 'Authentication Failed')
            return

        # Return a 200 OK response
        self.send_response(200)
        self.end_headers()