from nturl2path import url2pathname
from flask import Flask

#creates the flask app
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app
