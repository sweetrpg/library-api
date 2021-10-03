# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import functools

from flask import Blueprint
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
from sweetrpg_api_core.data import APIData
from sweetrpg_library_model.model.author import Author
from sweetrpg_library_model.db.author.document import AuthorDocument
from sweetrpg_library_model.db.author.schema import AuthorSchema
from .manager import AuthorList, AuthorDetail, AuthorVolumeRelationship


author_model_info = {
    "author": {
        "model": Author,
        "schema": AuthorSchema,
        "document": AuthorDocument,
        "type": "author",
        "collection": "authors",
        "properties": {"volumes": "volume"},
    },
}


def setup_routes(app):
    app.logger.info("Registering author models...")
    for model_name, model_info in author_model_info.items():
        APIData.add_model(model_name, model_info)

    app.logger.info("Setting up routes for Authors API")
    api = Api(app)
    api.route(AuthorList, "author_list", "/authors/")
    api.route(AuthorDetail, "author_detail", "/authors/<id>")
    api.route(AuthorVolumeRelationship, "author_volumes", "/authors/<id>/relationships/volumes")
