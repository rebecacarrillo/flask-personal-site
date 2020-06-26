#!/bin/bash


export FLASK_APP=beca.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py

flask run
