from .db import mongo

def init_app(app):
    mongo.init_app(app)
