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
            if content_length > 1024:
                self.send_error(400, 'Bad Request')
                return
            try:
                data = json.loads(self.rfile.read(content_length))
            except json.JSONDecodeError:
                self.send_error(400, 'Bad Request')
                return
            if 'subject' not in data or 'message' not in data or 'to' not in data:
                self.send_error(400, 'Bad Request')
                return
            try:
                server = smtplib.SMTP(smtp_server, smtp_port)
                server.starttls()
                server.login(smtp_username, smtp_password)
                msg = MIMEText(data['message'])
                msg['Subject'] = data['subject']
                msg['To'] = data['to']
                server.sendmail(smtp_username, data['to'], msg.as_string())
                server.quit()
            except smtplib.SMTPAuthenticationError:
                self.send_error(535, 'Authentication Failed')
                return
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Email sent successfully')

    return EmailHandler