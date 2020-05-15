import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    MAIL_SERVER='stmp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')



class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://dynamo:den28041997is@localhost/neighbourhood'
    DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://dynamo:den28041997is@localhost/test_neighbourhood'

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}