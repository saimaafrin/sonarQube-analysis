from flask import Flask
from flask_mail import Mail, Message
def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    app = Flask(__name__)
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_DEFAULT_SENDER'] = 'test@example.com'
    app.config['MAIL_TEMPLATE_FOLDER'] = template_folder
    mail = Mail(app)

    @app.route('/send-email')
    def send_email():
        msg = Message('Test email', sender='test@example.com', recipients=['test@example.com'])
        msg.body = 'This is a test email sent using Flask-Mail.'
        mail.send(msg)
        return 'Email sent successfully.'

    return app