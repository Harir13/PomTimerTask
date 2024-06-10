import sys
import os

# Add your project directory to the sys.path
project_home = '/home/hariharan83/PomTimerTask'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set up the Flask application object
from app import app as application

# Configure the WSGI server to use the Flask application object
from flask_wsgi import WSGIApplication
application = WSGIApplication(application)
