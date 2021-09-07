# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from marshmallow import post_load
from sweetrpg_library_model.volume import Volume


class VolumeAPISchema(Schema):
    class Meta:
        type_ = 'volume'
        self_view = 'volume_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'volume_list'

    @post_load
    def make_object(self, data, **kwargs):
        print(f'data: {data}')
        print(f'kwargs: {kwargs}')
        return Volume('', **data)

    id = fields.Str() # as_string=True, dump_only=True)
    name = fields.Str() # required=True) #, load_only=True)
    slug = fields.Str() # required=True) #, load_only=True)
    isbn = fields.Str() #, load_only=True)
    system = fields.Str() # required=True) #, load_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
