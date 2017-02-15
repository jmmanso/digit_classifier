#!/bin/bash

#Setup the python virtual environment

sudo easy_install virtualenv

sudo rm -rf $PYVENV

sudo -E virtualenv $PYVENV


# Install packages

sudo -E $PYVENV/bin/pip install --upgrade pip

sudo -E $PYVENV/bin/pip install -r requirements.txt
