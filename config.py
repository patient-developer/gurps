import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

DEVELOPMENT = 'development'
PRODUCTION = 'production'
DEFAULT = 'default'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    DEVELOPMENT: DevelopmentConfig,
    PRODUCTION: Config,

    DEFAULT: DevelopmentConfig
}
