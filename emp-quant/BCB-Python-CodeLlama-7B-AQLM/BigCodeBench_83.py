from flask import Flask
from flask_mail import Mail, Message
def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    """
    Creates a Flask application configured to send emails using Flask-Mail.
    It sets up the necessary SMTP configuration dynamically based on provided parameters
    and defines a route to send a test email.

    Parameters:
        smtp_server (str): The SMTP server address.
        smtp_port (int): The SMTP server port.
        smtp_user (str): The SMTP username.
        smtp_password (str): The SMTP password.
        template_folder (str): The folder path for email templates.

    Requirements:
    - flask.Flask
    - flask_mail.Mail
    - flask_mail.Message

    Returns:
        Flask: A Flask application instance configured for sending emails.

    Examples:
    >>> app = task_func('smtp.example.com', 587, 'user@example.com', 'password', 'templates')
    >>> type(app).__name__
    'Flask'
    >>> app.config['MAIL_USERNAME'] == 'user@example.com'
    True
    """
    app = Flask(__name__)
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = smtp_user
    app.config['MAIL_SUPPRESS_SEND'] = False
    app.config['MAIL_TEMPLATE_FOLDER'] = template_folder
    mail = Mail(app)

    @app.route('/send-test-email')
    def send_test_email():
        msg = Message('Test email', recipients=['user@example.com'])
        msg.body = 'This is a test email.'
        mail.send(msg)
        return 'Test email sent.'

    return app