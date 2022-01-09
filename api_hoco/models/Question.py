from flask import url_for
from .db import mongo
from bson.objectid import ObjectId

class Question:
    def __init__(self, question, answer):
        '''
            Initialization of an Object of the type Question.

            Parameters:
            -> question - (str): The question utterance
            -> answer - (str): The answer to the utterance made 
        '''
        self.question = question
        self.answer = answer

    def save(self):
        '''
            Function that saves the Question on the database used. If the question already exists on the
            database (if the name is already registered) the db register is just updated.
        '''
        question = mongo.db.questions.find_one({ 'question': self.question })

        if (question):
            mongo.db.questions.update_one({ 'question': self.question }, { '$set': vars(self) }) 

        else:
            mongo.db.questions.insert_one(vars(self)) 

        
        return mongo.db.questions.find_one({ 'question': self.question })

    @staticmethod
    def find_questions():
        '''
            Function to retrieve all questions registered in the database.
        '''
        result = mongo.db.questions.find()

        return [ question for question in result ]

    @staticmethod
    def delete_question(question_id):
        '''
            Function to delete a specific question registered. To do so, the id of the question inside de database is needed.

            Parameters:
            -> question_id - (str): The question_id of the question that's going to be deleted.
        '''
        mongo.db.questions.delete_one({ '_id': ObjectId(question_id) })


