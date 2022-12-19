from flask import url_for
from .db import mongo
from bson.objectid import ObjectId
from gridfs import GridFS
from ..util.constants import CATEGORIES, LIMIT_CREDITS

grid_fs = GridFS(mongo.db)


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

        with grid_fs.new_file(filename=f'{self.title}-certificate') as fp:
            fp.write(self.certificate)
            file_id = fp._id
        if grid_fs.find_one(file_id) is not None:
            activity_properties["_id"] = file_id
            result = mongo.db.activity.insert_one(activity_properties)
            return {'id': result.inserted_id, **activity_properties}
        else:
            raise Exception

    @staticmethod
    def download(id):
        grid_fs_file = grid_fs.find_one({'_id': ObjectId(id)})
        if grid_fs_file:
            return grid_fs_file.read()
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
    def delete_org(org_id):
        '''
            Function to delete a specific organization registered. To do so, the id of the organization is needed.

            Parameters:
            -> org_id - (str): The id of the organization that's going to be deleted.
        '''
        mongo.db.organization.delete_one({'_id': ObjectId(org_id)})

    @staticmethod
    def get_user_data(email: str):
        activities = Activity.get_all()  # TO-DO: Add email as parameter
        amount = 0
        data_dict = {}
        for category, value in CATEGORIES.items():
            data_dict[category] = {
                'category': category,
                'amount': 0,
                'max': value,
                'category_piece': 0,
            }

        for activity in activities:
            if (activity['credits'] is not None and activity['category'] in CATEGORIES.keys()):
                credits = int(activity['credits'])
                amount += credits
                data_dict[activity['category']]['amount'] = credits + \
                    data_dict[activity['category']]['amount']

        result = {
            'amount': amount,
            'max': LIMIT_CREDITS,
            'categories': []
        }

        for category_data in data_dict.values():
            category_data['category_piece'] = '{:.2f}'.format(category_data['amount'] / (amount + 0.01))
            result['categories'].append(category_data)

        return result
