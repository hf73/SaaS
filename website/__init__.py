from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from website import models

db = SQLAlchemy()
DB_NAME = "database.db"
DB2_NAME = "database2.db" #Named Database 2 to avoid confusions


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_BINDS']={'two' : f'sqlite:////{DB2_NAME}'} #Using SQLAlchemy Binds allows for multiple databases to communicate and copy each others information
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

class One(db.Model): #Creates the First DataBase
    id= db.Column(db.Integer, primary_key=True)
    
class Two(db.Model):#Creates the Second Database
    __bind_key__ = 'two'
    id= db.Column(db.Integer, primary_key=True)



def create_database(Model):#fills all information needed from auth file and creates both Databases
    if not path.exists('website/' + DB_NAME + DB2_NAME):
        with Model.app_context():  
            db.create_all(app=Model)
            print('Created Databases!')
