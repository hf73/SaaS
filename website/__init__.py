from nturl2path import url2pathname
from flask import Flask
from os import path

#import the database db = 
#creates the flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note

    create_database(app)

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME): #checks if the database exists
        db.create_all(app=app) #if it doesn't it creates it
        print('Created Database!')