#!usr/bin/python3

from flask import Blueprint
from os.path import dirname, basename, isfile
import glob


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

modules = glob.glob(dirname(__file__) + "/*.py")

for module in [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]:
    exec(f"from. {module} import *")
