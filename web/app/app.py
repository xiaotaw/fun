# encoding: utf-8

from flask import Flask


def create_app():
    """App Factory
    """
    app = Flask(__name__)

    # initialize extensions
    from .ext import bootstrap
    bootstrap.init_app(app)

    # register blueprints
    from .view.selfie2anime import bp
    app.register_blueprint(bp)

    return app
