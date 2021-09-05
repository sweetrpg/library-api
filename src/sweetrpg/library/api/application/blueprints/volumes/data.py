# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

from flask import current_app
from flask_rest_jsonapi.data_layers.base import BaseDataLayer


class VolumeData(BaseDataLayer):
    def query(self, view_kwargs):
        current_app.logger.info("Query for volumes: %s", view_kwargs)

    def create_object(self, data, view_kwargs):
        """Create an object
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        :return DeclarativeMeta: an object
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def get_object(self, view_kwargs):
        """Retrieve an object
        :params dict view_kwargs: kwargs from the resource view
        :return DeclarativeMeta: an object
        """
        current_app.logger.info("%s, %s", self, view_kwargs)
        raise NotImplementedError

    def get_collection(self, qs, view_kwargs, filters=None):
        """Retrieve a collection of objects
        :param QueryStringManager qs: a querystring manager to retrieve information from url
        :param dict view_kwargs: kwargs from the resource view
        :param dict filters: A dictionary of key/value filters to apply to the eventual query
        :return tuple: the number of object and the list of objects
        """
        current_app.logger.info("%s, %s, %s", self, qs, view_kwargs, filters)
        raise NotImplementedError

    def update_object(self, obj, data, view_kwargs):
        """Update an object
        :param DeclarativeMeta obj: an object
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if object have changed else False
        """
        current_app.logger.info("%s, %s, %s, %s", self, obj, data, view_kwargs)
        raise NotImplementedError

    def delete_object(self, obj, view_kwargs):
        """Delete an item through the data layer
        :param DeclarativeMeta obj: an object
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, obj, view_kwargs)
        raise NotImplementedError

    def create_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Create a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def get_relationship(self, relationship_field, related_type_, related_id_field, view_kwargs):
        """Get information about a relationship
        :param str relationship_field: the model attribute used for relationship
        :param str related_type_: the related resource type
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return tuple: the object and related object(s)
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def update_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Update a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def delete_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Delete a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def query(self, view_kwargs):
        """Construct the base query to retrieve wanted data
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_create_object(self, data, view_kwargs):
        """Provide additional data before object creation
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def after_create_object(self, obj, data, view_kwargs):
        """Provide additional data after object creation
        :param obj: an object from data layer
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_get_object(self, view_kwargs):
        """Make work before to retrieve an object
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def after_get_object(self, obj, view_kwargs):
        """Make work after to retrieve an object
        :param obj: an object from data layer
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_get_collection(self, qs, view_kwargs):
        """Make work before to retrieve a collection of objects
        :param QueryStringManager qs: a querystring manager to retrieve information from url
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def after_get_collection(self, collection, qs, view_kwargs):
        """Make work after to retrieve a collection of objects
        :param iterable collection: the collection of objects
        :param QueryStringManager qs: a querystring manager to retrieve information from url
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_update_object(self, obj, data, view_kwargs):
        """Make checks or provide additional data before update object
        :param obj: an object from data layer
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def after_update_object(self, obj, data, view_kwargs):
        """Make work after update object
        :param obj: an object from data layer
        :param dict data: the data validated by marshmallow
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_delete_object(self, obj, view_kwargs):
        """Make checks before delete object
        :param obj: an object from data layer
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def after_delete_object(self, obj, view_kwargs):
        """Make work after delete object
        :param obj: an object from data layer
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_create_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work before to create a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

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
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_get_relationship(self, relationship_field, related_type_, related_id_field, view_kwargs):
        """Make work before to get information about a relationship
        :param str relationship_field: the model attribute used for relationship
        :param str related_type_: the related resource type
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return tuple: the object and related object(s)
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

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
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_update_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work before to update a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        :return boolean: True if relationship have changed else False
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

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
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def before_delete_relationship(self, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work before to delete a relationship
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError

    def after_delete_relationship(self, obj, updated, json_data, relationship_field, related_id_field, view_kwargs):
        """Make work after to delete a relationship
        :param obj: an object from data layer
        :param bool updated: True if object was updated else False
        :param dict json_data: the request params
        :param str relationship_field: the model attribute used for relationship
        :param str related_id_field: the identifier field of the related model
        :param dict view_kwargs: kwargs from the resource view
        """
        current_app.logger.info("%s, %s, %s", self, data, view_kwargs)
        raise NotImplementedError
