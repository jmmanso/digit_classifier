"""
This file is loaded with the system's python binary by the wsgi daemon,
and below is when you switch to the virtual environment
"""

import sys
import os

### deprecated until we figure out how to get Apache to load env vars. For now, we will do dynamic text replacement with sed.
# fetch env variables
#VENV_DIR = os.getenv('PYVENV')
#API_LIB_DIR = os.getenv('MYAPP_REPO_DIR')
###

# activate virtual environment
activate_this = VENV_DIR+'/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

# append app dir so that python venv can access it
sys.path.append(API_LIB_DIR)


from views import app as application
