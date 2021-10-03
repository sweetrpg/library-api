# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import VolumeAPISchema
from sweetrpg_api_core.data import APIData
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_library_api.application.db import db


class VolumeList(ResourceList):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
        "model": Volume,
        "db": db,
    }


class VolumeDetail(ResourceDetail):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
        "model": Volume,
        "db": db,
    }


class VolumeAuthorRelationship(ResourceRelationship):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
        "model": Volume,
        "db": db,
    }
