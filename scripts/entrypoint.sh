#!/bin/bash

set -x
set -e

printenv
pwd
ls -la
ls -la /config

newrelic-admin run-program gunicorn --log-level debug -w 1 wsgi:app
