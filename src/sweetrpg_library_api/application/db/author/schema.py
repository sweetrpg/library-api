# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from marshmallow import Schema, fields, EXCLUDE
from marshmallow import post_load
from sweetrpg_library_model.author import Author


class AuthorDBSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_object(self, data, **kwargs):
        name = data.pop('name', None)
        return Author(name, **data)

    id = fields.Str() # as_string=True, dump_only=True)
    name = fields.Str(required=True) #, load_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
