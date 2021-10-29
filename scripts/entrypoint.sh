#!/bin/bash

set -x
set -e

printenv
#pwd
#ls -la
#ls -la /config

#newrelic-admin run-program gunicorn wsgi:app
#gunicorn wsgi:app
uwsgi --http :8281 --module wsgi:app --master --processes 4 --threads 2
#python appserver.py
#sleep 3600
