from flask import Flask
from flask_mail import Mail, Message
def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    app = Flask(__name__, template_folder=template_folder)
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password

    mail = Mail(app)

    @app.route('/send-test-email')
    def send_test_email():
        msg = Message("Test Email", sender=smtp_user, recipients=[smtp_user])
        msg.body = "This is a test email sent from a Flask application."
        mail.send(msg)
        return "Test email sent!"

    return app