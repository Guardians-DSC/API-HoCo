from flask import Blueprint, jsonify, render_template, request
from datetime import datetime
from api_hoco.controllers.organization import register_org

api_blueprints = Blueprint('api', __name__, template_folder='templates')

@api_blueprints.route("/status", methods=['GET'])
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

@api_blueprints.route("/doc", methods=['GET'])
def doc():
    return render_template("index.html")

@api_blueprints.route('/org', methods=['POST'])
def create_org():
    req = request.form

    name = req.get('name')
    github_url = req.get('github_url')

    image = request.files['image']
    result = register_org(name, github_url, image)
    return jsonify(result), 201




