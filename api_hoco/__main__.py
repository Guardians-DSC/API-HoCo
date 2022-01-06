from flask import Flask
from api_hoco.routes.api import api

app = Flask(__name__, template_folder='templates')

app.register_blueprint(api)

app.run(host="0.0.0.0", port=8000, debug=True)
