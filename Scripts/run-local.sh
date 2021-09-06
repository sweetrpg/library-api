#!/bin/bash

set -x
set -e
set -o pipefail

export FLASK_APP=sweetrpg.library.api.application.main:create_app
export FLASK_ENV=development

pushd src

# $(pyenv which flask) init-db
$(pyenv which flask) run

popd
