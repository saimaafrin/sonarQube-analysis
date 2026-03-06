
from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_email_password'

mail = Mail(app)

@app.route('/send_email')
def send_email():
    msg = Message('Test email', sender='your_email@gmail.com', recipients=['recipient@example.com'])
    msg.body = 'This is a test email sent using Flask-Mail.'
    mail.send(msg)
    return 'Email sent successfully!'