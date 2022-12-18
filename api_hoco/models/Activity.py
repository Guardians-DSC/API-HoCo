from flask import url_for
from .db import mongo
from bson.objectid import ObjectId
from gridfs import GridFS
import json

grid_fs = GridFS(mongo.db)


class Activity:
    def __init__(self, certificate=None, **kwargs):
        '''
            Initialization of an Object of the type Activity.

            Parameters:
            -> certificate - (bytes): Certificate file;
            -> title - (str): Title of the activity;
            -> category - (str): Activity category;
            -> time - (str): Time in hours that this activity took;
            -> credits - (str): Time in credits that this activity took;
        '''
        self.certificate = certificate
        self.title = kwargs.get('title')
        self.category = kwargs.get('category')
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

        with grid_fs.new_file(filename=self.certificate.filename) as fp:
            fp.write(self.certificate)
            file_id = fp._id
        if grid_fs.find_one(file_id) is not None:
            activity_properties["_id"] = file_id
            mongo.db.activity.insert_one(activity_properties)
            return activity_properties
        else:
            raise Exception

    @staticmethod
    def find_activity(id: str):
        '''
            Function to retrieve a activity using it's id
        '''
        activity = mongo.db.activity.find_one({'_id': ObjectId(id)})

        if activity:
            return activity
        return Exception

    @staticmethod
    def download(id):
        grid_fs_file = grid_fs.find_one({'_id': ObjectId(id)})

        if grid_fs_file:
            return grid_fs_file.filename, grid_fs_file.read()
        else:
            raise Exception

    @staticmethod
    def get_all():
        activities = list(mongo.db.activity.find({}))
        result = list()
        for activity in activities:
            activity["certificate"] = f"activity/download/{activity.get('_id')}"
            result.append(activity)
        return result


    @staticmethod
    def replace_certificate(id, new_certificate):
        file = grid_fs.find_one({'_id': ObjectId(id)})
        if (file is not None):
            grid_fs.delete(file._id)
            with grid_fs.new_file(filename=file.filename, _id=ObjectId(id)) as fp:
                fp.write(new_certificate)

        else:
            raise Exception

    @staticmethod
    def update(id: str, certificate=None, **properties):
        '''
            Function that updates a specific activity registered. To do so, 
            the id of the activity is needed.

            Parameters:
            -> id - (str): The id of the activity that's going to be deleted;
            -> certificate - (File): Activity's certificate file that's going 
            to replace the old one;
            -> properties - (dict): Other properties that are going to be updated.
        '''
        activity = Activity.find_activity(id)

        if (certificate is not None):
            Activity.replace_certificate(id, certificate)

        if (properties.get('time') is not None):
            activity['time'] = properties['time']
            activity['credits'] = None
        elif (properties.get('credits') is not None):
            activity['credits'] = properties['credits']
            activity['time'] = None

        mongo.db.activity.update_one({'_id': ObjectId(id)}, {
                                     '$set': activity})

        return Activity.find_activity(id)
