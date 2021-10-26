# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from sweetrpg_library_objects.api.volume.schema import VolumeAPISchema
from sweetrpg_api_core.data import APIData
from sweetrpg_library_objects.model.volume import Volume
from sweetrpg_library_api.application.db import db
from sweetrpg_library_api.application.blueprints.setup import model_info


class VolumeList(ResourceList):
    disable_oauth = True
    schema = VolumeAPISchema
    data_layer = {"class": APIData, "type": "volume", "model": Volume, "db": db, "model_info": model_info}


class VolumeDetail(ResourceDetail):
    disable_oauth = True
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
        "model": Volume,
        "db": db,
        "model_info": model_info
    }


class VolumeAuthorRelationship(ResourceRelationship):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
        "model": Volume,
        "db": db,
        "model_info": model_info
    }
