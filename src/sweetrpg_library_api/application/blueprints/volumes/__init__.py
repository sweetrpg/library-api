# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <paul@schifferers.net>"
"""
"""

import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from flask import current_app
from flask_rest_jsonapi import Api, ResourceDetail, ResourceList, ResourceRelationship
from flask_rest_jsonapi.exceptions import ObjectNotFound
from marshmallow_jsonapi.flask import Schema, Relationship
from marshmallow_jsonapi import fields
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from sweetrpg_library_model.volume import Volume

blueprint = Blueprint("volumes", __name__, url_prefix="/volumes")


from .manager import VolumeList, VolumeDetail, VolumeRelationship

def setup_routes(app):
    app.logger.info("Setting up routes for Volumes API")
    api = Api(app)
    api.route(VolumeList, 'volume_list', '/volumes/')
    api.route(VolumeDetail, 'volume_detail', '/volumes/<id>')

# @blueprint.route("/", methods=['GET'])
# def get_single_volume():
#     """

#     :return:
#     """
#     return {}
