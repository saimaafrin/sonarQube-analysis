from flask import Flask
import os
from flask_mail import Mail
def task_func(app_name):
    # Create a Flask application instance
    app = Flask(app_name)
    
    # Retrieve email server details from environment variables or use defaults
    mail_server = os.getenv('MAIL_SERVER', 'localhost')
    mail_port = int(os.getenv('MAIL_PORT', 25))
    mail_use_tls = os.getenv('MAIL_USE_TLS', 'False').lower() == 'true'
    mail_username = os.getenv('MAIL_USERNAME', None)
    mail_password = os.getenv('MAIL_PASSWORD', None)
    
    # Configure the Flask-Mail instance
    mail = Mail(app)
    mail.init_app(app)
    mail.config.update(
        MAIL_SERVER=mail_server,
        MAIL_PORT=mail_port,
        MAIL_USE_TLS=mail_use_tls,
        MAIL_USERNAME=mail_username,
        MAIL_PASSWORD=mail_password
    )
    
    # Return the Flask-Mail instance and the app's mail configurations
    return mail, mail.config