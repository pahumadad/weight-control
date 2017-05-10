#!/bin/bash

source env/bin/activate
export FLASK_APP=$(pwd)/wcontrol/src/api.py
export WCONTROL_CONF=wcontrol.conf.config

python -m flask run --host=0.0.0.0 --debugger
