# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from sweetrpg_library_model.model.review import Review
from sweetrpg_api_core.schema.base import BaseAPISchema


class ReviewAPISchema(BaseAPISchema):
    model_class = Review

    class Meta:
        type_ = "review"
        self_view = "review_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "review_list"

    name = fields.Str()  # , load_only=True)
    slug = fields.Str()  # , load_only=True)
    system = fields.Str()  # , load_only=True)
