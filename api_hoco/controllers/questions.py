from flask import Flask, jsonify, make_response
from api_hoco.models.Question import Question
from api_hoco.util.errors import input_not_given


def register_question(request):
    '''
        Controller function to register new questions by it's name, given url and image of it's logo.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    req_body = request.get_json()

    question = req_body['question']
    answer = req_body['answer']

    if not (question and answer): 
        params_required = ['question (str)', 'answer (str)']

        return make_response(input_not_given(params_required), 400)

    try:
        new_question = Question(question, answer)
        result = new_question.save()
        
        return make_response(jsonify(result), 201)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def get_questions():
    '''
        Controller function to retrieve all the questions registered on the database
    '''
    try:
        result = Question.find_questions()

        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)

def remove_question(req):
    '''
        Controller function to delete a specific question. The user needed to pass the name of the 
        question that's going to be deleted.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    name = req.args.get('id')

    if not name: 
        params_required = ['id (str)']

        return make_response(input_not_given(params_required), 400)

    try:
        Question.delete_question(name)
        result = Question.find_questions()

        return make_response(jsonify(result), 200)
    except Exception as e:
        return make_response({'Error:': str(e)}, 500)


