# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import logging

from sweetrpg_api_core.blueprints.health import register_health_check_service_hook

from sweetrpg_library_api.application.db import db


def _db_check():
    # db.connection
    return {
        'db': str(db),
        'connection': str(db.connection),
        'host': db.connection.host,
        'name': str(db.connection.get_default_database),
        'collections': [],
    }


def register_service_checks():
    logging.info("Registering health check service hook for 'database'...")
    register_health_check_service_hook('database', _db_check)
