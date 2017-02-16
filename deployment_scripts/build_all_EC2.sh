#!/bin/bash

# get the config env variables
source config_profile.sh

#Setup the python virtual environment
bash install_pyvenv.sh

# Train mymodel
bash train_model.sh

# Permissions and symlinks
bash set_permissions.sh

# Spin up Apache server
bash build_apache.sh
