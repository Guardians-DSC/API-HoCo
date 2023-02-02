from unittest import mock
from pathlib import Path

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


@mock.patch('api_hoco.routes.activities.register_activity')
def test_create_activity(mock_register_activity, client):
    resources = Path(__file__).parent / "resources"
    expected_return = {
        "_id": "ID",
		"category": "category",
		"file": "file.pdf",
		"credits": "0",
		"e-mail": "email",
		"time": "",
		"title": "title"
    }
    mock_register_activity.return_value = expected_return
    data_form = {"category": "category", "time": "", "file": (resources / "file.pdf").open("rb"), "credits": "0", "e-mail": "email", "title": "title"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 201
    assert response_json == expected_return


def test_create_activity_missing_email(client):
    resources = Path(__file__).parent / "resources"
    
    data_form = {"category": "category", "file": (resources / "file.pdf").open("rb"), "credits": "0", "title": "title"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['e-mail (str)']"


def test_create_activity_missing_credits(client):
    resources = Path(__file__).parent / "resources"

    data_form = {"category": "category", "file": (resources / "file.pdf").open("rb"), "e-mail": "email", "title": "title"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == None


def test_create_activity_missing_certificate(client):
    resources = Path(__file__).parent / "resources"
   
    data_form = {"category": "category", "time": "", "credits": "0", "e-mail": "email", "title": "title"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == None


@mock.patch('api_hoco.routes.activities.register_activity')
def test_create_activity_server_erro(mock_register_activity, client):
    resources = Path(__file__).parent / "resources"
    exception_msg = "uma exceção ocorreu no controller"
    mock_register_activity.side_effect = Exception(exception_msg)
    data_form = {"category": "category", "time": "", "file": (resources / "file.pdf").open("rb"), "credits": "0", "e-mail": "email", "title": "title"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 500
    assert "Error:" in response_json


def test_remove_activity_email_nao_informado(client):
    id_activity = "id"
    response = client.delete(f"/activity/{id_activity}")
    response_json = response.json

    assert response.status_code == 400
    assert response_json["Error"] == "e-mail was not informed"


@mock.patch('api_hoco.routes.activities.del_user_activity')
def test_remove_activity_nao_cadastrada(mock_del_user_activity, client):
    expected_return = 0
    mock_del_user_activity.return_value = expected_return
    id_activity = "id"
    user_email = "test"
    response = client.delete(f"/activity/{id_activity}?e-mail={user_email}",)
    response_json = response.json

    assert response.status_code == 400
    assert response_json["Error"] == "activity was not deleted"


@mock.patch('api_hoco.routes.activities.del_user_activity')
def test_remove_activity_excecao_no_controller(mock_del_user_activity, client):
    exception_msg = "uma exceção ocorreu no controller"
    mock_del_user_activity.side_effect = Exception(exception_msg)
    id_activity = "id"
    user_email = "test"
    response = client.delete(f"/activity/{id_activity}?e-mail={user_email}",)
    response_json = response.json

    assert response.status_code == 500
    assert "Error" in response_json


@mock.patch('api_hoco.routes.activities.del_user_activity')
def test_remove_activity(mock_del_user_activity, client):
    expected_return = {'isso': 'funcionou'}
    mock_del_user_activity.return_value = expected_return
    id_activity = "id"
    user_email = "test"
    response = client.delete(f"/activity/{id_activity}?e-mail={user_email}",)
    response_json = response.json

    assert response.status_code == 200
    assert response_json == expected_return


def test_update_activity_id_nao_informado(client):
    data_form = {}
    response = client.patch("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['_id (str)']"


@mock.patch('api_hoco.routes.activities.edit_activity')
def test_update_activity(mock_edit_activity, client):
    expected_return = {'isso': 'funcionou'}
    mock_edit_activity.return_value = expected_return
    data_form = {"_id": "123456789"}
    response = client.patch("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 201
    assert response_json == expected_return

@mock.patch('api_hoco.routes.activities.edit_activity')
def test_update_activity_excecao_no_controller(mock_edit_activity, client):
    exception_msg = "uma exceção ocorreu no controller"
    mock_edit_activity.side_effect = Exception(exception_msg)
    data_form = {"_id": "123456789"}
    response = client.patch("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 500
    assert "Error" in response_json
