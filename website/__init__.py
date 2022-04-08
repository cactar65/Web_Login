from flask import Flask


# this function creates the app from flask.
def create_app():
    #Intalizize the app
    app = Flask(__name__)
    #enycrption key for the app
    app.config['SECRET_KEY'] = "asdawwrrx fefegerc asdfesa"

    # this is importing the view from the views file
    from .views import views
    #importing the view from the auth file
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, name="auth", url_prefix='/')


    return app