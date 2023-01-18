from flask import Blueprint, request, jsonify, make_response
from api_hoco.controllers.questions import register_question, get_questions, remove_question

from api_hoco.util.errors import input_not_given

questions_blueprints = Blueprint('questions', __name__, template_folder='templates')


@questions_blueprints.route('/question', methods=['POST'])
def create_question():
    ''' Route to register a new question on the DB.'''
    req_body = request.get_json()

    question = req_body['question']
    answer = req_body['answer']

    if not (question and answer): 
        params_required = ['question (str)', 'answer (str)']

        return make_response(input_not_given(params_required), 400)

    try:
        result = register_question(question, answer)
        return make_response(jsonify(result), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@questions_blueprints.route('/questions', methods=['GET'])
def list_questions():
    ''' Route do list all the registered questions'''
    try:
        result = get_questions()
        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


@questions_blueprints.route('/question', methods=['DELETE'])
def delete_question():
    ''' Route to delete a existing question'''
    name = request.args.get('id')

    if not name: 
        params_required = ['id (str)']
        return make_response(input_not_given(params_required), 400)

    try:
        result = remove_question(name)
        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)
