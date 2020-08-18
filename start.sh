#!/bin/bash


export FLASK_APP=wsgi.py
export FLASK_ENV=production
export APP_CONFIG_FILE=config.py

flask run
