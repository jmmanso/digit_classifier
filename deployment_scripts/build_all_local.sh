#!/bin/bash

# get the config env variables
source config_profile.sh

#Setup the python virtual environment
bash install_pyvenv.sh

# Train mymodel
bash train_mymodel.sh

# Spin up Flask server on localhost
