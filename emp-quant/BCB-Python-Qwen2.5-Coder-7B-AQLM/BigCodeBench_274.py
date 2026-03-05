
import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json

def task_func(smtp_server, smtp_port, smtp_username, smtp_password):
    class EmailHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                email_data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Invalid JSON')
                return

            if 'subject' not in email_data or 'message' not in email_data or 'to' not in email_data:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Missing required fields')
                return

            subject = email_data['subject']
            message = email_data['message']
            to = email_data['to']

            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = smtp_username
            msg['To'] = to

            try:
                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(smtp_username, to, msg.as_string())
            except smtplib.SMTPAuthenticationError:
                self.send_response(535)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'Authentication Failed')
                return

            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Email sent successfully')

    return EmailHandler