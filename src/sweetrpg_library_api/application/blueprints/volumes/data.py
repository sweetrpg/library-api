# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from flask import current_app
from flask_rest_jsonapi.data_layers.base import BaseDataLayer
from flask_rest_jsonapi.exceptions import ObjectNotFound
from sweetrpg_library_model.volume import Volume
from .schema import VolumeAPISchema
from sweetrpg_library_api.application.db import db
from sweetrpg_library_api.application.db.volume.schema import VolumeDBSchema
from sweetrpg_common.db.mongodb.repo import MongoDataRepository


class VolumeData(BaseDataLayer):

    def __init__(self, kwargs):
        """Intialize an data layer instance with kwargs
        :param dict kwargs: information about data layer instance
        """
        print("init: %s", kwargs)

        if kwargs.get('methods') is not None:
            self.bound_rewritable_methods(kwargs['methods'])
            kwargs.pop('methods')

        kwargs.pop('class', None)

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.volume_repo = MongoDataRepository(mongo=db, model=self.model, schema=self.schema, id_attr='slug')

    def create_object(self, data, view_kwargs):
        """Create an object
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        :return DeclarativeMeta: an object
        """
        current_app.logger.info("self: %s, data: %s, view_kwargs: %s", self, data, view_kwargs)

        self.before_create_object(data, view_kwargs)

        # TODO
        obj = None

        self.after_create_object(obj, data, view_kwargs)

        return obj

    def get_object(self, view_kwargs, qs):
        """Retrieve an object
        :params dict view_kwargs: kwargs from the resource view
        :return DeclarativeMeta: an object
        """
        current_app.logger.info("self: %s, view_kwargs: %s, qs: %s", self, view_kwargs, qs)

        self.before_get_object(view_kwargs)

        record_id = view_kwargs['id']
        current_app.logger.info("Looking up record for ID '%s'...", record_id)
        volume_record = self.volume_repo.get(record_id)
        if not volume_record:
            raise ObjectNotFound(f'No Volume found for ID {view_kwargs["id"]}')
        current_app.logger.info("self: %s, volume_record: %s", self, volume_record)

        self.after_get_object(volume_record, view_kwargs)

        return volume_record

    def get_collection(self, qs, view_kwargs, filters=None):
        """Retrieve a collection of objects
        :param QueryStringManager qs: a querystring manager to retrieve information from url
        :param dict view_kwargs: kwargs from the resource view
        :param dict filters: A dictionary of key/value filters to apply to the eventual query
        :return tuple: the number of object and the list of objects
        """
        current_app.logger.info("self: %s, qs: %s, view_kwargs: %s, filters: %s", self, qs, view_kwargs, filters)
        querystring = qs.querystring
        current_app.logger.info("querystring: %s, fields: %s, sorting: %s, include: %s, pagination: %s", querystring, qs.fields, qs.sorting, qs.include, qs.pagination)

        self.before_get_collection(qs, view_kwargs)

        query = self.query(view_kwargs)
        query = self.paginate_query(query, qs.pagination)

        objs = []

        collection = self.after_get_collection(collection, qs, view_kwargs)

        return len(objs), objs

    def update_object(self, obj, data, view_kwargs):
        """Update an object
        :param DeclarativeMeta obj: an object
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if object have changed else False
        """
        current_app.logger.info("self: %s, obj: %s, data: %s, view_kwargs: %s", self, obj, data, view_kwargs)

        self.before_update_object(obj, data, view_kwargs)

        # TODO

        self.after_update_object(obj, data, view_kwargs)

    def delete_object(self, obj, view_kwargs):
        """Delete an item through the data layer
        :param DeclarativeMeta obj: an object
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, view_kwargs: %s", self, obj, view_kwargs)

        self.before_delete_object(obj, view_kwargs)

        # TODO

        self.after_delete_object(obj, view_kwargs)

    def create_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Create a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("self: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, json_data, relationship_field, related_id_field, view_kwargs)

        self.before_create_relationship(json_data, relationship_field, related_id_field, view_kwargs)

        # TODO
        obj = None

        self.after_create_relationship(obj, updated, json_data, relationship_field, related_id_field, view_kwargs)

        return obj, updated

    def get_relationship(self, relationship_field, related_type_, related_id_field, view_kwargs):
        """Get information about a relationship
        :param str relationship_field: the model attribute used for relationship
        :param str related_type_: the related resource type
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return tuple: the object and related object(s)
        """
        current_app.logger.info("self: %s, relationship_field: %s, related_type_: %s, related_id_field: %s, view_kwargs: %s", self, relationship_field, related_type_, related_id_field, view_kwargs)

        self.before_get_relationship(relationship_field, related_type_, related_id_field, view_kwargs)

        # TODO

        self.after_get_relationship(obj, related_objects, relationship_field, related_type_, related_id_field,
                                    view_kwargs)

        if isinstance(related_objects, InstrumentedList):
            return obj,\
                [{'type': related_type_, 'id': getattr(obj_, related_id_field)} for obj_ in related_objects]
        else:
            return obj, {'type': related_type_, 'id': getattr(related_objects, related_id_field)}

    def update_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Update a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("self: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, json_data, relationship_field, related_id_field, view_kwargs)

        self.before_update_relationship(json_data, relationship_field, related_id_field, view_kwargs)

        # TODO
        obj = None

        self.after_update_relationship(obj, updated, json_data, relationship_field, related_id_field, view_kwargs)

        return obj, updated

    def delete_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Delete a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, json_data, relationship_field, related_id_field, view_kwargs)

        self.before_delete_relationship(json_data, relationship_field, related_id_field, view_kwargs)

        # TODO

        self.after_delete_relationship(obj, updated, json_data, relationship_field, related_id_field, view_kwargs)

        return obj, updated

    def query(self, view_kwargs):
        """Construct the base query to retrieve wanted data
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, view_kwargs: %s", self, view_kwargs)
        return []

    def paginate_query(self, query, paginate_info):
        """Paginate query according to jsonapi 1.0
        :param Query query: sqlalchemy queryset
        :param dict paginate_info: pagination information
        :return Query: the paginated query
        """
        current_app.logger.info("self: %s, query: %s, paginate_info: %s", self, query, paginate_info)

        if int(paginate_info.get('size', 1)) == 0:
            return query

        page_size = int(paginate_info.get('size', 0)) or current_app.config['PAGE_SIZE']
        query = query.limit(page_size)
        if paginate_info.get('number'):
            query = query.offset((int(paginate_info['number']) - 1) * page_size)

        return query

    def before_create_object(self, data, view_kwargs):
        """Provide additional data before object creation
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, data: %s, view_kwargs: %s", self, data, view_kwargs)

    def after_create_object(self, obj, data, view_kwargs):
        """Provide additional data after object creation
        :param obj: an object from data layer
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, %s, data: %s, view_kwargs: %s", self, obj, data, view_kwargs)

    def before_get_object(self, view_kwargs):
        """Make work before to retrieve an object
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, data: %s, view_kwargs: %s", self, data, view_kwargs)

    def after_get_object(self, obj, view_kwargs):
        """Make work after to retrieve an object
        :param obj: an object from data layer
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, view_kwargs: %s", self, obj, view_kwargs)

    def before_get_collection(self, qs, view_kwargs):
        """Make work before to retrieve a collection of objects
        :param QueryStringManager qs: a querystring manager to retrieve information from url
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, qs: %s, view_kwargs: %s", self, qs, view_kwargs)

    def after_get_collection(self, collection, qs, view_kwargs):
        """Make work after to retrieve a collection of objects
        :param iterable collection: the collection of objects
        :param QueryStringManager qs: a querystring manager to retrieve information from url
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, collection: %s, qs: %s, view_kwargs: %s", self, collection, qs, view_kwargs)

        # TODO

        return collection

    def before_update_object(self, obj, data, view_kwargs):
        """Make checks or provide additional data before update object
        :param obj: an object from data layer
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, data: %s, view_kwargs: %s", self, obj, data, view_kwargs)

    def after_update_object(self, obj, data, view_kwargs):
        """Make work after update object
        :param obj: an object from data layer
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, data: %s, view_kwargs: %s", self, obj, data, view_kwargs)

    def before_delete_object(self, obj, view_kwargs):
        """Make checks before delete object
        :param obj: an object from data layer
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, view_kwargs: %s", self, obj, view_kwargs)

    def after_delete_object(self, obj, view_kwargs):
        """Make work after delete object
        :param obj: an object from data layer
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, view_kwargs: %s", self, obj, view_kwargs)

    def before_create_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work before to create a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("self: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, relationship_field, related_id_field, view_kwargs)

    def after_create_relationship(self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work after to create a relationship
        :param obj: an object from data layer
        :param bool updated: True if object was updated else False
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("self: %s, obj: %s, update: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs)

    def before_get_relationship(self, relationship_field, related_type_, related_id_field, view_kwargs):
        """Make work before to get information about a relationship
        :param str relationship_field: the model attribute used for relationship
        :param str related_type_: the related resource type
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return tuple: the object and related object(s)
        """
        current_app.logger.info("self: %s, relationship_field: %s, related_type_: %s, related_id_field: %s, view_kwargs: %s", self, relationship_field, related_type_, related_id_field, view_kwargs)

    def after_get_relationship(self, obj, related_objects, relationship_field, related_type_, related_id_field,
                               view_kwargs):
        """Make work after to get information about a relationship
        :param obj: an object from data layer
        :param iterable related_objects: related objects of the object
        :param str relationship_field: the model attribute used for relationship
        :param str related_type_: the related resource type
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return tuple: the object and related object(s)
        """
        current_app.logger.info("self: %s, obj: %s, update: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs)

    def before_update_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work before to update a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("self: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, json_data, relationship_field, related_id_field, view_kwargs)

    def after_update_relationship(self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work after to update a relationship
        :param obj: an object from data layer
        :param bool updated: True if object was updated else False
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("self: %s, obj: %s, update: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs)

    def before_delete_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work before to delete a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, json_data, relationship_field, related_id_field, view_kwargs)

    def after_delete_relationship(self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work after to delete a relationship
        :param obj: an object from data layer
        :param bool updated: True if object was updated else False
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("self: %s, obj: %s, update: %s, json_data: %s, relationship_field: %s, related_id_field: %s, view_kwargs: %s", self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs)