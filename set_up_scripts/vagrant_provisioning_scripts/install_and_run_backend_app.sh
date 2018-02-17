#!/usr/bin/env bash

# Purpose is to install the main project package, export certain variables
# and run it.

. venv/bin/activate
cd /vagrant
pip install --editable .
export FLASK_APP=fyp_web_ml_project
flask run --host=0.0.0.0
