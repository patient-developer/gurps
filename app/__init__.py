from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    from .hits import blueprint as hits_blueprint

    app.register_blueprint(hits_blueprint, url_prefix='/random-hit-locations')

    return app
