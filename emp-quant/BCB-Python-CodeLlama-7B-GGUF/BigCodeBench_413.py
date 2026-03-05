
import os
from flask_mail import Mail

def task_func(app):
    # Retrieve email server details from environment variables
    server = os.environ.get('MAIL_SERVER', 'localhost')
    port = int(os.environ.get('MAIL_PORT', 25))
    username = os.environ.get('MAIL_USERNAME')
    password = os.environ.get('MAIL_PASSWORD')
    use_tls = os.environ.get('MAIL_USE_TLS', 'true').lower() == 'true'
    use_ssl = os.environ.get('MAIL_USE_SSL', 'false').lower() == 'true'

    # Create Flask-Mail instance
    mail = Mail(app)

    # Configure Flask-Mail
    mail.init_app(app)
    mail.server = server
    mail.port = port
    mail.username = username
    mail.password = password
    mail.use_tls = use_tls
    mail.use_ssl = use_ssl

    # Return Flask-Mail instance and app's mail configurations
    return mail, app.config['MAIL']