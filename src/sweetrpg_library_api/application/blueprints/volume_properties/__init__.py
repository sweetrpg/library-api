# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import functools

from flask import Blueprint
from flask_rest_jsonapi import Api

blueprint = Blueprint("volumes", __name__, url_prefix="/volumes")


from .manager import VolumePropertyList, VolumePropertyDetail, VolumePropertyVolumeRelationship


def setup_routes(app):
    app.logger.info("Setting up routes for Volumes API")
    api = Api(app)
    api.route(VolumePropertyList, "volume_property_list", "/volume_properties/")
    api.route(VolumePropertyDetail, "volume_property_detail", "/volume_properties/<id>")
    api.route(VolumePropertyVolumeRelationship, "volume_property_volumes", "/volume_properties/<id>/relationships/volumes")
