from flask import Blueprint
from flask import jsonify
from datetime import datetime

api = Blueprint('api', __name__, template_folder='templates')

@api.route("/status", methods=['GET'])
def status():
    '''Retorna um simples json com status 200'''
    current_timestamp = datetime.now()

    status = {
        "status": "Operacional",
        "service": "API-HoCo",
        "timestamp": datetime.timestamp(current_timestamp),
        "date": current_timestamp,
    }
    return jsonify(status), 200

