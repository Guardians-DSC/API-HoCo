from api_hoco.models.Organization import Organization


def register_org(name, org_url, org_image):
    '''
        Controller function to register new organizations by it's name, given url and image of it's logo.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    new_org = Organization(name, org_url, org_image)
    result = new_org.save()
    return result


def get_orgs():
    '''
        Controller function to retrieve all the organizations registered on the database
    '''
    result = Organization.find_orgs()
    return result


def remove_org(org_id):
    '''
        Controller function to delete a specific organization. The user needed to pass the name of the 
        organization that's going to be deleted.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    Organization.delete_org(org_id)
    result = Organization.find_orgs()
    return result


