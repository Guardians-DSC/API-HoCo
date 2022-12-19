from flask import Flask, jsonify, make_response
from api_hoco.models.Activity import Activity
from api_hoco.util.errors import input_not_given

def register_activity(request):
    '''
        Controller function to register new organizations by it's name, given url and image of it's logo.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    req_form = request.form

    credit = req_form.get('credits')
    time = req_form.get('time')

    if (time and credit) or (not time and not credit):
        exclusive_params = 'You can\'t give credit and time parameters, You\'ll need to choose one over another'
        return make_response(exclusive_params, 400)

    title = req_form.get('title')
    category = req_form.get('category')
    certificate = request.files['certificate']
    
    if not (title and category and certificate): 
        params_required = ['title (str)', 'category (str)', 'certificate (file)']

        return make_response(input_not_given(params_required), 400)

    try:
        new_activity = Activity(certificate, **req_form)
        result = new_activity.save()
        
        return make_response(jsonify(result), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def download_activity(id):
    try:
        result = Activity.download(id)
        response = make_response(result)
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers["Content-Disposition"] = f"attachment; filename={id}"
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def get_all_activity():
    try:
        result = Activity.get_all()
        response = jsonify({'activities': result})
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def get_user_data(request):
    email = request.args.get('e-mail')

    try:
        result = Activity.get_user_data(email)
        response = jsonify(result)
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)
    