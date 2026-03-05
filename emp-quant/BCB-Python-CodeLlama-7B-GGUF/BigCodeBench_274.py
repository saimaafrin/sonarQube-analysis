
import cgi
import http.server
import smtplib
from email.mime.text import MIMEText
import json

class EmailHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        try:
            # Get the email data from the request body
            email_data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))

            # Extract the subject, message, and recipient from the email data
            subject = email_data['subject']
            message = email_data['message']
            to = email_data['to']

            # Create a new MIMEText object with the email message
            msg = MIMEText(message)

            # Set the subject and recipient of the email
            msg['Subject'] = subject
            msg['To'] = to

            # Send the email using the provided SMTP server and credentials
            smtp = smtplib.SMTP(smtp_server, smtp_port)
            smtp.login(smtp_username, smtp_password)
            smtp.sendmail(smtp_username, to, msg.as_string())
            smtp.quit()

            # Return a 200 OK response
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Email sent successfully')
        except json.JSONDecodeError:
            # Return a 400 Bad Request response if the email data is not valid JSON
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON data')
        except ValueError:
            # Return a 400 Bad Request response if the 'subject', 'message', or 'to' keys are missing
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Missing required keys')
        except smtplib.SMTPAuthenticationError:
            # Return a 535 Authentication Failed response if there is an authentication issue with the SMTP server
            self.send_response(535)
            self.end_headers()
            self.wfile.write(b'Authentication failed')

    # Create a new EmailHandler instance
    handler = EmailHandler(('localhost', 8000), ('', 0), '', '')

    # Start the HTTP server
    httpd = http.server.HTTPServer(('localhost', 8000), handler)
    httpd.serve_forever()