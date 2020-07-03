#!/bin/bash


export FLASK_APP=beca.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py

open http://127.0.0.1:5000/
flask run
