from unittest.mock import patch
import pytest
from src.app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client

def test_pagina_inicial_carrega(client):
    resposta = client.get("/")
    assert resposta.status_code == 200
    assert b"Atividade Integradora" in resposta.data

@patch("src.app.enviar_mensagem_api")
def test_receber_resposta_com_sucesso(mock_enviar, client):
    mock_enviar.return_value = "Resposta de sucesso da API."
    
    resposta = client.post("/ask", json={"message": "Ola, api."})
    
    assert resposta.status_code == 200
    dados = resposta.get_json()
    assert dados["content"] == "Resposta de sucesso da API."
    mock_enviar.assert_called_once()

@patch("src.app.enviar_mensagem_api")
def test_erro_ao_comunicar_com_servico_externo(mock_enviar, client):
    mock_enviar.side_effect = Exception("Erro na requisição")
    
    resposta = client.post("/ask", json={"message": "Teste"})
    
    assert resposta.status_code == 502
    dados = resposta.get_json()
    assert dados["error"] == "Falha ao se comunicar com o serviço de chat."
