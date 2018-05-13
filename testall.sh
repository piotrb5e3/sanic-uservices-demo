#!/usr/bin/env bash
set -e

# Test products-service
pushd cart-service
. .venv/bin/activate
pip install -r requirements.txt
pytest
deactivate
popd

# Test cart-service
pushd cart-service
. .venv/bin/activate
pip install -r requirements.txt
pytest
deactivate
popd

