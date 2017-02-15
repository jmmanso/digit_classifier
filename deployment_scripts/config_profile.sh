#!/bin/bash

# API name
export MYAPP="digits-api"

# path and name of python virtual environment
export PYVENV="/opt/digitsvenv"

# Directory where API code reside.
# Do not place it in $HOME, for some reason
# Apache does not like that
export MYAPP_REPO_DIR="/usr/src/digits_classifier/digits_classifier"

export MYAPP_API_DIR="$MYAPP_REPO_DIR/api"
