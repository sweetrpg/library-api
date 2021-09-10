# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from marshmallow import post_load
from sweetrpg_library_model.author import Author


class AuthorAPISchema(Schema):
    class Meta:
        type_ = 'author'
        self_view = 'author_detail'
        self_view_kwargs = {'id': '<id>'}
        self_view_many = 'author_list'

    @post_load
    def make_object(self, data, **kwargs):
        return Author('name', **data)

    id = fields.Str() # as_string=True, dump_only=True)
    name = fields.Str() # required=True) #, load_only=True)
    volumes = Relationship(self_view='author_volumes',
                           self_view_kwargs={'id': '<id>'},
                           related_view='volume_list',
                           related_view_kwargs={'author_id': '<id>'},
                           many=True,
                           schema='VolumeAPISchema',
                           type_='volume')
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
    deleted_at = fields.DateTime()
