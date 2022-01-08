from flask import Flask, jsonify, make_response
from api_hoco.models.Organization import Organization
from api_hoco.util.errors import input_not_given


def register_org(request):
    req_form = request.form

    org_image = request.files['image']
    name = req_form.get('name')
    org_url = req_form.get('org_url')

    if not (org_image and name and org_url): 
        params_required = ['name (str)', 'org_url (str)', 'image (file)']

        return make_response(input_not_given(params_required), 400)

    try:
        new_org = Organization(name, org_url, org_image)
        resultado = new_org.save()
        
        return make_response(jsonify(resultado), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)
        


    



