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

'''def test_create_activity(client):
    data_form = {"category": "test", "certificate": "teste", "credits": "0", "e-mail": "teste", "title": "teste"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 201'''

def test_create_activity(client):
    expected_return = {'isso': 'funcionou'}
    data_form = {"e-mail": "teste"}
    response = client.post("/activity", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 200
    assert response_json == expected_return

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
