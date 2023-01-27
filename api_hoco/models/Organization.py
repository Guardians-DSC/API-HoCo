from flask import url_for
from api_hoco.connect2db import DB
from bson.objectid import ObjectId
from api_hoco.util.util import encode_image

class Organization:
    def __init__(self, name, access_url, image):
        '''
            Initialization of an Object of the type Organzation.

            Parameters:
            -> name - (str): Name of the organization.
            -> access_url - (str): URL of the org, like a site or a social media link.
            -> image - (bytes): Image file of the organization logo.
        '''
        self.name = name
        self.access_url = access_url
        self.image = encode_image(image)

    def get_properties(self):
        '''
            Function that returns some properties of the Organization object
        '''
        
        return { 
            'name': self.name,
            'org_url': self.access_url,
            'image': f'data:image/jpeg;base64,{self.image}',
        }

    def save(self):
        '''
            Function that saves the Organization on the database used. If the organization already exists on the
            database (if the name is already registered) the db register is just updated.
        '''
        org_properties = self.get_properties()

        org = DB.organization.find_one({ 'name': self.name })

        if (org):
            DB.organization.update_one({ 'name': self.name }, { '$set': org_properties }) 

        else:
            DB.organization.insert_one(org_properties) 

        
        return DB.organization.find_one({ 'name': self.name })

    @staticmethod
    def find_orgs():
        '''
            Function to retrieve all the organization registered in the database.
        '''
        result = DB.organization.find()

        return [ org for org in result ]

    @staticmethod
    def delete_org(org_id):
        '''
            Function to delete a specific organization registered. To do so, the id of the organization is needed.

            Parameters:
            -> org_id - (str): The id of the organization that's going to be deleted.
        '''
        DB.organization.delete_one({ '_id': ObjectId(org_id) })


