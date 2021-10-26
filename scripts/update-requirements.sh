#!/bin/bash

set -e

scriptdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"

pushd ${scriptdir}/..

for r in app docs tests dev; do
    echo "Requirements: $r"
    pip-compile -r requirements/$r.in
done

popd
