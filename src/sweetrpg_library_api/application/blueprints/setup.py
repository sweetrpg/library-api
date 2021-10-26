# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_objects.model.author import Author
from sweetrpg_library_objects.db.author.document import AuthorDocument
from sweetrpg_library_objects.model.volume import Volume
from sweetrpg_library_objects.db.volume.document import VolumeDocument
from sweetrpg_library_objects.model.publisher import Publisher
from sweetrpg_library_objects.db.publisher.document import PublisherDocument
from sweetrpg_library_objects.model.review import Review
from sweetrpg_library_objects.db.review.document import ReviewDocument
from sweetrpg_library_objects.model.system import System
from sweetrpg_library_objects.db.system.document import SystemDocument
from sweetrpg_library_objects.model.studio import Studio
from sweetrpg_library_objects.db.studio.document import StudioDocument
from sweetrpg_library_objects.model.tag import Tag
from sweetrpg_library_objects.db.tag.document import TagDocument
from sweetrpg_library_objects.model.volume_property import VolumeProperty
from sweetrpg_library_objects.db.volume_property.document import VolumePropertyDocument


model_info = {
    "author": {
        "model": Author,
        # "schema": AuthorSchema,
        "document": AuthorDocument,
        "type": "author",
        "collection": "authors",
        "properties": {"volumes": "volume"},
    },
    "volume": {
        "model": Volume,
        # "schema": VolumeSchema,
        "document": VolumeDocument,
        "type": "volume",
        "collection": "volumes",
        "properties": {"authors": "author", "properties": "volume_property"},
    },
    "publisher": {
        "model": Publisher,
        # "schema": PublisherSchema,
        "document": PublisherDocument,
        "type": "publisher",
        "collection": "publishers",
        "properties": {},
    },
    "review": {
        "model": Review,
        # "schema": ReviewSchema,
        "document": ReviewDocument,
        "type": "review",
        "collection": "reviews",
        "properties": {"volumes": "volume"},
    },
    "studio": {
        "model": Studio,
        # "schema": StudioSchema,
        "document": StudioDocument,
        "type": "studio",
        "collection": "studios",
        "properties": {"authors": "author"},
    },
    "system": {
        "model": System,
        # "schema": SystemSchema,
        "document": SystemDocument,
        "type": "system",
        "collection": "systems",
        "properties": {},
    },
    "tag": {
        "model": Tag,
        # "schema": TagSchema,
        "document": TagDocument,
        "type": "tag",
        "collection": "tags",
        "properties": {},
    },
    "volume_property": {
        "model": VolumeProperty,
        # "schema": VolumePropertySchema,
        "document": VolumePropertyDocument,
        "type": "volume_property",
        "collection": "volume_properties",
        "properties": {"volumes": "volume"},
    },
}
