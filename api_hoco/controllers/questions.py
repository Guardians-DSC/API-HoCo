from api_hoco.models.Question import Question


def register_question(question, answer):
    '''
        Controller function to register new questions by it's name, given url and image of it's logo.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    new_question = Question(question, answer)
    result = new_question.save()
    return result


def get_questions():
    '''
        Controller function to retrieve all the questions registered on the database
    '''
    result = Question.find_questions()
    return result


def remove_question(name):
    '''
        Controller function to delete a specific question. The user needed to pass the name of the 
        question that's going to be deleted.

        Parameters:
        -> request - (Flask.Request): Request object that contains all the data passed in the request.
    '''
    Question.delete_question(name)
    result = Question.find_questions()
    return result
