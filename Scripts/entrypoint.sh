#!/bin/bash

set -x
set -e

printenv
pwd
ls -la

newrelic-admin run-program gunicorn wsgi:app
