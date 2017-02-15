#!/bin/bash


# Delete directories and symlinks

sudo rm /var/www/$MYAPP
sudo rm -rf $MYAPP_REPO_DIR
sudo rm -rf $PYVENV
