#!/bin/bash

# Setup the python virtual environment.
# Conda messes up external virtualenvs, thus,
# if conda is installed, should be used to install
# virtualenv.

if hash conda; then
      sudo conda install virtualenv
   else
      sudo easy_install virtualenv
fi


sudo rm -rf $PYVENV

sudo -E virtualenv $PYVENV


# Install packages

sudo -E $PYVENV/bin/pip install --upgrade pip

sudo -E $PYVENV/bin/pip install -r $MYAPP_REPO_DIR/deployment_scripts/requirements.txt
