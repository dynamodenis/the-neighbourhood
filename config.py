import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


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