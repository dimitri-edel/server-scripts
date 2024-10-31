#!/bin/bash
virtualenv venv
. ./venv/bin/activate
pip install -r /opt/scripts/requirements.txt
deactivate