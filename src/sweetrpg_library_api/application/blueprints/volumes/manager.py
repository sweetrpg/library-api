# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import VolumeAPISchema
from sweetrpg_library_model.volume import Volume
from .data import VolumeData
from sweetrpg_library_api.application.db.volume.schema import VolumeDBSchema


class VolumeList(ResourceList):
    schema = VolumeAPISchema
    data_layer = {
        'class': VolumeData,
        'model': Volume,
        'schema': VolumeDBSchema,
    }


class VolumeDetail(ResourceDetail):
    schema = VolumeAPISchema
    data_layer = {
        'class': VolumeData,
        'model': Volume,
        'schema': VolumeDBSchema,
    }


class VolumeRelationship(ResourceRelationship):
    schema = VolumeAPISchema
    data_layer = {
        'class': VolumeData,
        'model': Volume,
        'schema': VolumeDBSchema,
    }
