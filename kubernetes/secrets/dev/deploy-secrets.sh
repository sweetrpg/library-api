#!/bin/bash

set -e

ns=${1:-sweetrpg-library}

scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

pushd ${scriptdir}

#secretGenerator:
#  - name: sweetrpg-registry
#    type: kubernetes.io/dockerconfigjson
#    files:
#      - .dockerconfigjson
#  - name: sweetrpg-library-api-env
#    type: Opaque
#    envs:
#      - secrets.env
#  - name: sweetrpg-library-api-config-env
#    type: Opaque
#    files:
#      - newrelic.ini

echo "Docker registry config..."
kubectl create -n "${ns}" secret docker-registry sweetrpg-registry \
    --docker-server=registry.sweetrpg.com \
    --docker-username=docker \
    --docker-password=ESU7PnNtlt07zkvbnSyByrTdzllajxIQWqY7mswQR78
#kubectl create -n "${ns}" secret dockerconfigjson sweetrpg-registry \
#    --from-file=.dockerconfigjson

echo "NewRelic config..."
kubectl create -n "${ns}" secret generic sweetrpg-library-api-config-env \
    --from-file=newrelic.ini

echo "Other secrets..."
kubectl create -n "${ns}" secret generic sweetrpg-library-api-env \
    --from-env-file=secrets.env
kubectl create -n "${ns}" secret generic sweetrpg-library-api \
    --from-env-file=../common.env

popd
