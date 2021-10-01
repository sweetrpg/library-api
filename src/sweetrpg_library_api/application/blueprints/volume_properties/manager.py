# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import VolumePropertyAPISchema
from ..data import APIData



class VolumePropertyList(ResourceList):
    schema = VolumePropertyAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume_property",
    }


class VolumePropertyDetail(ResourceDetail):
    schema = VolumePropertyAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume_property",
    }


class VolumePropertyVolumeRelationship(ResourceRelationship):
    schema = VolumePropertyAPISchema
    data_layer = {
        "class": APIData,
        "type": "volume_property",
    }
