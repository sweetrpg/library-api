# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from marshmallow import Schema, fields, EXCLUDE
from marshmallow import post_load
from sweetrpg_library_model.volume import Volume


class VolumeDBSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_object(self, data, **kwargs):
        print(f'data: {data}')
        print(f'kwargs: {kwargs}')
        name = data.pop('name')
        slug = data.pop('slug')
        system = data.pop('system')
        return Volume(name, slug, system, **data)

    id = fields.Str() # as_string=True, dump_only=True)
    name = fields.Str() # required=True) #, load_only=True)
    slug = fields.Str() # required=True) #, load_only=True)
    isbn = fields.Str() #, load_only=True)
    system = fields.Str() # required=True) #, load_only=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
