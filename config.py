import os
class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'pitches'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass
    



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:MARtin1999@localhost/pitches'
    


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://martin:MARtin1999@localhost/pitches'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}