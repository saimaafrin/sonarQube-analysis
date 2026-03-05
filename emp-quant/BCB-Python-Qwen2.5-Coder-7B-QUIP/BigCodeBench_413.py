
import os
from flask_mail import Mail

def task_func(app):
    # Retrieve email server details from environment variables, or use defaults
    mail_server = os.getenv('MAIL_SERVER', 'smtp.example.com')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_username = os.getenv('MAIL_USERNAME', 'user@example.com')
    mail_password = os.getenv('MAIL_PASSWORD', 'password')
    
    # Initialize Flask-Mail with the retrieved or default values
    mail = Mail(app)
    app.config['MAIL_SERVER'] = mail_server
    app.config['MAIL_PORT'] = mail_port
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = mail_username
    app.config['MAIL_PASSWORD'] = mail_password
    
    # Return the Flask-Mail instance and the app's mail configurations
    return mail, app.config