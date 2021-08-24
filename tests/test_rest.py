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
    assert all(key in status for key in expected_keys) # verifica se todos os campos esperados estão presentes no status
    assert type(status["status"]) is str
    assert type(status["service"]) is str
    assert status["status"] == "operacional"
    assert status["service"] == "api-flask-example"