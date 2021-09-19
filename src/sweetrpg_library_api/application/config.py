# -*- coding: utf-8 -*-
__author__ = "Paul Schifferer <dm@sweetrpg.com>"
"""
config.py
- settings for the flask application object
"""


import os
import redis
import random
import hashlib


class BaseConfig(object):
    DEBUG = bool(os.environ.get('DEBUG') or True)
    PORT = os.environ.get('PORT') or 5000
    # ASSETS_DEBUG = True
    DB_HOST = os.environ["DB_HOST"]
    DB_PORT = os.environ["DB_PORT"] or "25017"
    DB_USER = os.environ["DB_USER"]
    DB_PW = os.environ["DB_PW"]
    DB_NAME = os.environ["DB_NAME"]
    DB_OPTS = os.environ["DB_OPTS"]
    DB_URL = f'mongodb+srv://{DB_USER}:{DB_PW}@{DB_HOST}/{DB_NAME}?{DB_OPTS}'
    MONGO_URI = DB_URL
    # used for encryption and session management
    # SECRET_KEY = os.environ.get('SECRET_KEY') or hashlib.sha256(f"{random.random()}".encode('utf-8')).hexdigest()
    # CSRF_TOKEN = os.environ.get('CSRF_TOKEN') or hashlib.sha256(f"{random.random()}".encode('utf-8')).hexdigest()
    CACHE_REDIS_HOST = os.environ['REDIS_HOST']
    CACHE_REDIS_PORT = int(os.environ.get('REDIS_PORT') or 6379)
    # CACHE_REDIS_DB = int(os.environ.get('REDIS_DB') or 7)
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url(f"redis://{os.environ['REDIS_HOST']}:{int(os.environ.get('REDIS_PORT') or 6379)}")
