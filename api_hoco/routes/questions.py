from flask import Blueprint, request
from api_hoco.controllers.questions import register_question, get_questions, remove_question

questions_blueprints = Blueprint('questions', __name__, template_folder='templates')

@questions_blueprints.route('/question', methods=['POST'])
def create_question():
    ''' Route to register a new question on the DB.'''
    result = register_question(request)
    return result

@questions_blueprints.route('/questions', methods=['GET'])
def list_questions():
    ''' Route do list all the registered questions'''
    return get_questions() 

@questions_blueprints.route('/question', methods=['DELETE'])
def delete_question():
    ''' Route to delete a existing question'''
    return remove_question(request) 


