import os
from flask import Flask
from flask_mail import Mail
def task_func(app):
    # Retrieve email server details from environment variables
    host = os.environ.get('MAIL_HOST', 'localhost')
    port = int(os.environ.get('MAIL_PORT', 25))
    username = os.environ.get('MAIL_USERNAME', None)
    password = os.environ.get('MAIL_PASSWORD', None)

    # Create Flask-Mail instance
    mail = Mail(app)

    # Set mail configurations
    mail.init_app(app)
    mail.host = host
    mail.port = port
    mail.username = username
    mail.password = password

    # Return Flask-Mail instance and mail configurations
    return mail, mail.config
app = Flask(__name__)