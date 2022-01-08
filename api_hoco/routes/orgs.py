from flask import Blueprint, request
from api_hoco.controllers.organization import register_org, get_orgs, remove_org

orgs_blueprints = Blueprint('orgs', __name__, template_folder='templates')

@orgs_blueprints.route('/org', methods=['POST'])
def create_org():
    ''' Route to register a new organization on the DB.'''
    result = register_org(request)
    return result

@orgs_blueprints.route('/orgs', methods=['GET'])
def list_orgs():
    ''' Route do list all the registered organization'''
    return get_orgs() 

@orgs_blueprints.route('/org', methods=['DELETE'])
def delete_org():
    ''' Route to delete a existing organization'''
    return remove_org(request) 


