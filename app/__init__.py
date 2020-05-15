from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_login import login_manager
from flask_mail import Mail
from sqlalchemy import create_engine
from flask_bootstrap import Bootstrap
import arrow



#INSTANCES OF EXTENTIONS
login_manager = LoginManager()
login_manager._session_protection = 'strong'
login_manager.login_view = 'auth.login'
db=SQLAlchemy()
login_manager=LoginManager()
mail = Mail()
bootstrap=Bootstrap()


def create_app(config_name):
    app=Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #REGISTER CONFIGURASTION
    app.config.from_object(config_options[config_name])


    #REGISTER EXTENTONS
    login_manager.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    
    #REGISTER BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix='/authenticate')




    def format_date(value):
        dt = arrow.get(value).to('UTC')
        return arrow.get(value).humanize()


    app.jinja_env.filters['timeago'] = format_date


    return app