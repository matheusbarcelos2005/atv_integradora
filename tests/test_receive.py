import pytest

from src.chat_client import ChatClient, ChatResponse
from src.chat_service import ChatService
from src.message_validator import MessageValidator


class StubChatClient(ChatClient):
    def __init__(self, response: ChatResponse):
        self._response = response

    def send_message(self, message: str) -> ChatResponse:
        return self._response


def build_service(response: ChatResponse) -> ChatService:
    return ChatService(StubChatClient(response), MessageValidator())


class TestChatResponseStructure:
    def test_response_has_required_fields(self):
        response = ChatResponse(content="texto")
        assert response.content == "texto"

    def test_response_is_immutable(self):
        response = ChatResponse(content="x")
        with pytest.raises(Exception):
            response.content = "alterado"


class TestReceivingResponse:
    def test_content_is_propagated_from_client(self):
        expected = ChatResponse(content="Ola, mundo!")
        service = build_service(expected)
        result = service.ask("Diga ola")
        assert result.content == "Ola, mundo!"

    def test_empty_response_content_is_accepted(self):
        expected = ChatResponse(content="")
        service = build_service(expected)
        result = service.ask("teste")
        assert result.content == ""

    def test_long_response_content_is_preserved(self):
        long_text = "linha\n" * 500
        expected = ChatResponse(content=long_text)
        service = build_service(expected)
        result = service.ask("escreva um texto longo")
        assert result.content == long_text
