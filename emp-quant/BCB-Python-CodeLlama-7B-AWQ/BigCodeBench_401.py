from flask import Flask
import os
from flask_mail import Mail
def task_func(app_name):
    app = Flask(app_name)
    mail_server = os.environ.get('MAIL_SERVER', 'localhost')
    mail_port = int(os.environ.get('MAIL_PORT', 25))
    mail_use_tls = bool(os.environ.get('MAIL_USE_TLS', False))
    mail_username = os.environ.get('MAIL_USERNAME', None)
    mail_password = os.environ.get('MAIL_PASSWORD', None)
    mail = Mail(app)
    mail.init_app(app, mail_server, mail_port, mail_use_tls, mail_username, mail_password)
    return mail, app.config