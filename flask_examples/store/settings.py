class Config(object):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'


class ProductionConfig(Config):

    DEBUG = False
