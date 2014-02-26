from webapp import app
from webapp import os, config

if 'APP_DEV' in os.environ:
    app.run(host=config.DevelopmentConfig.HOST)
else:
    app.run()
