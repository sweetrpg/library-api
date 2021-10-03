# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import functools

from flask import Blueprint
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
from sweetrpg_api_core.data import APIData
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_library_model.db.volume.document import VolumeDocument
from sweetrpg_library_model.db.volume.schema import VolumeSchema
from sweetrpg_library_model.model.volume_property import VolumeProperty
from sweetrpg_library_model.db.volume_property.document import VolumePropertyDocument
from sweetrpg_library_model.db.volume_property.schema import VolumePropertySchema
from .manager import VolumeList, VolumeDetail, VolumeAuthorRelationship


volume_model_info = {
    "volume": {
        "model": Volume,
        "schema": VolumeSchema,
        "document": VolumeDocument,
        "type": "volume",
        "collection": "volumes",
        "properties": {"authors": "author", "properties": "volume_property"},
    },
    "volume_property": {
        "model": VolumeProperty,
        "schema": VolumePropertySchema,
        "document": VolumePropertyDocument,
        "type": "volume_property",
        "collection": "volume_properties",
        "properties": {"volumes": "volume"},
    },
}


def setup_routes(app):
    app.logger.info("Registering volume models...")
    for model_name, model_info in volume_model_info.items():
        APIData.add_model(model_name, model_info)

    app.logger.info("Setting up routes for Volumes API")
    api = Api(app)
    api.route(VolumeList, "volume_list", "/volumes/")
    api.route(VolumeDetail, "volume_detail", "/volumes/<id>")
    api.route(VolumeAuthorRelationship, "volume_authors", "/volumes/<id>/relationships/authors")
