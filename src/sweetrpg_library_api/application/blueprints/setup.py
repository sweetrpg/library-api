# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

from sweetrpg_library_model.model.author import Author
from sweetrpg_library_model.db.author.document import AuthorDocument
from sweetrpg_library_model.db.author.schema import AuthorSchema
from sweetrpg_library_model.model.volume import Volume
from sweetrpg_library_model.db.volume.document import VolumeDocument
from sweetrpg_library_model.model.volume_property import VolumeProperty
from sweetrpg_library_model.db.volume_property.document import VolumePropertyDocument


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
    "volume_property": {
        "model": VolumeProperty,
        # "schema": VolumePropertySchema,
        "document": VolumePropertyDocument,
        "type": "volume_property",
        "collection": "volume_properties",
        "properties": {"volumes": "volume"},
    },
}
