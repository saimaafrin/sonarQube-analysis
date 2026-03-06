
import os
from flask_mail import Mail

def task_func(app):
    # Retrieve email server details from environment variables
    host = os.environ.get('MAIL_SERVER', 'localhost')
    port = int(os.environ.get('MAIL_PORT', 25))
    username = os.environ.get('MAIL_USERNAME', None)
    password = os.environ.get('MAIL_PASSWORD', None)
    use_tls = os.environ.get('MAIL_USE_TLS', False)
    use_ssl = os.environ.get('MAIL_USE_SSL', False)

    # Initialize Flask-Mail with the retrieved details
    mail = Mail(app)
    mail.init_app(app)

    # Set the mail configurations
    mail.config['MAIL_SERVER'] = host
    mail.config['MAIL_PORT'] = port
    mail.config['MAIL_USERNAME'] = username
    mail.config['MAIL_PASSWORD'] = password
    mail.config['MAIL_USE_TLS'] = use_tls
    mail.config['MAIL_USE_SSL'] = use_ssl

    # Return the Flask-Mail instance and the app's mail configurations
    return mail, mail.config