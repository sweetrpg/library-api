# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""main.py

Creates a Flask app instance and registers various services and middleware.
"""


from flask import Flask, session
from flask_migrate import Migrate
from flask_session import Session
from dotenv import load_dotenv, find_dotenv
from sweetrpg_library_api.application.cache import cache
from sweetrpg_library_api.application import constants
from logging.config import dictConfig
from sweetrpg_library_api.application.blueprints import error_page
from werkzeug.exceptions import HTTPException
from redis.client import Redis
from sentry_sdk.integrations.wsgi import SentryWsgiMiddleware
import analytics


ENV_FILE = find_dotenv()
if ENV_FILE:
    print(f"Loading environment from {ENV_FILE}...")
    load_dotenv(ENV_FILE)


def create_app(app_name=constants.APPLICATION_NAME):
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s %(module)s/%(funcName)s: %(message)s",
                }
            },
            "handlers": {"wsgi": {"class": "logging.StreamHandler", "stream": "ext://flask.logging.wsgi_errors_stream", "formatter": "default"}},
            "root": {"level": "DEBUG", "handlers": ["wsgi"]},
        }
    )

    app = Flask(app_name)
    app.config.from_object("sweetrpg_library_api.application.config.BaseConfig")
    # env = DotEnv(app)
    cache.init_app(app)

    analytics.write_key = app.config.get("SEGMENT_WRITE_KEY")
    analytics.debug = app.config.get("DEBUG") or False

    session = Session(app)

    # cors = CORS(app, resources={r"/*": {"origins": "*"}})

    sentry = SentryWsgiMiddleware(app)

    # from sweetrpg_library_api.application.blueprints.volumes import blueprint as volumes_blueprint
    # app.register_blueprint(volumes_blueprint, url_prefix="/volumes")

    from sweetrpg_library_api.application.blueprints.volumes import setup_routes as setup_volume_routes

    setup_volume_routes(app)

    from sweetrpg_library_api.application.blueprints.volume_properties import setup_routes as setup_volume_property_routes

    setup_volume_property_routes(app)

    from sweetrpg_library_api.application.blueprints.authors import setup_routes as setup_author_routes

    setup_author_routes(app)

    # from application.blueprints.api import blueprint as api_blueprint
    # app.register_blueprint(api_blueprint, url_prefix="/api/v1")
    #
    # from application.blueprints.apps import blueprint as apps_blueprint
    # app.register_blueprint(apps_blueprint, url_prefix="/apps")
    #
    # from application.blueprints.account import blueprint as account_blueprint
    # app.register_blueprint(account_blueprint, url_prefix="/account")
    #
    # from application.blueprints.auth import blueprint as auth_blueprint
    # app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from sweetrpg_library_api.application.blueprints.health import blueprint as health_blueprint

    app.register_blueprint(health_blueprint, url_prefix="/health")

    # from application.blueprints.billing import blueprint as billing_blueprint
    # app.register_blueprint(billing_blueprint, url_prefix="/billing")

    from sweetrpg_library_api.application.db import db

    # from flask_migrate import Migrate
    # db.init_app(app, **app.config['DB_OPTS'])
    db.init_app(app)
    app.logger.info("Database: %s", db)
    # db.init_app(app)
    migrate = Migrate(app, db)
    # setup_indexes(app, db.db)
    # register_models(app)

    # vue = Vue(app)

    # app.wsgi_app = SassMiddleware(app.wsgi_app, {
    #     'application': ('static/sass', 'static/css', '/static/css')
    # })
    # scss = Scss(app, static_dir='static', asset_dir='assets')

    # stripe.api_key = app.config['STRIPE_API_KEY']

    print(app.url_map)

    app.debug = app.config["DEBUG"]

    return app
