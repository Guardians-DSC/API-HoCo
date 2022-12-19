from flask import Flask, jsonify, make_response
from api_hoco.models.Activity import Activity
from api_hoco.util.errors import input_not_given

def register_activity(request):
    '''
        Controller function to register new activities by it's name, given url and image of it's logo.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
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
        filename, result = Activity.download(id)
        response = make_response(result)
        response.headers['Content-Type'] = 'application/octet-stream'
        response.headers["Content-Disposition"] = f"attachment; filename={filename}"
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def get_all_activity(request):
    e_mail = request.args.get('e-mail')
    if (e_mail is None):
        return make_response({'Error:': 'E-mail property not sended'}, 400)
    
    try:
        result = Activity.get_all(e_mail)
        response = jsonify({'activities': result})
        return response
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)
    
def edit_activity(request):
    '''
        Controller function to update a acitivity's properties. The properties that can be updated are:
        -> id - (str): Id of the activity that's going to be updated;
        -> credit - (int): Credits associated to the activity;
        -> time - (int): The hours associated to the activity;
        -> title - (str): Activity's title;
        -> category - (str): Activity's category;
        -> certificate - (File): Activity's certificate file;

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    req_form = request.form

    if ('id' not in req_form):
        return make_response(input_not_given(['id (str)']), 400)

    certificate = None
    if ('certificate' in request.files):
        certificate =  request.files['certificate']
    
    try:
        result = Activity.update(certificate, **req_form)
        
        return make_response(jsonify(result), 201)
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
    
