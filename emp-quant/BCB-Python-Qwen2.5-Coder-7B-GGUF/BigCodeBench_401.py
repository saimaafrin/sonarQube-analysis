
from flask import Flask
import os
from flask_mail import Mail

def task_func(app_name):
    app = Flask(app_name)
    
    # Retrieve email server details from environment variables or use defaults
    mail_server = os.getenv('MAIL_SERVER', 'localhost')
    mail_port = int(os.getenv('MAIL_PORT', 25))
    mail_use_tls = os.getenv('MAIL_USE_TLS', 'False').lower() in ['true', '1', 't', 'y', 'yes']
    mail_username = os.getenv('MAIL_USERNAME', None)
    mail_password = os.getenv('MAIL_PASSWORD', None)
    
    # Configure the mail settings
    app.config['MAIL_SERVER'] = mail_server
    app.config['MAIL_PORT'] = mail_port
    app.config['MAIL_USE_TLS'] = mail_use_tls
    app.config['MAIL_USERNAME'] = mail_username
    app.config['MAIL_PASSWORD'] = mail_password
    
    # Initialize Flask-Mail with the app's mail configurations
    mail = Mail(app)
    
    return mail, app.config['MAIL_SERVER'], app.config['MAIL_PORT'], app.config['MAIL_USE_TLS'], app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']