# Default configuration is production
# enable dev mode:
# export APP_DEV=1
import os


class Config(object):
    basedir = "{0}/webapp/lib/".format(
                os.path.abspath(os.path.dirname(__file__)))
    DEBUG = False
    TESTING = False
    LOG_LEVEL = 'WARNING'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'webapp.db')
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
    HOST = '127.0.0.1'


# Always ready for production
#class ProductionConfig(Config):

class DevelopmentConfig(Config):
    DEBUG = True
    HOST = '0.0.0.0'
    LOG_LEVEL = 'DEBUG'


class TestingConfig(Config):
    TESTING = True
