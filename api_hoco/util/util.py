import json
import base64 
from bson.json_util import ObjectId

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super(MyEncoder, self).default(obj) 

def encode_image(image):
    '''
        Function transforms image on a string that can be stored and sent to frontend to be rendered.

        Parameters:
        -> image - (bytes): Image file that's going to be parsed.
    '''
    image_bytes = base64.b64encode(image.read())
    string_image = image_bytes.decode('utf-8')
    return string_image