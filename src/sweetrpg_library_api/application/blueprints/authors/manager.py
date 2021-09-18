# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import AuthorAPISchema
from sweetrpg_library_model.model.author import Author
from ..data import APIData
from sweetrpg_library_model.db.author.schema import AuthorDBSchema


class AuthorList(ResourceList):
    schema = AuthorAPISchema
    data_layer = {
        "class": APIData,
        "type": "author",
    }


class AuthorDetail(ResourceDetail):
    schema = AuthorAPISchema
    data_layer = {
        "class": APIData,
        "type": "author",
    }


class AuthorVolumeRelationship(ResourceRelationship):
    schema = AuthorAPISchema
    data_layer = {
        "class": APIData,
        "type": "author",
    }
