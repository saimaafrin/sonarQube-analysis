
from flask import Flask
import os
from flask_mail import Mail

def task_func(app_name):
    # Initialize Flask application
    app = Flask(app_name)

    # Set mail configurations
    mail_server = os.environ.get('MAIL_SERVER', 'localhost')
    mail_port = int(os.environ.get('MAIL_PORT', 25))
    mail_use_tls = os.environ.get('MAIL_USE_TLS', False)
    mail_username = os.environ.get('MAIL_USERNAME', None)
    mail_password = os.environ.get('MAIL_PASSWORD', None)

    # Initialize Flask-Mail instance
    mail = Mail(app)

    # Set mail configurations
    mail.init_app(app)
    mail.config['MAIL_SERVER'] = mail_server
    mail.config['MAIL_PORT'] = mail_port
    mail.config['MAIL_USE_TLS'] = mail_use_tls
    mail.config['MAIL_USERNAME'] = mail_username
    mail.config['MAIL_PASSWORD'] = mail_password

    # Return tuple containing Flask-Mail instance and app's mail configurations
    return (mail, mail.config)