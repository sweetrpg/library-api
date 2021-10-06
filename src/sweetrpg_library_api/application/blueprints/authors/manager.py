# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import AuthorAPISchema
from sweetrpg_library_model.model.author import Author
from sweetrpg_api_core.data import APIData
from sweetrpg_library_api.application.db import db
from sweetrpg_library_api.application.blueprints.setup import model_info


class AuthorList(ResourceList):
    schema = AuthorAPISchema
    data_layer = {"class": APIData, "type": "author", "model": Author, "db": db, "model_info": model_info}


class AuthorDetail(ResourceDetail):
    schema = AuthorAPISchema
    data_layer = {"class": APIData, "type": "author", "model": Author, "db": db, "model_info": model_info}


class AuthorVolumeRelationship(ResourceRelationship):
    schema = AuthorAPISchema
    data_layer = {"class": APIData, "type": "author", "model": Author, "db": db, "model_info": model_info}
