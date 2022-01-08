from flask import Blueprint, jsonify, render_template, request
from datetime import datetime

api_blueprints = Blueprint('api', __name__, template_folder='templates')

@api_blueprints.route("/status", methods=['GET'])
def status():
    '''Returns the API status'''
    current_timestamp = datetime.now()

    status = {
        "status": "Operacional",
        "service": "API-HoCo",
        "timestamp": datetime.timestamp(current_timestamp),
        "date": current_timestamp,
    }
    return jsonify(status), 200

@api_blueprints.route("/doc", methods=['GET'])
def doc():
    '''Render the API documentation'''
    return render_template("index.html")

