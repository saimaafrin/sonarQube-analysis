
import os
from flask_mail import Mail

def task_func(app):
    # Retrieve email server configuration from environment variables or use defaults
    mail_config = {
        'MAIL_SERVER': os.getenv('MAIL_SERVER', 'smtp.example.com'),
        'MAIL_PORT': int(os.getenv('MAIL_PORT', 587)),
        'MAIL_USE_TLS': os.getenv('MAIL_USE_TLS', 'true').lower() == 'true',
        'MAIL_USERNAME': os.getenv('MAIL_USERNAME', 'your-email@example.com'),
        'MAIL_PASSWORD': os.getenv('MAIL_PASSWORD', 'your-password')
    }
    
    # Configure the Flask app with the mail settings
    app.config.update(mail_config)
    
    # Initialize Flask-Mail with the configured app
    mail = Mail(app)
    
    return mail, mail_config