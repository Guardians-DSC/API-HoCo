from api_hoco.models.Activity import Activity
from api_hoco.util.errors import input_not_given


def register_activity(certificate, data):
    e_mail = data.get("e-mail")
    new_activity = Activity(certificate, **data)
    new_activity.save()
    result = Activity.get_all(e_mail)
    return result
   

def download_activity(id):
    filename, result = Activity.download(id)
    return filename, result


def get_all_activity(e_mail):
    result = Activity.get_all(e_mail)
    return result

    
def edit_activity(certificate, data):
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
    result = Activity.update(certificate, **data)
    result = Activity.get_all(data['e-mail'])
    return result


def get_user_data(email):
    result = Activity.get_user_data(email)
    return result
    

def del_user_activity(activity_id, email):
    result = Activity.remove(activity_id, email)
    if result:
        return get_all_activity(email)
    return None