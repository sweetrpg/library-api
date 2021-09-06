#!/bin/bash

set -x
set -e
set -o pipefail

pushd src

export $(cat configs/dev.env | xargs)

python3 appserver.py

popd
