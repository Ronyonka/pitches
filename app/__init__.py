from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os



bootstrap = Bootstrap()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'

def create_app(config_name):

    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # if not app.debug and not app.testing:
    #         if app.config['MAIL_SERVER']:
    #             auth = None
    #             if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
    #                 auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    #             secure = None
    #             if app.config['MAIL_USE_TLS']:
    #                 secure = ()
    #             mail_handler = SMTPHandler(
    #                 mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
    #                 fromaddr='no-reply@' + app.config['MAIL_SERVER'],
    #                 toaddrs=app.config['ADMINS'], subject='Microblog Failure',
    #                 credentials=auth, secure=secure)
    #             mail_handler.setLevel(logging.ERROR)
    #             app.logger.addHandler(mail_handler)
    #             if not os.path.exists('logs'):
    #                 os.mkdir('logs')
    #             file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
    #                                             backupCount=10)
    #             file_handler.setFormatter(logging.Formatter(
    #                 '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    #             file_handler.setLevel(logging.INFO)
    #             app.logger.addHandler(file_handler)

    #             app.logger.setLevel(logging.INFO)
    #             app.logger.info('Microblog startup')

    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '')

    return app