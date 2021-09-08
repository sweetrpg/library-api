# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

import functools

from flask import Blueprint
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship

blueprint = Blueprint("authors", __name__, url_prefix="/authors")


from .manager import AuthorList, AuthorDetail, AuthorVolumeRelationship

def setup_routes(app):
    app.logger.info("Setting up routes for Authors API")
    api = Api(app)
    api.route(AuthorList, 'author_list', '/authors/')
    api.route(AuthorDetail, 'author_detail', '/authors/<id>')
    api.route(AuthorVolumeRelationship, 'author_volumes', '/authors/<id>/relationships/volumes')
