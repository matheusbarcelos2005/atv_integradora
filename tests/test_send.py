import pytest

from src.chat_client import ChatClient, ChatResponse
from src.chat_service import ChatService
from src.message_validator import InvalidMessageError, MessageValidator


class RecordingChatClient(ChatClient):
    def __init__(self):
        self.received_messages = []

    def send_message(self, message: str) -> ChatResponse:
        self.received_messages.append(message)
        return ChatResponse(content="ok")


@pytest.fixture
def recording_client():
    return RecordingChatClient()


@pytest.fixture
def service(recording_client):
    return ChatService(recording_client, MessageValidator())


class TestMessageValidation:
    def test_valid_message_is_returned_trimmed(self):
        validator = MessageValidator()
        assert validator.validate("  ola mundo  ") == "ola mundo"

    def test_empty_message_is_rejected(self):
        with pytest.raises(InvalidMessageError):
            MessageValidator().validate("")

    def test_whitespace_only_message_is_rejected(self):
        with pytest.raises(InvalidMessageError):
            MessageValidator().validate("   \n\t  ")

    def test_oversized_message_is_rejected(self):
        oversized = "a" * (MessageValidator.MAX_LENGTH + 1)
        with pytest.raises(InvalidMessageError):
            MessageValidator().validate(oversized)

    def test_none_message_is_rejected(self):
        with pytest.raises(InvalidMessageError):
            MessageValidator().validate(None)


class TestSendingMessage:
    def test_service_forwards_message_to_client(self, service, recording_client):
        service.ask("Explique SOLID")
        assert recording_client.received_messages == ["Explique SOLID"]

    def test_service_trims_message_before_sending(self, service, recording_client):
        service.ask("   com espacos extras   ")
        assert recording_client.received_messages == ["com espacos extras"]

    def test_invalid_message_blocks_call_to_client(self, service, recording_client):
        with pytest.raises(InvalidMessageError):
            service.ask("")
        assert recording_client.received_messages == []

    def test_service_supports_multiple_sequential_sends(self, service, recording_client):
        service.ask("primeiro")
        service.ask("segundo")
        service.ask("terceiro")
        assert recording_client.received_messages == ["primeiro", "segundo", "terceiro"]
