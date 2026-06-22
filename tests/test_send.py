import pytest
from src.utils import validar_mensagem
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client

# Testes unitários para validar_mensagem
def test_validar_mensagem_remove_espacos():
    assert validar_mensagem("  ola mundo  ") == "ola mundo"

def test_validar_mensagem_vazia_da_erro():
    with pytest.raises(ValueError) as erro:
        validar_mensagem("")
    assert "não pode estar vazia" in str(erro.value)

def test_validar_mensagem_nula_da_erro():
    with pytest.raises(ValueError) as erro:
        validar_mensagem(None)
    assert "não pode ser nula" in str(erro.value)

def test_validar_mensagem_longa_da_erro():
    mensagem_longa = "x" * 4001
    with pytest.raises(ValueError) as erro:
        validar_mensagem(mensagem_longa)
    assert "limite de 4000 caracteres" in str(erro.value)

# Testes de envio pela rota /ask
def test_envio_mensagem_invalida_retorna_bad_request(client):
    resposta = client.post("/ask", json={"message": "   "})
    assert resposta.status_code == 400
    dados = resposta.get_json()
    assert "não pode estar vazia" in dados["error"]
