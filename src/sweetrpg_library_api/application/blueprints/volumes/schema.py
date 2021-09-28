# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from marshmallow import post_load
from sweetrpg_library_model.model.volume import Volume
from flask import current_app


class VolumeAPISchema(Schema):
    class Meta:
        type_ = "volume"
        self_view = "volume_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "volume_list"

    @post_load
    def make_object(self, data, **kwargs):
        current_app.logger.debug("self: %s, data: %s, kwargs: %s", self, data, kwargs)
        return Volume(**data)

    id = fields.Str()  # as_string=True, dump_only=True)
    name = fields.Str()  # , load_only=True)
    slug = fields.Str()  # , load_only=True)
    isbn = fields.Str()  # , load_only=True)
    system = fields.Str()  # , load_only=True)
    authors = Relationship(
        self_view="volume_authors",
        self_view_kwargs={"id": "<id>"},
        related_view="author_list",
        related_view_kwargs={"volume_id": "<id>"},
        many=True,
        schema="AuthorAPISchema",
        type_="author",
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime()
