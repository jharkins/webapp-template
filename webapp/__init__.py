from flask import Flask
import os
#import logging
import config

from flask.ext.login import LoginManager, login_required, login_user, \
    current_user, logout_user

app = Flask(__name__)

# enable dev mode:
# export APP_DEV=1
if 'APP_DEV' in os.environ:
    app.config.from_object('config.DevelopmentConfig')
    app.logger.setLevel(config.DevelopmentConfig.LOG_LEVEL)
else:
    app.config.from_object('config.Config')


# setup logging
#file_handler = logging.FileHandler('app.log')
#app.logger.addHandler(file_handler)

# config for forms
app.secret_key = 'p?!sUG,2*kHiVsLq'
app.crsf_enabled = True

# Setup login manager
lm = LoginManager()
lm.init_app(app)


import webapp.views
