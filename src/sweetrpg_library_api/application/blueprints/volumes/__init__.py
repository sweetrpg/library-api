# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import functools

from flask import Blueprint
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship

blueprint = Blueprint("volumes", __name__, url_prefix="/volumes")


from .manager import VolumeList, VolumeDetail, VolumeAuthorRelationship, VolumeVolumePropertyRelationship


def setup_routes(app):
    app.logger.info("Setting up routes for Volumes API")
    api = Api(app)
    api.route(VolumeList, "volume_list", "/volumes/")
    api.route(VolumeDetail, "volume_detail", "/volumes/<id>")
    api.route(VolumeAuthorRelationship, "volume_authors", "/volumes/<id>/relationships/authors")
    api.route(VolumeVolumePropertyRelationship, "volume_volume_properties", "/volumes/<id>/relationships/properties")
