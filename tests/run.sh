#!/bin/bash

virtualenv -p python3 tests/venv
source tests/venv/bin/activate
pip install -r tests/requirements.txt
python -m unittest tests.tests_deploy
