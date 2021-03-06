from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"


# this function creates the app from flask.
def create_app():
    #Intalizize the app
    app = Flask(__name__)
    #enycrption key for the app
    app.config['SECRET_KEY'] = "asdawwrrx fefegerc asdfesa"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # this is importing the view from the views file
    from .views import views
    #importing the view from the auth file
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, name="auth", url_prefix='/')

    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")