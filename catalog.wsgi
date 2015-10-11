import sys
import os

applicationPath = '/var/www/catalog/appcode'
if applicationPath not in sys.path:
    sys.path.insert(0, applicationPath)

os.chdir(applicationPath)

from application import app as application
