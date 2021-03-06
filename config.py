import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://ron:3159@localhost/pitch'

    MAIL_SERVER = 'smtp.googlemail.com'

    MAIL_PORT = 587

    MAIL_USE_TLS = True

    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")

    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    pass

class ProdConfig(Config):

    pass


class DevConfig(Config):

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}