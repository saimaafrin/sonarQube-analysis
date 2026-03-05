import os
from flask_mail import Mail
def task_func(app):
    # Retrieve email server details from environment variables, use defaults if not available
    mail_server = os.getenv('MAIL_SERVER', 'smtp.example.com')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_use_tls = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    mail_use_ssl = os.getenv('MAIL_USE_SSL', 'false').lower() == 'true'
    mail_username = os.getenv('MAIL_USERNAME', 'user@example.com')
    mail_password = os.getenv('MAIL_PASSWORD', 'password')

    # Configure the Flask-Mail instance
    mail = Mail(app)
    mail.init_app(app, {
        'MAIL_SERVER': mail_server,
        'MAIL_PORT': mail_port,
        'MAIL_USE_TLS': mail_use_tls,
        'MAIL_USE_SSL': mail_use_ssl,
        'MAIL_USERNAME': mail_username,
        'MAIL_PASSWORD': mail_password
    })

    # Return the Flask-Mail instance and the app's mail configurations
    return mail, app.config['MAIL']