from flask import url_for
from .db import mongo

class Organization:
    def __init__(self, name, access_url, image):
        '''
            Initialization of an Object of the type Organzation.

            Parameters:
            -> name - (str): Name of the organization.
            -> access_url - (str): URL of the org, like a site or a social media link.
            -> image - (file): Image file of the organization logo.
        '''
        self.name = name
        self.access_url = access_url
        self.image = image

    def get_properties(self):
        '''
            Function that returns some properties of the Organization object
        '''

        return { 
            'name': self.name,
            'org_url': self.access_url,
            'image_id': f'{self.name}-logo',
            'image_url': url_for('api.get_file', filename=f'{self.name}-logo')
        }

    def save(self):
        '''
            Function that saves the Organization on the database used. If the organization already exists on the
            database (if the name is already registered) the db register is just updated.
        '''
        org_image = f'{self.name}-logo'

        mongo.save_file(org_image, self.image)
        
        org_properties = self.get_properties()

        org = mongo.db.organization.find_one({ 'name': self.name })

        if (org):
            mongo.db.organization.update_one({ 'name': self.name }, { '$set': org_properties }) 

        else:
            mongo.db.organization.insert_one(org_properties) 

        
        return mongo.db.organization.find_one({ 'name': self.name })

    @staticmethod
    def find_orgs():
        '''
            Function to retrieve all the organization registered in the database.
        '''
        result = mongo.db.organization.find()

        return [ { **org, 'image_url': url_for('api.get_file', filename=org['image_id']) } for org in result ]

    @staticmethod
    def delete_org(name):
        '''
            Function to delete a specific organization registered. To do so, the name of the organization is needed.

            Parameters:
            -> name - (str): The name of the organization that's going to be deleted.
        '''
        mongo.db.organization.delete_one({ 'name': name })

