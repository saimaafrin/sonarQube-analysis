from flask import Flask
import os
from flask_mail import Mail
def task_func(app_name):
    app = Flask(app_name)
    app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', 'localhost')
    app.config['MAIL_PORT'] = int(os.environ.get('MAIL_PORT', 25))
    app.config['MAIL_USE_TLS'] = bool(os.environ.get('MAIL_USE_TLS', False))
    app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME', None)
    app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD', None)
    mail = Mail(app)
    return (mail, app.config)
app_name = 'my_app'