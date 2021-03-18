import logging
import os

from app.config_common import *


# DEBUG can only be set to True in a development environment for security reasons
DEBUG = True


# Secret key for generating tokens
SECRET_KEY = 'ahsd8h123hasdohj2139hash'

# Admin credentials
ADMIN_CREDENTIALS = ('admin', 'pa$$word')

# Database choice
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG_TB_INTERCEPT_REDIRECTS = False

# Configuration of a Gmail account for sending mails
MAIL_CONFIGURED = False  # Change to True once the email is configured
MAIL_SERVER = None
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''
ADMINS = ['emailaddress@replacethisdomain.com']


LOG_FILE = True
LOG_MAXBYTES = 100000
LOG_BACKUPS = '1'
LOG_LEVEL = logging.DEBUG
LOG_PATH = APP_PATH = os.path.dirname(os.path.abspath(__file__))

LOG_ERROR = os.path.join(LOG_PATH,'error.log')
LOG_ERROR_LEVEL = logging.WARN
LOG_APPLICATION = os.path.join(LOG_PATH,'application.log')
LOG_APPLICATION_LEVEL = logging.DEBUG
