from flask import Blueprint, request
from api_hoco.controllers.organization import register_org

orgs_blueprints = Blueprint('orgs', __name__, template_folder='templates')

@orgs_blueprints.route('/org', methods=['POST'])
def create_org():
    ''' Route to register a new organization on the DB.'''
    result = register_org(request)
    return result




