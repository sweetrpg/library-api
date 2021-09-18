#!/bin/bash

set -x
set -e
set -o pipefail

pushd src

export $(cat configs/dev.env | xargs)

NEW_RELIC_CONFIG_FILE=../newrelic.ini newrelic-admin run-python appserver.py

popd
