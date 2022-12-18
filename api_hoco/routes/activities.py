from flask import Blueprint, request
from api_hoco.controllers.activity import register_activity, download_activity, get_all_activity, edit_activity

activities_blueprints = Blueprint('activities', __name__, template_folder='templates')

@activities_blueprints.route('/activity', methods=['POST'])
def create_activity():
    ''' Route to register a new activity on the DB.'''
    result = register_activity(request)
    return result

@activities_blueprints.route('/activity/download/<id>', methods=['GET'])
def get_activity(id):
    result = download_activity(id)
    return result

@activities_blueprints.route('/activities', methods=['GET'])
def get_activities():
    result = get_all_activity()
    return result

@activities_blueprints.route('/activity', methods=['PATCH'])
def update_activity():
    result = edit_activity(request)
    return result
