import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json
def task_func(smtp_server, smtp_port, smtp_username, smtp_password):
    class EmailHandler(http.server.SimpleHTTPRequestHandler):
        def do_POST(self):
            content_type = self.headers.get('content-type')
            content_length = self.headers.get('content-length')
            if content_type != 'application/json':
                self.send_error(400, 'Bad Request')
                return
            if content_length > 1024 * 1024:
                self.send_error(400, 'Bad Request')
                return
            try:
                email_data = json.loads(self.rfile.read(content_length))
            except json.JSONDecodeError:
                self.send_error(400, 'Bad Request')
                return
            if 'subject' not in email_data or 'message' not in email_data or 'to' not in email_data:
                self.send_error(400, 'Bad Request')
                return
            try:
                smtp_server = smtplib.SMTP(smtp_server, smtp_port)
                smtp_server.login(smtp_username, smtp_password)
                smtp_server.sendmail(email_data['from'], email_data['to'], email_data['subject'], email_data['message'])
                smtp_server.quit()
            except smtplib.SMTPAuthenticationError:
                self.send_error(535, 'Authentication Failed')
                return
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Email sent successfully')

    return EmailHandler