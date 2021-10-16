# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from flask_rest_jsonapi import ResourceList, ResourceDetail, ResourceRelationship
from .schema import ReviewAPISchema
from sweetrpg_api_core.data import APIData
from sweetrpg_library_model.model.review import Review
from sweetrpg_library_api.application.db import db
from sweetrpg_library_api.application.blueprints.setup import model_info


class ReviewList(ResourceList):
    schema = ReviewAPISchema
    data_layer = {"class": APIData, "type": "review", "model": Review, "db": db, "model_info": model_info}


class ReviewDetail(ResourceDetail):
    schema = ReviewAPISchema
    data_layer = {
        "class": APIData,
        "type": "review",
        "model": Review,
        "db": db,
        "model_info": model_info
    }


class ReviewAuthorRelationship(ResourceRelationship):
    schema = ReviewAPISchema
    data_layer = {
        "class": APIData,
        "type": "review",
        "model": Review,
        "db": db,
        "model_info": model_info
    }