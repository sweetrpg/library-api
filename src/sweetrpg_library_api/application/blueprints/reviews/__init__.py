# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
"""

import functools
from flask_rest_jsonapi import Api
from .manager import ReviewList, ReviewDetail, ReviewAuthorRelationship


def setup_routes(app):
    # app.logger.info("Registering review models...")
    # for model_name, model_info in review_model_info.items():
    #     APIData.add_model(model_name, model_info)

    app.logger.info("Setting up routes for Reviews API")
    api = Api(app)
    api.route(ReviewList, "review_list", "/reviews/")
    api.route(ReviewDetail, "review_detail", "/reviews/<id>")
    api.route(ReviewAuthorRelationship, "review_authors", "/reviews/<id>/relationships/authors")
