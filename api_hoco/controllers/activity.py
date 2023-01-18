from flask import Flask, jsonify, make_response

from api_hoco.models.Activity import Activity
from api_hoco.util.errors import input_not_given


def register_activity(certificate, data):
    try:
        e_mail = data.get("e-mail")
        new_activity = Activity(certificate, **data)
        new_activity.save()
        result = Activity.get_all(e_mail)
        return result
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


def download_activity(id):
    filename, result = Activity.download(id)
    return filename, result


def get_all_activity(e_mail):
    result = Activity.get_all(e_mail)
    return result

    
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
    req_form: dict = request.form

    if ('_id' not in req_form):
        return make_response(input_not_given(['_id (str)']), 400)

    certificate = None
    if ('certificate' in request.files):
        certificate =  request.files['certificate']


    if ('certificate' in req_form):
        req_form.pop('certificate')

    try:
        result = Activity.update(certificate, **req_form)
        result = Activity.get_all(req_form['e-mail'])
        return make_response(jsonify(result), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


def get_user_data(email):
    result = Activity.get_user_data(email)
    return result
    

def del_user_activity(activity_id, email):
    result = Activity.remove(activity_id, email)
    if result:
        return get_all_activity(email)
    return None