from flask import url_for
from api_hoco.connect2db import DB
from bson.objectid import ObjectId
from gridfs import GridFS
from ..util.constants import CATEGORIES, LIMIT_CREDITS

grid_fs = GridFS(DB)


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
        self.e_mail = kwargs.get('e-mail')

    def get_properties(self):
        '''
            Function that returns some properties of the Activity object
        '''
        return {
            'title': self.title,
            'category': self.category,
            'credits': self.credits,
            'time': self.time,
            'e-mail': self.e_mail
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
            DB.activity.insert_one(activity_properties)
            return activity_properties
        else:
            raise Exception

    @staticmethod
    def find_activity(id: str):
        '''
            Function to retrieve a activity using it's id
        '''
        activity = DB.activity.find_one({'_id': ObjectId(id)})

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
    def get_all(e_mail: str):
        activities = list(DB.activity.find({ 'e-mail': e_mail }))
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
    def update(certificate=None, **properties):
        '''
            Function that updates a specific activity registered. To do so, 
            the id of the activity is needed.

            Parameters:
            -> id - (str): The id of the activity that's going to be deleted;
            -> certificate - (File): Activity's certificate file that's going 
            to replace the old one;
            -> properties - (dict): Other properties that are going to be updated.
        '''
        _id = properties.get('_id')
        activity = Activity.find_activity(_id)

        if (certificate is not None):
            Activity.replace_certificate(_id, certificate)
        if (properties.get('title') is not None):
                activity['title'] = properties.get('title')
        if (properties.get('category') is not None):
                activity['category'] = properties.get('category')

        if (properties.get('time') is not None):
            activity['time'] = properties['time']
            activity['credits'] = None
        elif (properties.get('credits') is not None):
            activity['credits'] = properties['credits']
            activity['time'] = None

        DB.activity.update_one({'_id': ObjectId(_id)}, {
                                     '$set': activity})

        return Activity.find_activity(_id)

    @staticmethod
    def get_user_data(email: str):
        activities = Activity.get_all(email)
        data_dict = {}
        for category, value in CATEGORIES.items():
            data_dict[category] = {
                'category': category,
                'amount': 0,
                'max': value,
                'category_piece': 0,
            }

        hours = {}
        for activity in activities:
            if (activity['time'] is not None):
                if (hours.get(activity['category']) == None):
                    hours[activity['category']] = int(activity['time'])
                else:
                    hours[activity['category']] += int(activity['time'])


            if (activity['credits'] is not None and activity['category'] in CATEGORIES.keys()):

                if (data_dict[activity['category']]['amount'] + int(activity['credits']) > CATEGORIES[activity['category']]):
                    data_dict[activity['category']]['amount'] = CATEGORIES[activity['category']]
                else:
                    credits = int(activity['credits'])
                    data_dict[activity['category']]['amount'] = credits + \
                        data_dict[activity['category']]['amount']

        result = {
            'amount': sum([ data_dict[category]['amount'] for category in data_dict ]),
            'max': LIMIT_CREDITS,
            'categories': [],
            'hours': [{ 'category': category, 'time': hours[category] } for category in hours.keys()]
        }

        for category_data in data_dict.values():
            category_data['category_piece'] = float('{:.2f}'.format(category_data['amount'] / (result['amount'] + 0.01)))
            result['categories'].append(category_data)

        return result

    @staticmethod
    def remove(activity_id: str, email: str):
        activity = DB.activity.find_one({'_id': ObjectId(activity_id)})
        if activity and activity["e-mail"] == email:
            result = DB.activity.delete_one({"_id": ObjectId(activity_id)})
            return result.deleted_count
