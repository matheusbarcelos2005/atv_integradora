import pytest

from src.ai_client import AIClient, ChatResponse
from src.chat_service import ChatService
from src.prompt_validator import PromptValidator


class StubAIClient(AIClient):
    def __init__(self, response: ChatResponse):
        self._response = response

    def send_prompt(self, prompt: str) -> ChatResponse:
        return self._response


def build_service(response: ChatResponse) -> ChatService:
    return ChatService(StubAIClient(response), PromptValidator())


class TestChatResponseStructure:
    def test_response_has_required_fields(self):
        response = ChatResponse(content="texto", model="gpt-3.5-turbo", tokens_used=10)
        assert response.content == "texto"
        assert response.model == "gpt-3.5-turbo"
        assert response.tokens_used == 10

    def test_response_is_immutable(self):
        response = ChatResponse(content="x", model="m", tokens_used=1)
        with pytest.raises(Exception):
            response.content = "alterado"


class TestReceivingResponse:
    def test_content_is_propagated_from_client(self):
        expected = ChatResponse(content="Ola, mundo!", model="gpt-3.5-turbo", tokens_used=12)
        service = build_service(expected)
        result = service.ask("Diga ola")
        assert result.content == "Ola, mundo!"

    def test_model_is_propagated_from_client(self):
        expected = ChatResponse(content="resposta", model="gpt-4o", tokens_used=5)
        service = build_service(expected)
        result = service.ask("teste")
        assert result.model == "gpt-4o"

    def test_token_usage_is_propagated_from_client(self):
        expected = ChatResponse(content="resposta", model="gpt-3.5-turbo", tokens_used=42)
        service = build_service(expected)
        result = service.ask("teste")
        assert result.tokens_used == 42

    def test_empty_response_content_is_accepted(self):
        expected = ChatResponse(content="", model="gpt-3.5-turbo", tokens_used=0)
        service = build_service(expected)
        result = service.ask("teste")
        assert result.content == ""

    def test_long_response_content_is_preserved(self):
        long_text = "linha\n" * 500
        expected = ChatResponse(content=long_text, model="gpt-3.5-turbo", tokens_used=1500)
        service = build_service(expected)
        result = service.ask("escreva um texto longo")
        assert result.content == long_text
        assert result.tokens_used == 1500
