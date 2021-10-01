# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import VolumeAPISchema
from ..data import APIData


class VolumeList(ResourceList):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
    }


class VolumeDetail(ResourceDetail):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
    }


class VolumeAuthorRelationship(ResourceRelationship):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
    }


class VolumeVolumePropertyRelationship(ResourceRelationship):
    schema = VolumeAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume",
    }
