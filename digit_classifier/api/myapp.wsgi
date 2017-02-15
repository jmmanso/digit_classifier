"""
This file is loaded with the system's python binary by the wsgi daemon,
and below is when you switch to the virtual environment
"""

import sys
import os

# The install script will dynamically write in
# environment variables here
activate_this = VENV_DIR+'/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# append app dir so that python venv can access it
sys.path.append(API_LIB_DIR)



from views import app as application
