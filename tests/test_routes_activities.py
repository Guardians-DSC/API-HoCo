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
    id_activity_nao_cadastrada = "id n cadastrado"
    response = client.delete(f"/activity/{id_activity_nao_cadastrada}")
    response_json = response.json

    assert response.status_code == 400
    assert response_json["Error"] == "e-mail was not informed"