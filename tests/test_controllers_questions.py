from unittest import mock

import pytest

@mock.patch('api_hoco.controllers.questions.register_question')
@mock.patch('api_hoco.controllers.questions.get_questions')
def test_register_question_successful(mock_register_question, mock_get_questions, controller_questions):
    question = "Question?" 
    answer = "answer"
    expected_return = [{'_id': "ID", "question": "Question?", "answer": "answer"}]
    mock_register_question = {"question": "Question?", "answer": "answer"}
    mock_get_questions.return_value = expected_return
    result = controller_questions.register_question(question, answer)
    assert result == expected_return


@mock.patch('api_hoco.controllers.questions.remove_question')
@mock.patch('api_hoco.controllers.questions.get_questions')
def test_remove_question_successful(mock_remove_question, mock_get_questions, controller_questions):
    name = "name"
    expected_return = {'_id':'ID', 'name':'name'}
    mock_get_questions.return_value = expected_return
    mock_remove_question.return_value = 1
    result = controller_questions.remove_question(name)
    assert result == expected_return
