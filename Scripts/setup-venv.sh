#!/bin/bash

set -x
set -e
set -o pipefail

pyenv install -s
$(pyenv which python) -m pip install pip-tools
$(pyenv which pip-compile) requirements/dev.in
$(pyenv which pip-sync) requirements/dev.txt
# $(pyenv which python) -m pip install pipenv
# $(pyenv which pipenv) install
