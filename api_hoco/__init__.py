from flask import Flask
from flask_cors import CORS, cross_origin
from api_hoco.util.util import MyEncoder

def create_app():
    app = Flask(__name__)
    CORS(app, support_credentials=True)
    app.json_encoder = MyEncoder

    from . import routes, controllers
    routes.init_app(app)

    return app

