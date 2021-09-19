# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask import current_app
from flask_pymongo import PyMongo
import pymongo


db = PyMongo()

def setup_indexes(app, client):
    app.logger.info("Setting up database indexes...")
    client.volumes.create_index([('slug', pymongo.ASCENDING)], name='volume_slug', unique=True)
    client.volumes.create_index([('name', pymongo.ASCENDING)], name='volume_name')
    client.volumes.create_index([('system', pymongo.ASCENDING)], name='volume_system')
    client.authors.create_index([('name', pymongo.ASCENDING)], name='author_name')
