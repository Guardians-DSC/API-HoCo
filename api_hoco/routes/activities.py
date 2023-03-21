from flask import Blueprint, request, jsonify, make_response

from api_hoco.controllers.activity import register_activity, download_activity, get_user_data, get_all_activity, edit_activity, get_all_activity, del_user_activity
from api_hoco.util.errors import input_not_given

activities_blueprints = Blueprint(
    'activities', __name__, template_folder='templates')


@activities_blueprints.route('/activity', methods=['POST'])
def create_activity():
    ''' Route to register a new activity on the DB.'''
    req_form = request.form
    e_mail = req_form.get('e-mail')

    if (not e_mail):
        params_required = ['e-mail (str)']
        return make_response(input_not_given(params_required), 400)

    credit = req_form.get('credits')
    time = req_form.get('time')

    if (time and credit) or (not time and not credit):
        exclusive_params = 'You can\'t give credit and time parameters, You\'ll need to choose one over another'
        return make_response(exclusive_params, 400)

    title = req_form.get('title')
    category = req_form.get('category')
    certificate = request.files['file']
    
    if not (title or category or certificate): 
        params_required = ['title (str)', 'category (str)', 'certificate (file)']
        return make_response(input_not_given(params_required), 400)

    data = request.form.to_dict()
    try:
        result = register_activity(certificate, data)
        return make_response(jsonify(result), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@activities_blueprints.route('/activity/download/<id>', methods=['GET'])
def get_activity(id):
    try:
        filename, result = download_activity(id)
        response = make_response(result)
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@activities_blueprints.route('/activities', methods=['GET'])
def get_activities():
    e_mail = request.args.get('e-mail')
    if (e_mail is None):
        return make_response({'Error:': 'E-mail property not sended'}, 400)
    
    try:
        result = get_all_activity(e_mail)
        response = jsonify({'activities': result})
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@activities_blueprints.route('/activity', methods=['PATCH'])
def update_activity():
    req_form: dict = request.form

    if ('_id' not in req_form):
        return make_response(input_not_given(['_id (str)']), 400)

    certificate = None
    if ('certificate' in request.files):
        certificate =  request.files['certificate']

    if ('certificate' in req_form):
        req_form.pop('certificate')

    try:
        result = edit_activity(certificate, req_form)
        return jsonify(result), 201
    except Exception as e:
        return make_response({'Error': str(e)}, 500)


@activities_blueprints.route('/user_data', methods=['GET'])
def user_data():
    email = request.args.get('email')
    if (email is None):
        return make_response({'Error:': 'E-mail property not sended'}, 400)

    try:
        result = get_user_data(email)
        response = jsonify(result)
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@activities_blueprints.route('/activity/<activity_id>', methods=['DELETE'])
def remove_user_activity(activity_id):
    email = request.args.get('e-mail')
    if not email:
            return make_response({'Error': "e-mail was not informed"}, 400)
    
    try:
        result = del_user_activity(activity_id, email)
        if result == None:
            return make_response({'Error': "activity was not deleted"}, 400)
        response = jsonify(result), 200
        return response
    except Exception as e:
        return make_response({'Error': str(e)}, 500)
