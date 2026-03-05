
from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = smtp_server
app.config['MAIL_PORT'] = smtp_port
app.config['MAIL_USERNAME'] = smtp_user
app.config['MAIL_PASSWORD'] = smtp_password
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/send-email')
def send_email():
    msg = Message('Test email', sender='test@example.com', recipients=['recipient@example.com'])
    msg.body = 'This is a test email sent using Flask-Mail.'
    mail.send(msg)
    return 'Email sent successfully!'