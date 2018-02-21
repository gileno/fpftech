from flask import Flask

from .extensions import db
from .api.catalog import catalog_blueprint


def create_app(config_object):
    app = Flask('store')
    app.debug = True
    app.config.from_object(config_object)
    db.init_app(app)
    # blueprints
    app.register_blueprint(catalog_blueprint)
    return app
