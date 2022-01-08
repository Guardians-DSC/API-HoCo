from flask import Flask
from api_hoco.util.util import MyJsonify

def create_app():
    app = Flask(__name__)
    app.json_encoder = MyJsonify
    from .models.db import mongo
    mongo.init_app(app, uri='mongodb://bd-mongo:27017/hoco')

    from . import routes, controllers
    routes.init_app(app)

    return app

