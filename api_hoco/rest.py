from flask import Flask
from api_hoco.routes.api import api

app = Flask(__name__)

app.register_blueprint(api)
