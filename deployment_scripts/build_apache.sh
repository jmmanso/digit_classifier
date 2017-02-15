#!/bin/bash

# Copy configuration file into apache dir
sudo cp /var/www/$MYAPP/myapp.conf /etc/apache2/sites-available/

# Apache is sometimes weird and doesnt import env variables.
# Thus, we will dynamically write the value in the config file:
sudo sed -i "s/\$MYAPP/$MYAPP/g" /etc/apache2/sites-available/myapp.conf

# update permissions
sudo chown -R www-data /etc/apache2/sites-available/
sudo chmod -R 775 /etc/apache2/sites-available/

# Enable site
sudo a2ensite myapp.conf


# Disable default site
sudo a2dissite 000-default.conf


# Reload config
sudo service apache2 reload


# Restart server
sudo apachectl restart
