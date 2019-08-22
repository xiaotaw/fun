# encoding: utf-8

import os
from flask import Flask

APP = os.environ['APP']
APP_DIR = os.path.abspath(os.path.dirname(__file__))


def create_app(config=None):
    """App Factory
    """
    app = Flask(__name__)
    app.config.from_object('envcfg.json.%s' % APP)
    app.config.from_object(config)
    app.config['APP_DIR'] = APP_DIR

    # initialize extensions
    from .ext import bootstrap
    bootstrap.init_app(app)

    # register blueprints
    from .view.selfie2anime import bp
    app.register_blueprint(bp)

    return app
