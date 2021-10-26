#!/bin/bash

set -e

scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

pushd ${scriptdir}/..

for d in app docs tests dev; do
    echo "Requirements: $d"
    pip-compile -r requirements/$d.in
done

popd
