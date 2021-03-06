from flask import url_for
from .db import mongo
from bson.objectid import ObjectId

class Activity:
    def __init__(self, certificate, title, category, **kwargs):
        '''
            Initialization of an Object of the type Organzation.

            Parameters:
            -> certificate - (bytes): Certificate file.
            -> name - (str): Name of the organization.
            -> access_url - (str): URL of the org, like a site or a social media link.
        '''
        self.certificate = certificate
        self.title = title
        self.category = category
        self.credits = kwargs.get('credits')
        self.time = kwargs.get('time')

    def get_properties(self):
        '''
            Function that returns some properties of the Activity object
        '''
        return { 
            'title': self.title,
            'category': self.category,
            'credits': self.credits,
            'time': self.time,
        }

    def save(self):
        '''
            Function that saves the Activity on the database used.
        '''
        activity_properties = self.get_properties()
        mongo.save_file(f'{self.title}-certificate', self.certificate)

        result = mongo.db.activity.insert_one(activity_properties) 
        return { 'id': result.inserted_id, **activity_properties }

    @staticmethod
    def find_orgs():
        '''
            Function to retrieve all the organization registered in the database.
        '''
        result = mongo.db.organization.find()

        return [ org for org in result ]

    @staticmethod
    def delete_org(org_id):
        '''
            Function to delete a specific organization registered. To do so, the id of the organization is needed.

            Parameters:
            -> org_id - (str): The id of the organization that's going to be deleted.
        '''
        mongo.db.organization.delete_one({ '_id': ObjectId(org_id) })


