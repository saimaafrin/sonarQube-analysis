
from flask import Flask
import os
from flask_mail import Mail

def task_func(app_name):
    # Create a Flask application instance
    app = Flask(app_name)

    # Retrieve email server details from environment variables with defaults
    mail_server = os.getenv('MAIL_SERVER', 'localhost')
    mail_port = int(os.getenv('MAIL_PORT', 25))
    mail_use_tls = os.getenv('MAIL_USE_TLS', 'False').lower() in ['true', '1', 't', 'y', 'yes']
    mail_username = os.getenv('MAIL_USERNAME', None)
    mail_password = os.getenv('MAIL_PASSWORD', None)

    # Configure the Flask-Mail instance
    mail = Mail(app)
    app.config['MAIL_SERVER'] = mail_server
    app.config['MAIL_PORT'] = mail_port
    app.config['MAIL_USE_TLS'] = mail_use_tls
    app.config['MAIL_USERNAME'] = mail_username
    app.config['MAIL_PASSWORD'] = mail_password

    # Return the Flask-Mail instance and the app's mail configurations
    return mail, app.config['MAIL_SERVER'], app.config['MAIL_PORT'], app.config['MAIL_USE_TLS'], app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']