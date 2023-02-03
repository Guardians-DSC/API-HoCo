from unittest import mock

import pytest

from api_hoco import create_app

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })


    yield app


@pytest.fixture
def client(app):
    client = app.test_client()
    return client


@mock.patch('api_hoco.routes.questions.register_question')
def test_create_question(mock_register_question, client):
    expected_return = {
        "_id": "ID",
	    "question": "question?",
	    "answer": "answer"
    }
    mock_register_question.return_value = expected_return
    data_json = {"question": "question?", "answer": "answer"}
    response = client.post("/question", json=data_json, content_type='application/json')
    response_json = response.json

    assert response.status_code == 201
    assert response_json == expected_return


def test_create_question_missing_question(client):    
    data_json = {"question": "", "answer": "answer"}
    response = client.post("/question", json=data_json, content_type='application/json')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['question (str)', 'answer (str)']"


def test_create_question_missing_answer(client):    
    data_json = {"question": "question?", "answer": ""}
    response = client.post("/question", json=data_json, content_type='application/json')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['question (str)', 'answer (str)']"


@mock.patch('api_hoco.routes.questions.register_question')
def test_register_question_excecao_no_controller(mock_register_question, client):
    exception_msg = "uma exceção ocorreu no controller"
    mock_register_question.side_effect = Exception(exception_msg)
    data_json = {"question": "question?", "answer": "answer"}
    response = client.post("/question", json=data_json, content_type='application/json')
    response_json = response.json

    assert response.status_code == 500
    assert "Error:" in response_json


@mock.patch('api_hoco.routes.questions.remove_question')
def test_remove_question(mock_remove_question, client):
    expected_return = {'isso': 'funcionou'}
    mock_remove_question.return_value = expected_return
    id_question = "ID"
    response = client.delete(f"/question?id={id_question}")
    response_json = response.json

    assert response.status_code == 200
    assert response_json == expected_return


def test_remove_question_missing_name(client):
    response = client.delete(f"/question")
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['id (str)']"


@mock.patch('api_hoco.routes.questions.remove_question')
def test_remove_question_excecao_no_controller(mock_remove_question, client):
    exception_msg = "uma exceção ocorreu no controller"
    mock_remove_question.side_effect = Exception(exception_msg)
    id_question = "ID"
    response = client.delete(f"/question?id={id_question}")
    response_json = response.json

    assert response.status_code == 500
    assert "Error:" in response_json
