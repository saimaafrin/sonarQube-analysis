import os
from flask_mail import Mail
def task_func(app):
    """
    Initialize a Flask application with Flask-Mail. 

    Parameters:
    app (Flask): The Flask application to configure.

    Returns:
    tuple: A tuple containing the Flask-Mail instance and the app's mail configurations.

    Note:
    - The details of the email server are retrieved from environment variables. 
    - If the variables do not exist, use defaults.
    
    Requirements:
    - os
    - flask_mail

    Example:
    >>> from flask import Flask
    >>> app = Flask("test")
    >>> mail, configs = task_func(app)
    >>> 'MAIL_SERVER' in configs
    True
    """
    # Retrieve the mail server configuration from environment variables.
    mail_server = os.environ.get('MAIL_SERVER', 'localhost')
    mail_port = os.environ.get('MAIL_PORT', 25)
    mail_username = os.environ.get('MAIL_USERNAME', None)
    mail_password = os.environ.get('MAIL_PASSWORD', None)
    mail_use_tls = os.environ.get('MAIL_USE_TLS', False)
    mail_use_ssl = os.environ.get('MAIL_USE_SSL', False)
    mail_default_sender = os.environ.get('MAIL_DEFAULT_SENDER', None)
    mail_max_emails = os.environ.get('MAIL_MAX_EMAILS', None)
    mail_suppress_send = os.environ.get('MAIL_SUPPRESS_SEND', False)
    mail_ascii_attachments = os.environ.get('MAIL_ASCII_ATTACHMENTS', False)
    mail_debug = os.environ.get('MAIL_DEBUG', False)
    mail_ssl_keyfile = os.environ.get('MAIL_SSL_KEYFILE', None)
    mail_ssl_certfile = os.environ.get('MAIL_SSL_CERTFILE', None)
    mail_ssl_password = os.environ.get('MAIL_SSL_PASSWORD', None)
    mail_ssl_cert_reqs = os.environ.get('MAIL_SSL_CERT_REQS', None)
    mail_ssl_ca_certs = os.environ.get('MAIL_SSL_CA_CERTS', None)
    mail_use_localtime = os.environ.get('MAIL_USE_LOCALTIME', False)
    mail_subject_prefix = os.environ.get('MAIL_SUBJECT_PREFIX', None)
    mail_template_folder = os.environ.get('MAIL_TEMPLATE_FOLDER', None)
    mail_max_message_parts = os.environ.get('MAIL_MAX_MESSAGE_PARTS', None)
    mail_message_default_subtype = os.environ.get('MAIL_MESSAGE_DEFAULT_SUBTYPE', None)
    mail_attachments = os.environ.get('MAIL_ATTACHMENTS', None)
    mail_bcc_sender = os.environ.get('MAIL_BCC_SENDER', None)
    mail_suppress_send = os.environ.get('MAIL_SUPPRESS_SEND', False)
    mail_suppress_send_to = os.environ.get('MAIL_SUPPRESS_SEND_TO', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_message = os.environ.get('MAIL_SUPPRESS_SEND_MESSAGE', None)
    mail_suppress_send_to_message = os.environ.get('MAIL_SUPPRESS_SEND_TO_MESSAGE', None)
    mail_suppress_send_