# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from flask_rest_jsonapi import ResourceList
from .schema import VolumeSchema
from sweetrpg_library_model.volume import Volume
from .data import VolumeData


class VolumeList(ResourceList):
    schema = VolumeSchema
    data_layer = {
        'class': VolumeData,
        'model': Volume,
    }
