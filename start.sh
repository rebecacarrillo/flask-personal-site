#!/bin/bash


export FLASK_APP=wsgi.py
export FLASK_DEBUG=True

flask run
