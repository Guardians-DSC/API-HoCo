import json
from bson.json_util import ObjectId

class MyJsonify(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj) 

