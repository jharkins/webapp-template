# Default configuration is production
# enable dev mode:
# export APP_DEV=1


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = ''
    LOG_LEVEL = 'WARNING'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///webapp.db'
    HOST = '127.0.0.1'


# Always ready for production
#class ProductionConfig(Config):

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    LOG_LEVEL = 'DEBUG'


class TestingConfig(Config):
    TESTING = True
