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
                self.send_error(400, 'Invalid JSON')
                return

            required_keys = ['subject', 'message', 'to']
            if not all(key in email_data for key in required_keys):
                self.send_error(400, 'Missing required keys')
                return

            try:
                msg = MIMEText(email_data['message'])
                msg['Subject'] = email_data['subject']
                msg['From'] = smtp_username
                msg['To'] = email_data['to']

                with smtplib.SMTP(smtp_server, smtp_port) as server:
                    server.starttls()
                    server.login(smtp_username, smtp_password)
                    server.sendmail(smtp_username, email_data['to'], msg.as_string())
            except smtplib.SMTPAuthenticationError:
                self.send_error(535, 'Authentication Failed')
                return

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            response = {
                'content-type': 'application/json',
                'content-length': len(json.dumps({'status': 'Email sent successfully'}))
            }
            self.wfile.write(json.dumps(response).encode('utf-8'))

    return EmailHandler