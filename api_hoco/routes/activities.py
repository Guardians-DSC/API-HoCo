from flask import Blueprint, request
from api_hoco.controllers.activity import register_activity, get_certificate
from api_hoco.models.db import mongo


activities_blueprints = Blueprint('activities', __name__, template_folder='templates')

@activities_blueprints.route('/activity', methods=['POST'])
def create_activity():
    ''' Route to register a new activity on the DB.'''
    result = register_activity(request)
    return result

@activities_blueprints.route('/file/<fileId>')
def retrieve_certificate(fileId):
    ''' Route to register a new activity on the DB.'''

    return mongo.send_file(fileId)
    return get_certificate(fileId)