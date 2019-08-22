# encoding: utf-8

"""
App will be called by Gunicorn
"""

from werkzeug.middleware.proxy_fix import ProxyFix

from .app import create_app

app = create_app()
app.wsgi_app = ProxyFix(app.wsgi_app)
