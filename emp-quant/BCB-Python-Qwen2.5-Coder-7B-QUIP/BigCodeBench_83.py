
from flask import Flask
from flask_mail import Mail, Message

def task_func(smtp_server, smtp_port, smtp_user, smtp_password, template_folder):
    # Create a Flask application instance
    app = Flask(__name__)
    
    # Configure the mail settings
    app.config['MAIL_SERVER'] = smtp_server
    app.config['MAIL_PORT'] = smtp_port
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = smtp_user
    app.config['MAIL_PASSWORD'] = smtp_password
    
    # Initialize Flask-Mail
    mail = Mail(app)
    
    # Define a route to send a test email
    @app.route('/send-test-email')
    def send_test_email():
        msg = Message('Test Email', sender='your-email@example.com', recipients=['recipient-email@example.com'])
        msg.body = 'This is a test email sent from a Flask application.'
        mail.send(msg)
        return 'Test email sent successfully!'
    
    return app