# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields


class VolumeSchema(Schema):
    class Meta:
        type_ = 'volume'
        self_view = 'volume_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'volume_list'

        id = fields.Integer(as_string=True, dump_only=True)
        name = fields.Str(required=True, load_only=True)
        slug = fields.Str(required=True, load_only=True)
        isbn = fields.Str(required=True, load_only=True)
        system = fields.Str(required=True, load_only=True)
        created_at = fields.Date()
        updated_at = fields.Date()
        deleted_at = fields.Date()
