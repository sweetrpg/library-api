#!/bin/bash

set -x
set -e

printenv
#pwd
#ls -la
#ls -la /config

#newrelic-admin run-program gunicorn wsgi:app
#gunicorn wsgi:app
python appserver.py
