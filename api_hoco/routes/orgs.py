from flask import Blueprint, request, jsonify, make_response
from api_hoco.controllers.organization import register_org, get_orgs, remove_org

from api_hoco.util.errors import input_not_given

orgs_blueprints = Blueprint('orgs', __name__, template_folder='templates')


@orgs_blueprints.route('/org', methods=['POST'])
def create_org():
    ''' Route to register a new organization on the DB.'''
    req_form = request.form

    org_image = request.files['image']

    name = req_form.get('name')
    org_url = req_form.get('org_url')

    if not (org_image and name and org_url):
        params_required = ['name (str)', 'org_url (str)', 'image (file)']

        return make_response(input_not_given(params_required), 400)

    try:
        new_org = register_org(name, org_url, org_image)
        return make_response(jsonify(new_org), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@orgs_blueprints.route('/orgs', methods=['GET'])
def list_orgs():
    ''' Route do list all the registered organization'''
    try:
        result = get_orgs()
        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@orgs_blueprints.route('/org', methods=['DELETE'])
def delete_org():
    ''' Route to delete a existing organization'''
    org_id = request.args.get('id')

    if not org_id: 
        params_required = ['id (str)']
        return make_response(input_not_given(params_required), 400)

    try:
        result = remove_org(org_id)
        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)
