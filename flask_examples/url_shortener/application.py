from flask import Flask

from .extensions import db, migrate


def create_app(config_object):
    app = Flask('url_shortener')
    app.config.from_object(config_object)
    db.init_app(app)
    migrate.init_app(app, db)
    return app
