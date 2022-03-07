def create_app(config_name):
    #...
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    #....

    from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

def create_app(config_name):
    #....
    #Initializing Flask Extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
#....