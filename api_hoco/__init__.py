from flask import Flask

def create_app():
    app = Flask(__name__)
    from .models.db import mongo
    mongo.init_app(app, uri='mongodb://bd-mongo:27017/hoco')

    from . import routes, controllers
    routes.init_app(app)

    return app

