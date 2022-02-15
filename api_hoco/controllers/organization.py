from flask import Flask, jsonify, make_response
from api_hoco.models.Organization import Organization
from api_hoco.util.errors import input_not_given


def register_org(request):
    '''
        Controller function to register new organizations by it's name, given url and image of it's logo.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    req_form = request.form

    org_image = request.files['image']
    name = req_form.get('name')
    org_url = req_form.get('org_url')

    if not (org_image and name and org_url): 
        params_required = ['name (str)', 'org_url (str)', 'image (file)']

        return make_response(input_not_given(params_required), 400)

    try:
        new_org = Organization(name, org_url, org_image)
        result = new_org.save()
        
        return make_response(jsonify(result), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def get_orgs():
    '''
        Controller function to retrieve all the organizations registered on the database
    '''
    try:
        result = Organization.find_orgs()


        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def remove_org(req):
    '''
        Controller function to delete a specific organization. The user needed to pass the name of the 
        organization that's going to be deleted.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    org_id = req.args.get('id')

    if not org_id: 
        params_required = ['id (str)']

        return make_response(input_not_given(params_required), 400)

    try:
        Organization.delete_org(org_id)
        result = Organization.find_orgs()

        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


