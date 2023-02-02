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


def test_create_org_missing_params(client):
    resources = Path(__file__).parent / "resources"

    data_form = {"image": (resources / "image.png").open("rb")}
    response = client.post("/org", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['name (str)', 'org_url (str)', 'image (file)']"


def test_create_org_missing_params_url(client):
    resources = Path(__file__).parent / "resources"

    data_form = {"image": (resources / "image.png").open("rb"), "name":"ORG"}
    response = client.post("/org", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 400
    assert response_json == "Parameters required: ['name (str)', 'org_url (str)', 'image (file)']"

@mock.patch('api_hoco.routes.orgs.register_org')
def test_create_org(mock_register_org, client):
    resources = Path(__file__).parent / "resources"
    expected_return = {
	    "_id": 'ID',
	    "name": "ORG",
	    "org_url": "<URL>",
	    "image": "image.png"
    }
    mock_register_org.return_value = expected_return
    data_form = {"image": (resources / "image.png").open("rb") ,"name": "ORG", "org_url": "<URL>",}
    response = client.post("/org", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 201
    assert response_json == expected_return


@mock.patch('api_hoco.routes.orgs.register_org')
def test_create_org_server_erro(mock_register_org, client):
    resources = Path(__file__).parent / "resources"
    exception_msg = "uma exceção ocorreu no controller"
    mock_register_org.side_effect = Exception(exception_msg)
    data_form = {"image": (resources / "image.png").open("rb") ,"name": "ORG", "org_url": "<URL>",}
    response = client.post("/org", data=data_form, content_type='multipart/form-data')
    response_json = response.json

    assert response.status_code == 500
    assert "Error:" in response_json
