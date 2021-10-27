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

echo "Deleting old secrets..."
kubectl delete -n "${ns}" secret sweetrpg-registry api-newrelic api-db api-cache api-auth api-misc api-common || true

echo "Docker registry config..."
kubectl create -n "${ns}" secret docker-registry sweetrpg-registry \
    --docker-server=registry.sweetrpg.com \
    --docker-username=docker \
    --docker-password=ESU7PnNtlt07zkvbnSyByrTdzllajxIQWqY7mswQR78
#kubectl create -n "${ns}" secret dockerconfigjson sweetrpg-registry \
#    --from-file=.dockerconfigjson

echo "NewRelic config..."
kubectl create -n "${ns}" secret generic api-newrelic \
    --from-file=newrelic.ini

echo "Other secrets..."
kubectl create -n "${ns}" secret generic api-db \
    --from-env-file=db.env
kubectl create -n "${ns}" secret generic api-cache \
    --from-env-file=cache.env
kubectl create -n "${ns}" secret generic api-auth \
    --from-env-file=auth.env
kubectl create -n "${ns}" secret generic api-misc \
    --from-env-file=misc.env
#kubectl create -n "${ns}" secret generic api-stripe \
#    --from-env-file=stripe.env
kubectl create -n "${ns}" secret generic api-common \
    --from-env-file=../common.env

popd
