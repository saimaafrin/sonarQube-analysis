
import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json

class EmailHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            email_data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return
        
        if 'subject' not in email_data or 'message' not in email_data or 'to' not in email_data:
            self.send_error(400, "Missing required fields")
            return
        
        subject = email_data['subject']
        message = email_data['message']
        to_email = email_data['to']
        
        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = smtp_username
            msg['To'] = to_email
            
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, to_email, msg.as_string())
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Email sent successfully")
        except smtplib.SMTPAuthenticationError:
            self.send_error(535, "Authentication failed")

def task_func(smtp_server, smtp_port, smtp_username, smtp_password):
    httpd = http.server.HTTPServer(('localhost', 8000), EmailHandler)
    print("Serving at port 8000")
    httpd.serve_forever()