from flask import Blueprint, request
from api_hoco.controllers.activity import register_activity

activities_blueprints = Blueprint('activities', __name__, template_folder='templates')

@activities_blueprints.route('/activity', methods=['POST'])
def create_activity():
    ''' Route to register a new activity on the DB.'''
    result = register_activity(request)
    return result
