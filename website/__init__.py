from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#imports flask framework and database
from os import path
from flask_login import LoginManager


db = SQLAlchemy()
DB_NAME= "database.db"

def create_app():
    app = Flask(__name__) #initializes the app
    app.config['SECRET_KEY'] = 'a'  #secures website cookie and session data, the key can be anything
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/') #no prefix due to '/'
    app.register_blueprint(auth, url_prefix='/') 


    from .models import User

    with app.app_context():
        db.create_all()


    login_manager = LoginManager()
    login_manager.login_view = 'auth.login' #redirects to login if not already logged in
    login_manager.init_app(app)

    @login_manager.user_loader #telling flask how to load a user
    def load_user(id):
        return User.query.get(int(id)) #filters user by user id

    return app



