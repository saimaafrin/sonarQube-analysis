
from flask import Flask
from flask_mail import Mail, Message

def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    app = Flask(__name__)
    mail = Mail(app)

    # Set up SMTP configuration dynamically based on provided parameters
    mail.init_app(app)
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USE_LOCALTIME'] = True
    app.config['MAIL_TEMPLATE_FOLDER'] = template_folder

    # Define a route to send a test email
    @app.route('/')
    def test_email():
        msg = Message('Test Email', sender='test@example.com', recipients=['test@example.com'])
        mail.send(msg)
        return 'Test email sent'

    return app