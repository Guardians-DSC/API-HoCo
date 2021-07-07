import pytest

from backend import rest


# Fixtures nada mais são do que variáveis personalizadas que poderão ser utilizadas nos testes.

# Essa fixture foi feita com base na recomendação de testagem da documentação do Flask,
# e o que ela faz é disponibilizar o acesso à interface da API.
@pytest.fixture
def client():
    client = rest.app.test_client()
    return client


def test_status(client):
    expected_keys = ["status", "service"]
    response = client.get("/status")
    status = response.json

    assert response.status_code == 200
    assert all(key in status for key in expected_keys)
    assert type(status["status"]) is str
    assert type(status["service"]) is str
    assert status["status"] == "operacional"
    assert status["service"] == "api-flask-example"


def test_cadastrar(client):
    assert client is not None
    nome = "um nome qualquer"
    json_request = {
        "nome": nome
    }
    expected_status_code = 200

    response = client.post("/cadastrar", json=json_request)

    response_nome = response.json["nome"]
    response_status_code = response.status_code

    assert response_nome == nome
    assert response_status_code == expected_status_code
