# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from marshmallow import post_load
from sweetrpg_library_model.model.volume_property import VolumeProperty
from flask import current_app


class VolumePropertyAPISchema(Schema):
    class Meta:
        type_ = "volume_property"
        self_view = "volume_property_detail"
        self_view_kwargs = {"id": "<id>"}
        self_view_many = "volume_property_list"

    @post_load
    def make_object(self, data, **kwargs):
        current_app.logger.debug("self: %s, data: %s, kwargs: %s", self, data, kwargs)
        return VolumeProperty(**data)

    id = fields.Str()  # as_string=True, dump_only=True)
    name = fields.Str()  # , load_only=True)
    type = fields.Str()  # , load_only=True)
    value = fields.Str()  # , load_only=True)
    volumes = Relationship(
        self_view="volume_property_volumes",
        self_view_kwargs={"id": "<id>"},
        related_view="volume_property_list",
        related_view_kwargs={"volume_property_id": "<id>"},
        many=True,
        schema="VolumeAPISchema",
        type_="volume",
    )
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime()
