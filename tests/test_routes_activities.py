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
