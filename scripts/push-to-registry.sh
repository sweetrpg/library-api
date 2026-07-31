#!/bin/bash

set -e

export DOCKER_BUILDKIT=1
registry=registry.sweetrpg.com
name=sweetrpg-shelf-api

docker push \
    ${registry}/${name}
