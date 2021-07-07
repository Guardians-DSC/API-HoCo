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


@app.route("/cadastrar", methods=['POST'])
def cadastrar():
    '''Retorna um json construído a partir do valor do json enviado na request pelo usuário'''
    content = request.get_json() #captura o json enviado na request
    nome = content["nome"] #pega o valor do campo 'nome' do json

    response = {
        "nome": nome
    }

    return jsonify(response), 200
