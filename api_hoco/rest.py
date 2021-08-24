from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route("/status", methods=['GET'])
def status():
    '''Retorna um simples json com status 200'''
    status = {
        "status": "operacional",
        "service": "api-flask-example",
    }
    return jsonify(status), 200
