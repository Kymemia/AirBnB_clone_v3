#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify

@app_views('/status', methods=['GET'])
def get_status:
    """returns a status OK"""
    return jsonify({"status": "OK"})
