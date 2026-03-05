import os
from flask_mail import Mail
def task_func(app):
    # Retrieve email server details from environment variables, use defaults if not available
    mail_server = os.getenv('MAIL_SERVER', 'smtp.example.com')
    mail_port = int(os.getenv('MAIL_PORT', 587))
    mail_use_tls = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    mail_use_ssl = os.getenv('MAIL_USE_SSL', 'false').lower() == 'true'
    mail_username = os.getenv('MAIL_USERNAME', 'your_username')
    mail_password = os.getenv('MAIL_PASSWORD', 'your_password')

    # Configure the Flask-Mail instance
    mail = Mail()
    mail.init_app(app)

    # Set the mail configurations
    app.config['MAIL_SERVER'] = mail_server
    app.config['MAIL_PORT'] = mail_port
    app.config['MAIL_USE_TLS'] = mail_use_tls
    app.config['MAIL_USE_SSL'] = mail_use_ssl
    app.config['MAIL_USERNAME'] = mail_username
    app.config['MAIL_PASSWORD'] = mail_password

    # Return the Flask-Mail instance and the app's mail configurations
    return mail, app.config['MAIL_SERVER'], app.config['MAIL_PORT'], app.config['MAIL_USE_TLS'], app.config['MAIL_USE_SSL'], app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']