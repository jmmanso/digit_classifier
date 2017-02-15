#!/bin/bash

#Set symlink to API lib folder:
sudo rm -rf /var/www/$MYAPP
sudo ln -sT $MYAPP_API_DIR /var/www/$MYAPP

# Dynamically write environment variables into the code.
sudo sed -i "s#VENV_DIR#\"$PYVENV\"#g" /var/www/$MYAPP/myapp.wsgi
sudo sed -i "s#API_LIB_DIR#\"$MYAPP_API_DIR\"#g" /var/www/$MYAPP/myapp.wsgi



# Give ownership to Apache of symlink and target dir
sudo chown -R www-data /var/www/$MYAPP
sudo chown -R www-data $MYAPP_REPO_DIR

# Let Apache use python venv
sudo chgrp -R www-data $PYVENV
sudo chmod -R 775 $PYVENV
